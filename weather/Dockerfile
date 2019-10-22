FROM python:3

WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY weather.py .
COPY api_conf.json .

CMD ["python3", "./weather.py"]  