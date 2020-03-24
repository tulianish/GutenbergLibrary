from ubuntu

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

WORKDIR /ServiceContainer

COPY . /ServiceContainer

RUN pip --no-cache-dir install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=script
ENV FLASK_DEBUG=True
CMD [ "flask", "run", "--host", "0.0.0.0" ]
