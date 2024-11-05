# Use the official Python image from the Docker Hub
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file to the container
COPY requirements.txt /usr/src/app/

# Install dependencies
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# Copy the rest of the application code to the container
COPY . /usr/src/app

# Expose the port that Streamlit runs on
EXPOSE 8501

# Command to run the Streamlit app
ENTRYPOINT ["streamlit", "run", "main_app.py", "--server.port=8501", "--server.address=0.0.0.0"]