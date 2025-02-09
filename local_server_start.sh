#!/bin/bash

#PROJECT_DIR=$(pwd)
#myenv_path = "$PROJECT_DIR/myenv/bin/activate

#activate the virtual environment
source myenv/bin/activate

# start the gunicorn server here & start the gunicorn in the background
gunicorn -b 127.0.0.1:8000 app:app &

# start the nginx server
sudo systemctl start nginx

echo "nginx and gunicorn servers are started"



# note: here we can more steps to check whether gunicorn and nginx are configured properly or not
