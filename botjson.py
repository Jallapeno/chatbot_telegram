# -- coding:utf-8 --
import telebot  # biblioteca do bot
import json  # biblioteca de tratamento json
import urllib  # tratamento de url

API_TOKEN = "CHAVE DE API GERADA PRO SEU BOT NO TELEGRAM"  # @botHytalo

bot = telebot.TeleBot(API_TOKEN)  # telebot = sumario de comandos; TeleBot = Comando (aplicando o token)


@bot.message_handler(commands=['cep'])
def send_cep(message):
    msg = bot.reply_to(message, """Digite o cep que deseja consultar:""")
    cid = message.chat.id
    bot.register_next_step_handler(msg, send_cep_step)  # armazenamento da informação digitada


def send_cep_step(message):
    cid = message.chat.id
    mensagem_cep = message.text
    url = "https://viacep.com.br/ws/" + mensagem_cep + "/json/"
    response = urllib.urlopen(url)  # consulta a url inserida

    data = json.loads(response.read())  # carrega os valores do json retornado

    cep = data['cep']
    logradouro = data['logradouro']
    bairro = data['bairro']
    localidade = data['localidade']
    uf = data['uf']
    bot.send_message(cid,
                     ' Cep: ' + cep + '\n Logradouro: ' + logradouro + '\n Bairro: ' + bairro + '\n Localidade: ' + localidade + '\n UF: ' + uf)


bot.polling()
