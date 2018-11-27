FROM debian:latest
WORKDIR /opt/locust
RUN apt update && apt install -y python-pip
RUN pip install --no-cache-dir locust
RUN pip install --no-cache-dir bzt
ADD . /opt/locust
RUN touch /.bzt-rc && chmod 644 /.bzt-rc 
EXPOSE 8089 5557 5558