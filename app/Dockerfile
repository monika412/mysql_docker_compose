FROM alpine:3.7

RUN mkdir /Mysql_Api

RUN apk update \
  && apk add --no-cache python3 \
  && apk add libc-dev \
  && apk --no-cache --update-cache add gcc gfortran build-base python3-dev wget freetype-dev libpng-dev openblas-dev \	
  && apk add --no-cache subversion \
  && apk add curl bash binutils tar git \
  && python3 -m ensurepip \
  && git clone https://github.com/monika412/Mysql_Api /Mysql_Api \
  && pip3 install -r /Mysql_Api/requirements.txt 	



CMD cd /Mysql_Api && git pull && python3 /Mysql_Api/mysql_api1.py

