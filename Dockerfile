FROM python:3.10-alpine
LABEL authors="Ilnur"

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT ["uvicorn"]

CMD ["--port", "8000", "main:app"]

EXPOSE 8000:8000