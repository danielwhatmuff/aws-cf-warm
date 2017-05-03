FROM fedora:23

ADD requirements.txt .

RUN mkdir -p /usr/local/bin && \
    dnf install -y wget openssl-devel gcc python-devel redhat-rpm-config libffi-devel && \
    pip install -U pip && \
    pip install -r requirements.txt && \
    dnf remove -y  openssl-devel vim redhat-rpm-config libffi-devel gcc && \
    dnf clean all

COPY . /usr/local/bin/

WORKDIR /usr/local/bin/

CMD ["aws-cf-warm"]
