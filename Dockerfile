# Use the official Python 3.12 slim image as the base
FROM python:3.12-slim

# Install system dependencies (including build essentials and libpq for PostgreSQL)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Install Poetry
ENV POETRY_VERSION=1.5.0
ENV PATH="/root/.local/bin:$PATH"
RUN pip install "poetry==$POETRY_VERSION"

# Set the working directory
WORKDIR /app

# Copy the Poetry configuration files first (for caching dependency installation)
COPY pyproject.toml poetry.lock ./

# Configure Poetry to install dependencies globally (without virtualenv) and install production dependencies only.
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-dev

# Copy the rest of the application code
COPY . .

# Expose the port (assuming your API listens on 8000)
EXPOSE 8000

# Default command to run the API.
# To run migrations, you can override this command (see docker-compose instructions below).
CMD ["python", "src/__main__.py", "runapi"]
