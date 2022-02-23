FROM python:3.8.5
#Set src files
RUN mkdir api
WORKDIR /api/
COPY app /api/app
COPY Pipfile /api/Pipfile
COPY Pipfile.lock /api/Pipfile.lock
COPY .env /api/.env

RUN pip install pipenv 
RUN pipenv --python 3.8.5
RUN pipenv install 

CMD ["pipenv", "run", "uvicorn", "--port", "8000", "--host", "0.0.0.0", "app.main:app"]
