#!/bin/bash


# touch ./instance/logger.sqlite
python3 -m flask --app logger init-db
python3 -m flask --app logger run --host=0.0.0.0 --port=1337 --debug

#python3 ./logger/logging_client.py