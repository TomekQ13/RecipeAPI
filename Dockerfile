FROM python:3.8
WORKDIR /RecipesApp/
RUN pip install pipenv


COPY Pipfile Pipfile.lock .env ./
RUN pipenv install --system --deploy

COPY . .
CMD ["python", "app/app.py"]