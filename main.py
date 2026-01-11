import telebot
from flask import Flask
from threading import Thread

# سيرفر صغير لضمان بقاء البوت حياً 24 ساعة
app = Flask('')
@app.route('/')
def home(): return "البوت يعمل الآن!"

def run(): app.run(host='0.0.0.0', port=8080)
def keep_alive(): Thread(target=run).start()

# التوكن الخاص بك مضاف جاهزاً
TOKEN = '8210772496:AAGSu7xK3vVnhsmNb_DUA4p2k8HZVOl9CYE' 
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "✅ تم تشغيل البوت بنجاح! أنا الآن أعمل من السيرفر السحابي 24 ساعة.")

    @bot.message_handler(func=lambda message: True)
    def echo_all(message):
        bot.reply_to(message, f"رسالتك وصلت: {message.text}")

        if __name__ == "__main__":
            keep_alive()
                print("البوت انطلق...")
                    bot.polling(none_stop=True)
                    