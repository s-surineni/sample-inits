FROM python:3.4

RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
ENV HTTP_PROXY "http://www-proxy.us.oracle.com:80"
ENV HTTPS_PROXY "http://www-proxy.us.oracle.com:80"
ENV FTP_PROXY "http://www-proxy.us.oracle.com:80"

RUN pip install Flask==0.10.1 uWSGI==2.0.8
WORKDIR /app
COPY app /app

EXPOSE 9090 9191
USER uwsgi

CMD ["uwsgi", "--http", "0.0.0.0:9090", "--wsgi-file", "/app/identidock.py", \
    "--callable", "app", "--stats", "0.0.0.0:9191"]