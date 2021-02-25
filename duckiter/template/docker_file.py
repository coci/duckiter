from jinja2 import Template

dockerfile = \
    """
FROM python:{{ python_version }}

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . /app

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

{{ migrate }}
{{ project_server }}
"""
