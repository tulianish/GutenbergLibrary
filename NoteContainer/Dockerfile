from ubuntu

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

WORKDIR /NoteContainer

COPY . /NoteContainer

RUN pip --no-cache-dir install -r requirements.txt

EXPOSE 5003

ENV FLASK_APP=script
ENV FLASK_DEBUG=True
ENV FLASK_RUN_PORT=5003

CMD [ "flask", "run", "--host", "0.0.0.0" ]
