from ubuntu

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

WORKDIR /CatalogueContainer

COPY . /CatalogueContainer

RUN pip --no-cache-dir install -r requirements.txt

EXPOSE 5002

ENV FLASK_APP=script
ENV FLASK_DEBUG=True
ENV FLASK_RUN_PORT=5002

CMD [ "flask", "run", "--host", "0.0.0.0" ]
