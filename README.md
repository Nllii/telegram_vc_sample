# Telethon streaming.

#### This project is meant to be used with [Telegram-Paperplane](https://github.com/RaphielGang/Telegram-Paperplane)


#### This project uses the @dev branch of [using pytgcalls](https://pytgcalls.github.io)

#### Hosting, use your phone and install  code-server... you can use a cloud notebooks such as kaggle or google colab.


1. !git clone https://github.com/Nllii/telegram_vc_sample.git
2. !curl -fsSL https://code-server.dev/install.sh | sh
3. !code-server --link

```python

cd into telegram_vc_sample 

python -m telegram_voice

```


######  auth keys is a json format: 

```json

{
    "API_KEY": "",
    "API_HASH": "",
    "CHAT_ID":"",
    "STRING_SESSION":"",
    "PHONE":"",
    "CLOUD_MODE":"",
    "BOT_TOKEN":""

}




```
<!-- TODO

- Create a branch to work on youtube inline bot

- Add firebase storage script

- Add kaggle and google colab script to the dev_install script for cloud_mode

 -->
