# Vocab

## 🔑 What is an Identity Provider (IdP)?
Simple Analogy:

Think of logging into apps like entering a secured office:

You (user) → want to enter
App (Airflow, website) → building you want access to
Identity Provider (IdP) → security guard checking your ID

👉 Instead of every building hiring its own guard, they trust a central security system.

An Identity Provider is a system that:

✅ Authenticates users

(Verifies who you are — username/password, OTP, SSO, etc.)

✅ Issues identity proof

(Usually a token like JWT)

👉 Example:

Microsoft Azure Active Directory is an Identity Provider.

Others:

Google Identity Platform
Okta
Auth0


## Tenant ID and Client ID
Think of Microsoft Azure Active Directory like a large corporate campus:

Tenant ID = 🏢 The campus itself (your organization)

Client ID = 🪪 Your specific app’s ID badge

👉 So:

Tenant = who owns the identity system

Client = which app is asking for login

🔑 What is Tenant ID?
👉 Definition

A Tenant ID identifies your organization (Azure AD instance).

It is a globally unique identifier (GUID), Represents your company’s identity directory

Example:
Tenant ID = a1b2c3d4-xxxx-xxxx-xxxx-abcdef123456

Think:

“Which organization is authenticating this user?”

🧾 What is Client ID? 👉 Definition

A Client ID identifies a specific application registered in Azure.

Each app gets its own Client ID

Used during OAuth flow to tell Azure:

“This request is coming from THIS app”

Example:
Client ID = 9f8e7d6c-xxxx-xxxx-xxxx-abcdef654321
Think:

“Which application is requesting login?”

⚖️ Key Differences
| Feature      | Tenant ID 🏢               | Client ID 🪪            |
| ------------ | -------------------------- | ----------------------- |
| Represents   | Organization               | Application             |
| Scope        | One per Azure AD           | One per app             |
| Purpose      | Identify identity provider | Identify requesting app |
| Used in URL  | Yes (OAuth endpoints)      | No                      |
| Created when | Azure AD created           | App registration        |


# Security: OAuth2 (Azure AD) Implementation in Apache Airflow

Implementing OAuth2 (Azure AD) in Apache Airflow is a very practical use case—especially in enterprise setups like yours. I'll explain it step-by-step with a clear analogy + actual config so it sticks.

## 🧠 First: Concept (Analogy)

Think of Airflow UI like an office building:

- Airflow = Office building
- Azure AD = Security gate with ID cards
- OAuth2 = The process of checking your ID
- Token = Your temporary visitor pass

👉 Instead of Airflow managing usernames/passwords, it asks Azure:

"Is this person valid?"
Azure says "Yes" and gives a token, and Airflow trusts it.

## Architecture Overview

User → Airflow UI → Azure AD Login → Token → Airflow (via Flask AppBuilder)

Airflow uses:
- Flask AppBuilder (FAB) for auth
- OAuth provider = Azure AD

## Implementation - Start

### ⚙️ Step 1: Register App in Azure

Go to:
👉 Microsoft Azure Portal

Create App Registration
Azure Active Directory → App registrations → New registration
Set:
- Name: airflow-auth

Redirect URI:

http://<your-airflow-url>/oauth-authorized/azure

After creation, note:
- Client ID
- Tenant ID

Create Client Secret
Go to "Certificates & Secrets"
Create new secret → copy value

### 🔐 Step 2: Configure Airflow

Airflow uses FAB config via webserver_config.py

👉 Location:

$AIRFLOW_HOME/webserver_config.py

🧾 Example Config

```python
from flask_appbuilder.security.manager import AUTH_OAUTH

AUTH_TYPE = AUTH_OAUTH

OAUTH_PROVIDERS = [
    {
        'name': 'azure',
        'icon': 'fa-windows',
        'token_key': 'access_token',
        'remote_app': {
            'client_id': '<CLIENT_ID>',
            'client_secret': '<CLIENT_SECRET>',
            'api_base_url': 'https://graph.microsoft.com/v1.0/',
            'client_kwargs': {
                'scope': 'User.Read'
            },
            'request_token_url': None,
            'access_token_url': 'https://login.microsoftonline.com/<TENANT_ID>/oauth2/v2.0/token',
            'authorize_url': 'https://login.microsoftonline.com/<TENANT_ID>/oauth2/v2.0/authorize',
        }
    }
]
```

### 👤 Step 3: Map Azure User → Airflow User

Add this in same file:

```python
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = "Viewer"
```

👉 This auto-creates users when they login.

### 🔎 Step 4: Fetch User Info from Azure

Add custom user info function:

```python
def azure_user_info(response=None):
    me = current_app.appbuilder.sm.oauth_remotes['azure'].get('me').json()
    return {
        "username": me["userPrincipalName"],
        "first_name": me.get("givenName", ""),
        "last_name": me.get("surname", ""),
        "email": me["mail"] or me["userPrincipalName"],
    }
```

Then register it:

```python
OAUTH_PROVIDERS[0]['user_info'] = azure_user_info
```

### 🔁 Step 5: Restart Airflow

```bash
airflow webserver restart
airflow scheduler restart
```

### ✅ Step 6: Test Login

Open Airflow UI:

http://<your-airflow-url>

You should see:

👉 Login with Azure button



