# Test app for learn FastAPI

![preview image](docs/preview.png)

## Run local

- For work in network

    ```bash
    uvicorn app.main:app --reload --port 8000 --host 0.0.0.0
    ```
- For work in local machine

    ```bash
    uvicorn app.main:app --reload --port 8000 --host localhost
    ```

> it is written on the course https://stepik.org/course/179694/syllabus
