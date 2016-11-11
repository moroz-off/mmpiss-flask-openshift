FROM python:3.3
MAINTAINER Denis Morozov "morozoff.py@gmail.com"

EXPOSE 80
EXPOSE 443
EXPOSE 8051

ADD ./requirements.txt /tmp
RUN pip3 install -r tmp/requirements.txt

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ENTRYPOINT ["python3"]
CMD ["index.py"]
