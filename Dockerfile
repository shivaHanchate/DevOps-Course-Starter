FROM python:3.8-slim-buster as base

WORKDIR /app
COPY poetry.lock pyproject.toml /app/
RUN apt-get update && apt-get install -y \curl
CMD /bin/bash
RUN pip install poetry && poetry install --no-root 
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

FROM base as test
COPY . .
ENV FLASK_APP todo_app/app.py
ENV PYTHONPATH=/app
# Install Chrome for Selenium
RUN curl https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o /chrome.deb
RUN dpkg -i /chrome.deb || apt-get install -yf
RUN rm /chrome.deb
# Install chromedriver for Selenium
RUN curl https://chromedriver.storage.googleapis.com/2.31/chromedriver_linux64.zip -o /usr/local/bin/chromedriver
RUN chmod +x /usr/local/bin/chromedriver
ENTRYPOINT ["poetry","run","pytest"]