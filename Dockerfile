# Base Image-a light-weight Python use pannrom
FROM python:3.9-slim

# Working directory set panrom
WORKDIR /app

# Application code-a copy panrom
COPY app.py .

# Container run aagum podhu app.py execute aagum
CMD ["python", "app.py"]
