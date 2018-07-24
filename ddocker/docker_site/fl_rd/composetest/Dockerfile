FROM python:3.4-alpine
ENV HTTP_PROXY "http://www-proxy.us.oracle.com:80"
ENV HTTPS_PROXY "http://www-proxy.us.oracle.com:80"
ENV FTP_PROXY "http://www-proxy.us.oracle.com:80"
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "app.py"]