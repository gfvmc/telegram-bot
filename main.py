import telebot
from flask import Flask
from threading import Thread

# سيرفر الإنعاش لضمان العمل 24 ساعة
app = Flask('')
@app.route('/')
def home(): return "Bot is Online!"

def run(): app.run(host='0.0.0.0', port=8080)
def keep_alive(): Thread(target=run).start()

# --- ضع التوكن الخاص بك هنا ---
TOKEN = 'ضـع_تـوكـن_بـوتـك_هـنـا' 
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "✅ تم تشغيل البوت بنجاح وهو يعمل الآن من السيرفر!")

    @bot.message_handler(func=lambda message: True)
    def echo(message):
        bot.reply_to(message, f"وصلت رسالتك: {message.text}")

        if __name__ == "__main__":
            keep_alive()
                print("البوت انطلق...")
                    bot.polling(none_stop=True)
                    