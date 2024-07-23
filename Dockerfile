# Use a base image with Ubuntu 22.04
FROM ubuntu:22.04

# Update and install basic system dependencies
RUN apt-get update && \
    apt-get install -y apt-transport-https ca-certificates && \
    apt-get update && \
    apt-get install -y \
    build-essential \
    wget \
    make \
    gcc \
    g++ \
    perl \
    python3 \
    python3-pip \
    python3-venv \
    libexpat1-dev \
    libxml2-dev \
    zlib1g-dev \
    libncurses5-dev \
    libbz2-dev \
    libgdbm-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt into the container
COPY requirements.txt .

# Install Python packages
RUN pip3 install --no-cache-dir -r requirements.txt

# Install EMBOSS 
# Download EMBOSS
RUN wget ftp://emboss.open-bio.org/pub/EMBOSS/EMBOSS-6.6.0.tar.gz -O /tmp/EMBOSS-6.6.0.tar.gz || { echo "Download failed"; exit 1; }
#RUN wget ftp://emboss.open-bio.org/pub/EMBOSS/EMBOSS-6.6.0.tar.gz && \

# Extract EMBOSS
RUN tar -xzf /tmp/EMBOSS-6.6.0.tar.gz -C /tmp || { echo "Extraction failed"; exit 1; }

# Change to EMBOSS directory
WORKDIR /tmp/EMBOSS-6.6.0

# Configure EMBOSS
RUN ./configure --without-x || { echo "Configuration failed"; exit 1; }

# Build EMBOSS
RUN make || { echo "Build failed"; exit 1; }

# Install EMBOSS
RUN make install || { echo "Installation failed"; exit 1; }

# Cleanup
WORKDIR /
RUN rm -rf /tmp/EMBOSS-6.6.0.tar.gz /tmp/EMBOSS-6.6.0

# Remove additional caches
RUN rm -rf /root/.cache /var/cache/apt/*

# Set the default command to open a bash shell
CMD ["/bin/bash"]
