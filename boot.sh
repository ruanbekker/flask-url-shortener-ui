#!/bin/sh
gunicorn -w 2 -b 0.0.0.0:8080 --access-logfile=/dev/stdout --error-log=/dev/stderr app:app
