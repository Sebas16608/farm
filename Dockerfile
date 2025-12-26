# -----------------------------
# Base
# -----------------------------
FROM python:3.13-slim

# Evitar .pyc y logs buffer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Dependencias del sistema (psycopg2 / Pillow / etc)
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
       libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# -----------------------------
# Dependencias Python
# -----------------------------
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# -----------------------------
# Código del proyecto
# -----------------------------
COPY . .

# Crear carpeta static
RUN mkdir -p /app/static

# -----------------------------
# Collectstatic + Gunicorn
# -----------------------------
CMD python manage.py collectstatic --noinput && \
    gunicorn Farm.wsgi:application --bind 0.0.0.0:8000
