FROM python:3.11.1-slim

# Set workdir
WORKDIR /app

# Copy source code
COPY ./src /app
COPY ./src/requirements.txt /app/

# Install system dependencies
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y \
    locales \
    libmemcached-dev \
    libjpeg-dev \
    zlib1g-dev \
    build-essential \
    python3-dev \
    python3-setuptools \
    gcc \
    make && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Setup locale
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
    && locale-gen && dpkg-reconfigure locales

# Create and activate virtual environment
RUN python3 -m venv /opt/venv

# Upgrade pip & install dependencies
RUN /opt/venv/bin/pip install --upgrade pip
RUN /opt/venv/bin/pip install -r requirements.txt

# (Optional) Buat script kamu executable, kalau memang ada
RUN chmod +x config/migrate.sh || true
RUN chmod +x config/entrypoint.sh || true

# Set PATH agar command `python` & `pip` langsung jalan dari venv
ENV PATH="/opt/venv/bin:$PATH"

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]