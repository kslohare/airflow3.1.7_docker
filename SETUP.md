
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

This will run the Docker containers in detached mode and create a stack under `airflowtutorial` in Docker Desktop.

## 7. UI Intro
- **Asset**
- **XCOM**: Helps to build stateful DAGs