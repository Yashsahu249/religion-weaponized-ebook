# Use the official Python 3.11 slim image as the base image
FROM python:3.11-slim

# Install font packages needed by book_cover_generator.py
RUN apt-get update && apt-get install -y --no-install-recommends \
    fonts-dejavu-core \
 && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy and install Python dependencies first (layer-cache friendly)
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Default command: generate cover, PDF, and EPUB
CMD ["python", "build.py"]