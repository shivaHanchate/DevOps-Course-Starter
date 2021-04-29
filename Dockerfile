FROM python:3.8-slim-buster as base

WORKDIR /app
COPY poetry.lock pyproject.toml /app/
RUN apt-get update && apt-get install -y curl && pip install poetry 
RUN poetry config virtualenvs.create false --local && poetry install --no-root
EXPOSE 5000

FROM base as production
COPY ./todo_app /app/todo_app
ENV PYTHONPATH=/app
RUN poetry add gunicorn
ENV PORT=8000
EXPOSE $PORT
COPY ./entrypoint_prod.sh ./
RUN chmod +x entrypoint_prod.sh
ENTRYPOINT ["./entrypoint_prod.sh"]

FROM base as development
ENV FLASK_APP todo_app/app.py
ENV FLASK_ENV development
COPY ./entrypoint_dev.sh ./
RUN chmod +x entrypoint_dev.sh
ENTRYPOINT ["./entrypoint_dev.sh"]

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
ENTRYPOINT [ "poetry", "run", "pytest" ]