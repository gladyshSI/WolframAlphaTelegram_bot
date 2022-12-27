# WolframAlphaTelegram_bot
Telegram bot using Wolfram alpha API 
## About
You can find this bot [here](https://t.me/WFAlfa_bot).
This Telegram Bot accepts your request and sends a short text response and pictures with the results provided by the Wolpram API.  
Telegram bot can also work in inline mode, but in this case it sends only a short text response.  
## Usage Examples
![Alt text](static/images/1.jpg?raw=true "Private messages")
![Alt text](static/images/3.jpg?raw=true "Inline mod")
## How to start up
0. Add telegram bot token in /keys/telegram_token.txt  
   Add Wolfram AppID in /keys/wolfram_key.txt  
   Add Server URL in /keys/url.txt  
   
Tested on Ubuntu:
1. ```sudo apt-get update```
3. ```sudo apt-get upgrade```  
Check that ```ngrok_deploy.sh``` and ```run.sh``` are runnable:
3. ```chmod +x ngrok_deploy.sh```
4. ```chmod +x run.sh```  
> If you want to test it with ngrok:  
>     Register on the [website](https://dashboard.ngrok.com/get-started/setup)  
>     Add authtoken in /keys/ngrok_token.txt  
>     ```./ngrok_deploy.sh```  
>     Add ngrok url (like https://32515a83.ngrok.io) in /keys/ngrok_token.txt  
5. ```./run.sh```
