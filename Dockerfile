# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Add a non-root user for running the application
RUN adduser --disabled-password --gecos '' appuser

# Set the working directory and copy app files
WORKDIR /app
COPY . /app

# Install dependencies with root privileges
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Change ownership of the app directory to the non-root user
RUN chown -R appuser:appuser /app

# Switch to the non-root user
USER appuser

# Expose the Flask port
EXPOSE 5000

# Run the Flask server with ENTRYPOINT
ENTRYPOINT ["python", "app.py"]
