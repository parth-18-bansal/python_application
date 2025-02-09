#!/bin/bash

# stop the gunicorn server
gunicorn_pid=$(pgrep -f gunicorn | head -n 1)
if [[ -n "$gunicorn_pid" ]]
then
    sudo kill "$gunicorn_pid"
fi

# stop the nginx server
sudo systemctl stop nginx