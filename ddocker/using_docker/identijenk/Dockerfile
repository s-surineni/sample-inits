FROM jenkins/jenkins:latest
USER root
RUN apt-get update \
        && apt-get install -y apt-transport-https \
        && apt-get install -y sudo \
        && apt-get install -y ca-certificates \
        && apt-get install -y curl \
        && apt-get install -y gnupg-agent \
        && apt-get install -y software-properties-common \
        && curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - \
        && apt-key fingerprint 0EBFCD88 \
        && add-apt-repository \
        "deb [arch=amd64] https://download.docker.com/linux/debian \
        $(lsb_release -cs) \
        stable" \
        && apt-get update \
        && apt-get install -y docker-ce
        # docker-ce-cli containerd.io
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers
# RUN curl -L https://github.com/docker/compose/releases/download/1.27.4/\
#         docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose; \
#         chmod +x /usr/local/bin/docker-compose
RUN curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose; \
        chmod +x /usr/local/bin/docker-compose
USER jenkins
COPY plugins.txt /usr/share/jenkins/plugins.txt
RUN xargs /usr/local/bin/install-plugins.sh < /usr/share/jenkins/plugins.txt
# docker run -d --name jenkins -p 8080:8080 --volumes-from jenkins-data -v /var/run/docker.sock:/var/run/docker.sock identijenky
