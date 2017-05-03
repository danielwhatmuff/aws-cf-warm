FROM fedora:23

RUN mkdir -p /usr/local/bin && \
    dnf install -y wget tar vim openssl-devel gcc python-devel redhat-rpm-config libffi-devel && \
    pip install -U pip

ADD requirements.txt .

RUN pip install -r requirements.txt

COPY . /usr/local/bin/

WORKDIR /usr/local/bin/

CMD ["aws-cf-warm"]
