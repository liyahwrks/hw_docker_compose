FROM python:3.13-slim

WORKDIR /var/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY docker-app/build/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY . .

ENTRYPOINT ["/entrypoint.sh"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]