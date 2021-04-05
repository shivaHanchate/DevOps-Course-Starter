FROM python:3.8-slim-buster as base

WORKDIR /app
COPY poetry.lock pyproject.toml /app/
RUN apt-get update && apt-get install -y curl && pip install poetry && poetry install --no-root 
EXPOSE 5000

FROM base as production
COPY ./todo_app /app/todo_app
ENV PYTHONPATH=/app
RUN poetry add gunicorn
EXPOSE $PORT
ENTRYPOINT ["poetry","run","gunicorn","-w","4","-b","0.0.0.0:$PORT","todo_app.app:app"]

FROM base as development
ENV FLASK_APP todo_app/app.py
ENV FLASK_ENV development
ENTRYPOINT ["poetry","run","flask","run","--host=0.0.0.0"]

FROM base as test
ENV FLASK_APP todo_app/app.py
# Install Chrome for Selenium
RUN curl https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o /chrome.deb
RUN dpkg -i /chrome.deb || apt-get install -yf
RUN rm /chrome.deb
# Install chromedriver for Selenium
RUN LATEST=`curl -sSL https://chromedriver.storage.googleapis.com/LATEST_RELEASE` && echo $LATEST && curl https://chromedriver.storage.googleapis.com/${LATEST}/chromedriver_linux64.zip -o /app/chromedriver.zip
RUN apt-get install unzip -y && unzip ./chromedriver.zip
COPY . .
ENTRYPOINT ["poetry","run","pytest"]