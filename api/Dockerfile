FROM python:3.10.2-alpine3.15
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE 5000

CMD [ "python3", "main.py"]