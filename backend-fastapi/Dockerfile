FROM python:3.12-slim
RUN apt-get update && apt-get install -y libpango-1.0-0 libpangoft2-1.0-0 libjpeg62-turbo libffi8 libxml2 libxslt1.1 libharfbuzz0b && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY app ./app
COPY templates ./templates
ENV PORT=3000
EXPOSE 3000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3000"]
