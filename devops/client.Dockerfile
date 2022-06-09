FROM ubuntu:latest

# Download Package Information
RUN apt-get update -y

ENV DEBIAN_FRONTEND noninteractive 

# Download tzdata
RUN apt-get install -y --no-install-recommends tzdata

# Downlaod python, pip and tk
RUN apt-get install -y python3 python3-pip python3-tk

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .
