
import requests

# Replace with your bot's token and chat ID
BOT_TOKEN = ""
CHAT_ID = '6449739887'  # You can find your chat ID by messaging your bot and checking the message updates

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print("Message sent successfully")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")

# Your main application code goes here
# ...

# Send the message when the application finishes
#send_telegram_message("The application has finished running successfully.")
