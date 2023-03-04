FROM python:3.9

WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY app.py .

# Set the default environment variables
ENV PORT=6080
ENV DATA_FILE=/app/config.txt

# Expose the application port
EXPOSE $PORT

# Start the CherryPy server
CMD ["python3", "app.py"]
