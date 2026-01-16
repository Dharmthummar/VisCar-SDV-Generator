# VisCar SDV GenAI Generator - Dockerfile

FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Rust (for Rust code generation support)
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy framework code
COPY framework/ ./framework/
COPY applications/ ./applications/
COPY antigravity.yaml .

# Set environment variables
ENV PYTHONPATH=/app
ENV GEMINI_API_KEY=""
ENV JULES_API_KEY=""

# Create output directory
RUN mkdir -p /app/output

# Default command
CMD ["python", "-m", "framework"]

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import framework; print('healthy')" || exit 1

# Labels
LABEL maintainer="VisCar Team"
LABEL description="SDV GenAI Application Generator"
LABEL version="1.0.0"
