FROM python:3.7.13-slim-bullseye as builder
WORKDIR /app
RUN apt-get update && \
    apt-get install -y gcc libpq-dev libsnmp-dev && \
    rm -rf /var/lib/apt/lists/* 
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

FROM python:3.7.13-slim-bullseye
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apt-get update && \
    apt-get install -y libsnmp-dev && \
    rm -rf /var/lib/apt/lists/* 
COPY --from=builder /app/wheels /wheels
COPY . .
RUN pip install --no-cache /wheels/*
CMD ["python3", "scheduler.py"]
