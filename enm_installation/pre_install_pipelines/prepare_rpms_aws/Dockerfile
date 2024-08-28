FROM debian

RUN apt update \
    && apt install -y createrepo python3-pip wget \
    && pip3 install awscli --upgrade \
    && mkdir -p /mnt/iso /enm_repodata \
    && rm -rf /var/cache/apt/ ~/.cache/pip
