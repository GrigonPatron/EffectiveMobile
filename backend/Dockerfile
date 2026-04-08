FROM python:3.14-slim

WORKDIR /app

COPY app.py .

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
HEALTHCHECK --interval=5s --timeout=2s --retries=5 \
  CMD curl -f http://localhost:8080/ || exit 1

RUN useradd -m grigorii
USER grigorii

EXPOSE 8080

CMD ["python", "app.py"]