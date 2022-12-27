#!/bin/bash

# If you will use ngrok (ONLY FOR DEBUG!)

# VARS:
TOKEN=$(cat ./keys/ngrok_token.txt)
PORT=5000


sudo tar xvzf ngrok-v3-stable-linux-amd64.tgz -C /usr/local/bin
ngrok config add-authtoken $TOKEN
ngrok http $PORT