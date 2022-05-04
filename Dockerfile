FROM python:2
RUN /usr/local/bin/python -m pip --disable-pip-version-check install --upgrade pip django==1.6.11

ADD . /src
RUN pip --disable-pip-version-check install /src

WORKDIR /app
RUN django-admin.py startproject demo .
COPY ./docker/*.py /app/demo/

CMD python manage.py runserver 0.0.0.0:8000 --noreload
EXPOSE 8000
VOLUME ["/app/demo/db"]
