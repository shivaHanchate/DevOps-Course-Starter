FROM python:3.8-slim-buster as base

WORKDIR /app
COPY poetry.lock pyproject.toml /app/

RUN pip install poetry && poetry install --no-root && poetry add gunicorn
EXPOSE 5000

FROM base as production
COPY ./todo_app /app/todo_app
ENV PYTHONPATH=/app
ENTRYPOINT ["poetry","run","gunicorn","-w","4","-b","0.0.0.0","todo_app.app:app"]

FROM base as development
ENV FLASK_APP todo_app/app.py
ENV FLASK_ENV development
ENTRYPOINT ["poetry","run","flask","run","--host=0.0.0.0"]