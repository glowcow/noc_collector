FROM python:3.9.12-slim-bullseye
WORKDIR /app
ENV PYTHONUNBUFFERED 1
RUN apt-get update && \
    apt-get install -y gcc libpq-dev libsnmp-dev && \
    rm -rf /var/lib/apt/lists/* 
COPY . .
RUN pip install --no-cache -r requirements.txt
CMD ["python", "scheduler.py"]
