#!/bin/bash

# Step 1: Build the Docker image
docker build -t flask-app .

# Step 2: Run the Docker container, mapping port 5000 on the container to port 5000 on the host
docker run -p 5000:5000 flask-app
