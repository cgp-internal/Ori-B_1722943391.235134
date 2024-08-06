#!/bin/bash

# Install Python
apt-get update -y
apt-get install python3 -y
apt-get install pip -y

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install required dependencies
pip install -r requirements.txt

# Create database
alembic init alembic
alembic upgrade head

# Start the server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000