import telebot

API_TOKEN = '8081350546:AAGdTpk_MK9PAiQZSAz3bc-rh9jry2DcF4I'
CHANNEL_USERNAME = '@testuser81818'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def check_membership(message):
    user_id = message.from_user.id
    try:
        member = bot.get_chat_member(CHANNEL_USERNAME, user_id)
        if member.status in ['member', 'administrator', 'creator']:
            bot.reply_to(message, "✅ شما عضو کانال هستید. خوش اومدید!")
        else:
            bot.reply_to(message, f"❌ برای ادامه باید عضو کانال بشی:\n👉 {CHANNEL_USERNAME}")
    except Exception as e:
        bot.reply_to(message, f"❌ برای ادامه باید عضو کانال بشی:\n👉 {CHANNEL_USERNAME}")

bot.infinity_polling()
