FROM python:3.4

ENV HTTP_PROXY "http://www-proxy.us.oracle.com:80"
ENV HTTPS_PROXY "http://www-proxy.us.oracle.com:80"
ENV FTP_PROXY "http://www-proxy.us.oracle.com:80"

RUN pip install Flask==0.10.1
WORKDIR /app
copy app /app

CMD ["python", "identidock.py"]