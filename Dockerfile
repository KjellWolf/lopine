# syntax=docker/dockerfile:1
FROM python:3.12
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
#RUN apt-get update && apt-get install -y netcat
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]