#!/bin/bash

# Variables
URL=$(cat ./keys/url.txt)
TELEGRAM_TOKEN=$(cat ./keys/telegram_token.txt)


echo "Install python3.10-venv if needed: Please write down your sudo password:"
sudo apt install python3.10-venv
python3 -m venv venv
echo "========================================================================"
echo "activate environment:"
source  ./venv/bin/activate

echo "========================================================================"
echo "pip upgrade:"
python3 -m pip install --upgrade pip
echo "========================================================================"
echo "pip install -r requirements.txt"
python3 -m pip install -r requirements.txt

echo "========================================================================"
echo "set Webhook: "

curl --location --request POST "https://api.telegram.org/bot$TELEGRAM_TOKEN/setWebhook?url=$URL" --header "Content-Type: application/json" --data-raw '{"url": "${URL}"}'

flask --app wolframAlfaInlineBot.py run