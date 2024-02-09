FROM python:3.10-alpine
LABEL authors="Ilnur"

#EXPOSE 8000

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN mkdir db_local
RUN pip install -r requirements.txt

COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "1234"]

