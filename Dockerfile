# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Run the command to start the application (this will be overridden by docker-compose for initial setup)
CMD ["uvicorn", "your_project_name.asgi:application", "--host", "0.0.0.0", "--port", "8000"]
