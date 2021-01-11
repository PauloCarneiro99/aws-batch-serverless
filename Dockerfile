FROM nvidia/cuda:11.0-base

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl ca-certificates git \
    python3 python3-dev python3-pip \
    build-essential manpages-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \
    python3 get-pip.py && \
    rm get-pip.py

COPY . .
RUN pip3 install -r requirements.txt