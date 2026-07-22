FROM python:3.12-slim

WORKDIR /app

COPY app.py .

#
# Create a large file to simulate a production container image
#
RUN dd if=/dev/zero of=/app/test-data.bin bs=1M count=800

EXPOSE 8080

CMD ["python3", "app.py"]
