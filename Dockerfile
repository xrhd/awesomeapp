FROM python:3.12-slim

# Install uv for fast package management
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Set working directory
WORKDIR /app

# Copy dependency definition files
COPY pyproject.toml uv.lock ./

# Install dependencies
# --frozen ensures we use exact versions from uv.lock
# --no-dev excludes development dependencies like pytest
RUN uv sync --frozen --no-dev

# Download dataset during build to avoid runtime rate limits
RUN apt-get update && apt-get install -y curl && \
    curl -L -o quotes.jsonl https://huggingface.co/datasets/Abirate/english_quotes/resolve/main/quotes.jsonl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*


# Copy application code
COPY src ./src
COPY templates ./templates
COPY static ./static

# Cloud Run defaults to port 8080
ENV PORT=8080

# Run the application
# Use uv run to execute in the virtual environment created by sync
CMD ["uv", "run", "fastapi", "run", "src/main.py", "--port", "8080"]
