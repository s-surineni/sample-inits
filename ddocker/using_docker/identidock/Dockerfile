FROM python:3.4

RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
# ENV HTTP_PROXY "http://www-proxy.us.oracle.com:80"
# ENV HTTPS_PROXY "http://www-proxy.us.oracle.com:80"
# ENV FTP_PROXY "http://www-proxy.us.oracle.com:80"

RUN pip install Flask==0.10.1 uWSGI requests==2.5.1
WORKDIR /app
COPY app /app
COPY cmd.sh /

EXPOSE 9090 9191
USER uwsgi

CMD ["/cmd.sh"]
