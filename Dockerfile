FROM ubuntu:18.04

# Add Maintainer Info
LABEL maintainer="Vasileios Giotsas <vasilis.giotsas@gmail.com>"

# Install aws-cli v2
RUN apt update && apt install -y unzip curl python3
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install

# Set the Current Working Directory inside the container
WORKDIR /app

# Copy the files from the current directory to the Working Directory inside the container
ADD . .

RUN chmod +x ./start_crawl
RUN chmod +x ./aws_sync
RUN chmod +x ./ingest_es.py

# Command to run the executable
CMD ["./start_crawl"]