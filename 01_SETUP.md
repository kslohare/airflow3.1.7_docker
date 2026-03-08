
# airflow3.1.7_docker

## Know versions since they break things
python3 --version

https://airflow.apache.org/docs/apache-airflow/stable/installation/prerequisites.html
airflow 3.1.7

Reference: [YouTube Setup Guide](https://www.youtube.com/watch?v=IiczxlbQb8s&t=3338s)

## 1. Create Required Folders

Open an empty folder in VS Code and create the following directories:

```sh
mkdir -p config dags logs plugins
touch .gitignore
```

## 2. Download docker-compose.yaml
```sh
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/3.1.7/docker-compose.yaml'
```

This will create containers for components like the DAG processor, scheduler, API, etc.
**Additional configuration:**

- After `postgres:volumes`, add the following to access from your local machine:
	```yaml
	ports:
		- "5432:5432"
	```
- Set the following environment variable to stop loading example DAGs:
	```yaml
	AIRFLOW__CORE__LOAD_EXAMPLES: 'false'
	```

## 3. Create .env File
Create a `.env` file in the root folder and define the following variable:
```sh
echo "AIFFLOW_UID=50000" > .env
```

## 4.1 Verify comptible python version - If Python version is incompatible, pip will throw error.
```sh
pip install "apache-airflow==3.1.7" --dry-run
```


## 4. Create Virtual Environment (for local development)
To suppress warnings and manage dependencies:
```sh
pip install uv
uv init
uv sync
.venv/Scripts/activate  # On Windows
# or
source .venv/bin/activate  # On Linux/Mac
```

This will create a `.git` folder, `.python-version`, and `uv.lock`.

## 5. Install Airflow
```sh
# uv add apache-airflow
#uv pip install apache-airflow==3.1.7 --constraint constraints-3.11.txt
uv pip install apache-airflow==3.1.7
```

This will create `pyproject.toml`.

## 6. Start Docker Containers
```sh
docker compose up -d
```
```text
1. What happens when you run docker compose up -d

When you run:

docker compose up -d

Docker Compose looks for a file called:

docker-compose.yml

in your project folder.

This file tells Docker:

	Which containers to start

	Which Docker images to use

	Which ports to expose

	Which folders from your VS Code project should be mounted inside the container

So Docker Compose reads this file, not VS Code.
```

This will run the Docker containers in detached mode and create a stack under `airflowtutorial` in Docker Desktop.

## 7. UI Intro
- **Asset**
- **XCOM**: Helps to build stateful DAGs


## 8. What is the role of docker-compose.yaml file and airflow.cfg file in Airflow 3.1.7 version, how they differ
### Role of airflow.cfg
Airflow Config Creation:
When you create your first DAG, the `config/airflow.cfg` file will be created automatically. 

This file belongs to Airflow itself.
It defines:

	DAG folder location

	Executor type

	Logging settings

	Scheduler behavior

	Timezone

	Security configs

Think of it as:
⚙ Internal Airflow engine configuration

# What Is airflow-init?
```text
airflow-init is a one-time initialization service defined in docker-compose.yaml.
It is not a permanent Airflow component like:
scheduler
webserver
worker
It runs once to prepare Airflow before starting other services.

Why Do We Need It?
When Airflow starts for the first time, it needs to:
	Create metadata database tables
	Run database migrations
	Create admin user
	Set correct folder permissions
2) p
If this step is skipped → webserver/scheduler will fail.
So airflow-init prepares everything.
```

# Key Differences between DOcker and Docker Compose File
```text| Feature       | Docker                      | Docker Compose                   |
| ------------- | --------------------------- | -------------------------------- |
| Purpose       | Run single container        | Run multi-container applications |
| Command style | CLI commands                | YAML configuration               |
| Configuration | Mostly command line         | `docker-compose.yml` file        |
| Use case      | Simple apps                 | Microservices apps               |
| Startup       | Run containers individually | Start all containers together    |

```

# What is Service
```text
In docker compose world, container is called Service

```

# Always use double spaces when working with YAML

# Healthcheck Importance in multi-service(muliple container within same n/w) systems
## 1 Why healthcheck is needed in multi-service(muliple container within same n/w) systems
```text
In many systems (like Apache Airflow, web apps, microservices), services depend on each other.
Example architecture:
Web App
   │
   ▼
API Service
   │
   ▼
Database

Problem: Even if Docker starts the database container first, it may not yet be ready to accept connections.
Example timeline:
Container started → Database still initializing → App tries to connect → FAIL
Healthcheck solves this.
```
## 2 What healthcheck does
```text
Healthcheck periodically runs a test command inside the container to verify that the service is working.
Example check:
Is port open?
Is HTTP endpoint responding?
Is database accepting connections?
If the test passes → container status = healthy

If it fails → container status = unhealthy
```
## 3 Where healthcheck appears
Inside docker-compose.yml
Example:
```yaml
services:
  web:
    image: nginx
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost"]
      interval: 30s
      timeout: 10s
      retries: 3
```
# Docker storage
| Bind Mount           | Named Volume        |
| -------------------- | ------------------- |
| Uses host directory  | Managed by Docker   |
| Good for development | Good for production |
| Requires full path   | Only volume name    |
| Easy debugging       | Better isolation    |

# Interact with postgres from Inside container
```sh
docker ps | grep "postgres"
docker exec -it airflow317_docker-postgres-1 psql -U airflow
\dt  # Display Tables

```

# 

## Vs Code with Docker
1) Install Material thing Icon
2) pip install uv
3) uv init # This will create virutal env for me

