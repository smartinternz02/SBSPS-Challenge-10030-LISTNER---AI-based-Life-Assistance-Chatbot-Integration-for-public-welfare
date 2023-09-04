# SBSPS-Challenge-10030-LISTNER---AI-based-Life-Assistance-Chatbot-Integration-for-public-welfare
LISTNER - AI-based Life Assistance Chatbot Integration for public welfare

#LISTNER - AI-Based Life Assistance Chatbot Integration For Public Welfare

## About

This is a Telegram bot that utilizes the OpenAI API to generate responses based on user input.

The bot is built using Python and the python-telegram-bot library for interacting with the Telegram Bot API. It integrates with the OpenAI API to generate responses using the OpenAI GPT-3 model.

## Prerequisites

*   Python 3 installed
*   Telegram Bot API token
*   OpenAI API key
*   Dependencies: python-telegram-bot, openai

## Installation

1.  Clone the repository: `git clone https://github.com/your-username/telegram-openai-bot.git`
2.  Navigate to the project directory: `cd telegram-openai-bot`
3.  Install the necessary dependencies: `pip install python-telegram-bot openai`

## Configuration

1.  Create a new Telegram bot by chatting with the BotFather on Telegram.
2.  Obtain the API token for your Telegram bot.
3.  Replace `'YOUR_TELEGRAM_TOKEN'` with your actual Telegram bot token in the `bot = telegram.Bot(token='YOUR_TELEGRAM_TOKEN')` line of the code.
4.  Obtain an OpenAI API key from the OpenAI website.
5.  Replace `'YOUR_OPENAI_API_KEY'` with your actual OpenAI API key in the `openai.api_key = 'YOUR_OPENAI_API_KEY'` line of the code.

## Usage

1.  Run the Python script: `python bot.py`
2.  Add your Telegram bot to a group or start a private chat with it.
3.  Send messages to the bot and it will respond with generated text based on the OpenAI API.

## Customization

*   You can modify the command handler functions (`start()`, `echo()`) and add more functionality to suit your needs.
*   You can experiment with different OpenAI models and parameters by modifying the `generate_response()` function.

