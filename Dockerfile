FROM python:3.7.13-slim-bullseye
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apt-get update && \
    apt-get install -y gcc libpq-dev libsnmp-dev && \
    rm -rf /var/lib/apt/lists/* 
COPY . .
RUN pip install --no-cache -r requirements.txt
CMD ["python3", "scheduler.py"]
