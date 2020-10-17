FROM python:latest
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
COPY . /code/
WORKDIR /code
RUN pip install -r requirements.txt
EXPOSE 8000
VOLUME /code
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# docker run -it --volume "$(PWD)":/code multiuser django-admin startproject multi_user .
# docker run  --volume "$(PWD)":/code -p 8000:8000 --name multiuser multiuser
