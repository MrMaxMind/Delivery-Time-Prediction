# Use Python base image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy project files into the container
COPY . /app

# Create a virtual environment in the container
RUN python -m venv venv

# Activate the virtual environment and install dependencies
RUN . /app/venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

# Ensure the virtual environment is used when running commands
ENV PATH="/app/venv/bin:$PATH"

# Define environment variable
ENV FLASK_ENV=production

# Expose port
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
