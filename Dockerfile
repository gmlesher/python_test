# Python version for image build
ARG PYTHON_VERSION=3.13

# Get specified python version docker image. Alpine is a tiny linux distro.
FROM python:${PYTHON_VERSION}-alpine AS base

# Install uv (python package manager) via apk
RUN apk add --no-cache uv

# Install ruff via apk
RUN apk add ruff

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy the source code into the container
COPY . .

# Run on port
# EXPOSE 7878

# Set the command to run the app
CMD ["uv", "run", "app.py"]
