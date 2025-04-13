FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8050

CMD ["gunicorn", "--config", "gunicorn.conf.py", "main:server"]
