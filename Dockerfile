FROM python:3.8-slim-buster as base

WORKDIR /app
COPY poetry.lock pyproject.toml /app/
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - && poetry install --no-root 
EXPOSE 5000

FROM base as production
COPY ./todo_app /app/todo_app
ENV PYTHONPATH=/app
RUN poetry add gunicorn
ENTRYPOINT ["poetry","run","gunicorn","-w","4","-b","0.0.0.0","todo_app.app:app"]

FROM base as development
ENV FLASK_APP todo_app/app.py
ENV FLASK_ENV development
ENTRYPOINT ["poetry","run","flask","run","--host=0.0.0.0"]