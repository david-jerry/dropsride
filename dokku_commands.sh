#!/bin/bash

# Running dokku commands for django manage.py

python manage.py makemigrations && python manage.py migrate && python manage.py update_countries_plus && python manage.py get_currency_exchange && python manage.py get_ng_banks

# Processes has ended
