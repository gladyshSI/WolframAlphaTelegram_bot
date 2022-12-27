# WolframAlphaTelegram_bot
Telegram bot using Wolfram alpha API 

### How to start up
0. Add telegram bot token in /keys/telegram_token.txt
   Add Wolfram AppID in /keys/wolfram_key.txt
   Add Server URL in /keys/url.txt
   
For Ubunta:
1. ```sudo apt-get update```
2. ```sudo apt-get upgrade```
Check that ```ngrok_deploy.sh``` and ```run.sh``` are runable:
3. ```chmod +x ngrok_deploy.sh```
4. ```chmod +x run.sh```
If you want to test it with ngrok:
      Register on the [website](https://dashboard.ngrok.com/get-started/setup)
      Add authtoken in /keys/ngrok_token.txt
      ```./ngrok_deploy.sh```
      Add ngrok url (like https://32515a83.ngrok.io) in /keys/ngrok_token.txt
5. ```./run.sh```
