FROM python:3.8.6

WORKDIR /root/song

COPY . /root/song

RUN pip install --upgrade pip && \
    pip install --ignore-installed -r /root/song/requirements.txt


ENTRYPOINT [ "python" ]

CMD ["main.py" ]