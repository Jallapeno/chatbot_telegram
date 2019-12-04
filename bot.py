# -- coding:utf-8 --
import telebot # import da biblioteca do pyTelegramBotpi

API_TOKEN="SUA CHAVE DE API DO BOT GERADO NO TELEGRAM" 

bot = telebot.TeleBot(API_TOKEN) #telebot = sumario de comandos; TeleBot = Comando (aplicando o token)

#Inicio

@bot.message_handler(commands =["start"]) #comando de /start no Telegram
def send_welcome(message):
	cid = message.chat.id # id da conversa
	msg = bot.reply_to(message,"Olá Mundo, bot criado. \n ID: " + str(cid)) #envio de mensagem para o usuário
	bot.send_message(cid, "Caso precise de ajuda => /ajuda")

#ajuda

@bot.message_handler(commands =["ajuda"]) #função /ajuda digitada pelo usuário
def send_more(message):
	cid = message.chat.id # id da conversa
	msg_more = bot.reply_to(message, "Esqueceu das funções?\n Opção 1: /cadastro \n Opção 2: /categorias \n Opção 3: /contato")
	bot.send_message(cid, "Caso ainda encontre dificuldades, entre em contato\n pelo E-mail: jallapeno@email.com")

bot.polling() # função responsável por sempre responder o usuário
