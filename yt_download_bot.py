import telebot
from pytube import YouTube
import os

bot = telebot.TeleBot("TELEGRAM_BOT_TOKEN", parse_mode=None)

# Variable to keep track of the state
awaiting_link = False


# Command handler for /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    """
    Handles the '/start' command and sends a welcome message to the user.

    Parameters:
        message (telebot.types.Message): The incoming message containing the '/start' command.

    Returns:
        None

    This function is registered as a message handler for the bot using the `bot.message_handler` decorator.
    It replies to the incoming message with a welcome message and information about the bot's functionality.
    """
    bot.reply_to(message, "Welcome to the Telegram Youtube Downloader bot. Send /help for more information.")


# Command handler for /help
@bot.message_handler(commands=['help'])
def send_help(message):
    """
    Handles the '/help' command and sends a message to the user with information about the bot's functionality.

    Parameters:
        message (telebot.types.Message): The incoming message containing the '/help' command.

    Returns:
        None

    This function is registered as a message handler for the bot using the `bot.message_handler` decorator.
    It replies to the incoming message with a message containing information about the bot's functionality.
    """
    bot.reply_to(message, "This is a Youtube Downloader bot! To download a YouTube video, send /yt_download.")


# Command handler for /yt_download
@bot.message_handler(commands=['yt_download'])
def request_video_link(message):
    """
    Handles the '/yt_download' command and requests the user to send a YouTube video link.

    Parameters:
        message (telebot.types.Message): The incoming message containing the '/yt_download' command.

    Returns:
        None

    This function is registered as a message handler for the bot using the `bot.message_handler` decorator.
    It sets the `awaiting_link` global variable to True to indicate that the bot is awaiting a YouTube video link.
    It sends a message to the chat asking the user to send the YouTube video link they want to download.
    """
    global awaiting_link
    awaiting_link = True
    bot.send_message(message.chat.id, "Please send the YouTube video link you want to download.")


# Message handler for text messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    """
    Handle incoming messages and perform actions based on the message content.

    Parameters:
        message (telebot.types.Message): The incoming message.

    Returns:
        None

    This function is registered as a message handler for the bot using the `bot.message_handler` decorator.
    It checks if the bot is currently awaiting a YouTube video link by checking the value of the `awaiting_link` global variable.
    If `awaiting_link` is True, it tries to download the highest resolution video from the provided YouTube link.
    The video is downloaded to the local directory using the `YouTube.streams.get_highest_resolution().download()` method.
    The downloaded video file is then sent as a video message to the chat using the `bot.send_video` method.
    After sending the video, the video file is removed from the local directory using the `os.remove` method.
    If an error occurs during the download or sending process, an error message is sent to the chat using the `bot.send_message` method.
    If `awaiting_link` is False and the message is a text message, the function replies to the message with the original message text using the `bot.reply_to` method.
    """
    global awaiting_link
    if awaiting_link:
        try:
            yt = YouTube(message.text)
            highest_quality_stream = yt.streams.get_highest_resolution()
            bot.send_message(message.chat.id, f"Downloading video: {yt.title}")
            video_path = highest_quality_stream.download()  # Downloads the video to the local directory
            with open(video_path, 'rb') as video:
                bot.send_video(message.chat.id, video)
            os.remove(video_path)  # Remove the video file after sending
            awaiting_link = False  # Reset the state
        except Exception as e:
            bot.send_message(message.chat.id, f"An error occurred: {e}")
            awaiting_link = False  # Reset the state
    else:
        bot.reply_to(message, message.text)


# Start the bot
if __name__ == '__main__':
    print("Listening ...")
    bot.infinity_polling()
