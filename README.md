# Telegram Youtube Downloader Bot

A simple Telegram bot that allows users to download YouTube videos by sending a YouTube link. Built with telebot for Telegram API integration and pytube for video downloading.

# Explanation

There are multiple libraries used to make Telegram bots in Python but this bot uses the telebot library which is the esiest way to make a Telegram bot.

## Installation

1. Clone the repository:
git clone https://github.com/Abtin0/telegram-yt-downloader-bot.git


2. Install the required dependencies:
pip install -r requirements.txt


## Usage

1. Create a Telegram bot using the BotFather and obtain the bot token.


2. Replace TELEGRAM_BOT_TOKEN with your bot's token


3. Run the bot:
python yt_download_bot.py


4. Start chatting with the bot in Telegram!

## Commands

- `/start`: Starts the bot and sends a welcome message.
- `/help`: Sends information about the bot's functionality.
- `/yt_download`: Downloads the YouTube video specified by the URL and sends it as a file.
