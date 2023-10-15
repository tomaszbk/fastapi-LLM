from python:3.11.6

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app app
