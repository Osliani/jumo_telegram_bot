from dotenv import load_dotenv
import telebot, utils, os

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TELEGRAM_TOKEN)


@bot.message_handler(commands=["start", "help"])
def cmd_start(message):
    print("/start")
    data = {
        "id": message.chat.id, 
        "message": "Hola, en qué me puedes ayudar?"
    }
    utils.send_message(data)
    
    
@bot.message_handler(commands=["contact"])
def cmd_start(message):
    print("/contact")
    data = {
        "id": message.chat.id, 
        "message": "Envíame los enlaces de los sitios web de su empresa para visitarlos."
    }
    utils.send_message(data)
    
    
@bot.message_handler(commands=["lead"])
def cmd_start(message):
    print("/lead")
    data = {
        "id": message.chat.id, 
        "message": "Consulta el presupuesto con el que cuenta la empresa para iniciar negociaciones con el cliente."
    }
    utils.send_message(data)
    
    
@bot.message_handler(content_types=['text'])
def reply_text(message):
    print(f"-User: {message.text}")
    data = {
        "id": message.chat.id, 
        "message": message.text
    }
    utils.send_message(data)


if __name__ == "__main__":
    print("BOT LISTO!")
    bot.infinity_polling()