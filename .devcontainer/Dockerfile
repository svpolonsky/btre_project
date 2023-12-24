# Build image:
# docker build -t real-estate-image .
# Run container interactively
# docker run --rm -it --name real-estate-container real-estate-image


# Start with Ubuntu 18.04 as the base image
FROM ubuntu:22.04

# Optionally set a maintainer or author of the Dockerfile
LABEL maintainer="spolonsky@icloud.com"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y sudo

# Update the package list
RUN apt-get update && \
    apt-get install -y git python3-dev python3-pip libpq-dev postgresql postgresql-contrib nginx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install django gunicorn psycopg2-binary

# Create a new user 'djangoadmin' and set up a home directory
RUN useradd -m djangoadmin 
# Add 'djangoadmin' to the sudo group to give root privileges
RUN usermod -aG sudo djangoadmin
# Give 'djangoadmin' passwordless sudo privileges
RUN echo 'djangoadmin ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/djangoadmin && chmod 0440 /etc/sudoers.d/djangoadmin




USER djangoadmin



# Copy files from your host to the container
# Here, we are copying everything in the current directory on the host
# to the /app directory in the container
#COPY . /app

# Set the working directory to /app so the following commands run in this directory
WORKDIR /app

# Install Python modules, most importntly Django
RUN pip install django gunicorn psycopg2-binary

# python3 -m pip install -r requirements.txt

# Command to run your program
#CMD ["python3", "your_script.py"]
CMD ["/bin/bash"]
