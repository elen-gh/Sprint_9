FROM python:3.14-slim

WORKDIR /app

ENV PYTHONPATH=/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["pytest", "--alluredir", "allure-results"]
 
