FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install requests pytest
CMD ["pytest", "test.py"]