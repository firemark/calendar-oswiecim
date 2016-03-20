FROM python:3.4
ENV PYTHONUNBUFFERED 1
ENV DJANGO_CONFIGURATION Docker
ENV DJANGO_SETTINGS_MODULE saudi.settings
RUN mkdir /code
RUN pip install -r /code/requirements.txt --upgrade
ADD webapp /code/
WORKDIR /code
