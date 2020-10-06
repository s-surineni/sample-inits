FROM jenkins:latest
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
USER jenkins
