import openai
import telegram
from telegram.ext import Updater, MessageHandler, Filters

# importing telegram tools from telegram.ext

# Set up the Telegram bot using your API token
bot = telegram.Bot(token='your_telegram_bot
_token')
updater = Updater(token='your_telegram_bot_token', use_context=True)

# Set up the OpenAI API using your API key
openai.api_key = "your_openai_api_key"

def echo(update, context):
    user_text = update.message.text

    # Use the OpenAI API to generate a response based on the user's input
    response = openai.Completion.create(
        engine="davinci",
        prompt=user_text,
        temperature=0.5,
        max_tokens=200,
        n=1,
        stop=None,
        timeout=15,
    )
    bot_response = response.choices[0].text.strip()

    # Send the response back to the user via the Telegram bot
    update.message.reply_text(bot_response)


# Set up a message handler to trigger the `echo` function whenever a new message is received
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# acknowledgment message for polling
print("polling...")
updater.start_polling()
updater.idle()
