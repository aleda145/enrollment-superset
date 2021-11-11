FROM python:3.9.7-slim-buster
RUN apt-get update
RUN apt-get -y upgrade
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y build-essential gcc
RUN pip install apache-superset==1.3.2
RUN pip install psycopg2-binary
ENV FLASK_APP=superset
RUN superset db upgrade
ENV SUPERSET_CONFIG_PATH=/config/superset_config.py
COPY superset_config.py /config/superset_config.py
ARG superset_password
RUN superset fab create-admin \
    --username admin \
    --firstname Admin \
    --lastname Adminsson \
    --email admin@example.com \
    --password $superset_password
RUN superset init
RUN superset set-database-uri -d superset -u postgresql+psycopg2://postgres:a_strong_postgrespassword@superset_db:5432/superset
COPY import_dashboards /dashboards
RUN superset import-dashboards -p /dashboards
CMD superset run -h 0.0.0.0 -p 8088 --with-threads --reload --debugger
