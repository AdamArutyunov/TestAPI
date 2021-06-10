# Base
FROM python:3-onbuild

# Environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

# Port expose
EXPOSE 8000
