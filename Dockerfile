FROM fedora:23

COPY . /usr/local/bin/

WORKDIR /usr/local/bin/

RUN mkdir -p /usr/local/bin && \
    dnf install -y wget tar vim openssl-devel gcc python-devel redhat-rpm-config libffi-devel && \
    pip install -U pip && \
    pip install -r requirements.txt

CMD ["aws-cf-warm"]
