FROM python:3.10-slim

RUN addgroup --system appgrp && \
    adduser --system --ingroup appgrp appusr

WORKDIR /app

COPY app.py .
COPY requirements.txt .

RUN chown -R appusr:appgrp /app && \
    pip3 install --no-cache-dir -r requirements.txt

USER appusr

EXPOSE 8080

CMD ["python3", "app.py"]
