FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/src

COPY ./tests/ /code/tests

COPY ./setup.py /code/setup.py

RUN pip install -e /code/.

CMD ["uvicorn", "src.recipe_api.main:app", "--host", "0.0.0.0", "--port", "80"]
