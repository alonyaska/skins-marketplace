#!/bin/bash

# Если первый аргумент "celery"
if [ "${1}" == "celery" ]; then
  celery --app=app.tasks.celerys:celery worker -l INFO

# Если первый аргумент "flower"
elif [ "${1}" == "flower" ]; then
  celery --app=app.tasks.celerys:celery flower

fi