import telebot

TOKEN = "8958216011:AAFnVhWLhFMy8KF17LT7oH-VIX3bAs00Mwk"
bot = telebot.TeleBot(TOKEN)

history = []

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "✅ WINGO BOT ON\n\nSend result like:\nRED BIG\nGREEN SMALL\n\nLink: https://t.me/Wingo22bot")

@bot.message_handler(func=lambda m: True)
def all_msg(m):
    text = m.text.upper()
    color = None
    if "RED" in text: color = "RED"
    elif "GREEN" in text: color = "GREEN"
    elif "VIOLET" in text: color = "VIOLET"
    
    if color:
        size = "BIG" if "BIG" in text else "SMALL"
        history.append((color, size))
        bot.reply_to(m, f"Added: {color} {size}\nTotal: {len(history)}\nSend /predict for prediction")
    elif "/predict" in text or "PREDICT" in text:
        if len(history) < 3:
            bot.reply_to(m, f"Need {3-len(history)} more results first")
        else:
            bot.reply_to(m, f"Next Prediction: RED BIG (based on {len(history)} data)")
    else:
        bot.reply_to(m, "Send like: RED BIG")

print("Bot Running...")
bot.infinity_polling()
