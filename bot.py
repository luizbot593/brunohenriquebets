import telebot
from flask import Flask
from threading import Thread

# 🔥 Dados sensíveis (pegos nas variáveis de ambiente da Render)
import os
TOKEN = os.getenv('TOKEN')
ID_GRUPO = os.getenv('ID_GRUPO')

bot = telebot.TeleBot(TOKEN)

# ✅ FLASK - Mantém o bot online
app = Flask('')

@app.route('/')
def home():
    return "✅ Bot está online e funcionando!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# 🔥 Comandos do bot

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 Seja bem-vindo ao Bruno Henrique Bets! Use /menu para ver as opções.")

@bot.message_handler(commands=['menu'])
def menu(message):
    texto = """
🏟️ *Menu Principal - Bruno Henrique Bets* 🏟️

🎯 /sinaisgratis - Receber sinais gratuitos
💰 /planos - Ver planos premium
📊 /gestao - Dicas de gestão de banca
🤖 /suporte - Falar com o suporte
"""
    bot.send_message(message.chat.id, texto, parse_mode="Markdown")

@bot.message_handler(commands=['sinaisgratis'])
def sinaisgratis(message):
    bot.reply_to(message, "🚀 Aguardando... Aqui você vai receber seus sinais gratuitos assim que estiverem disponíveis!")

@bot.message_handler(commands=['planos'])
def planos(message):
    texto = """
💎 *Planos Premium Bruno Henrique Bets* 💎

- 🔥 *Mensal:* R$ XX
- 🚀 *Trimestral:* R$ XX
- 🏆 *Vitalício:* R$ XX

Acesse nosso Instagram ou fale no /suporte para contratar!
"""
    bot.send_message(message.chat.id, texto, parse_mode="Markdown")

@bot.message_handler(commands=['gestao'])
def gestao(message):
    texto = """
📊 *Gestão de Banca Recomendada* 📊

- ✅ Use 1% a 3% da sua banca por entrada.
- ⚠️ Nunca recupere perdas no impulso.
- 🧠 Foque no longo prazo.
"""
    bot.send_message(message.chat.id, texto, parse_mode="Markdown")

@bot.message_handler(commands=['suporte'])
def suporte(message):
    bot.reply_to(message, "🆘 Fale conosco no Instagram: @seuinsta ou aqui mesmo no Telegram!")

# ✅ Iniciar Bot + Flask
keep_alive()
print('🤖 BOT ONLINE...')
bot.infinity_polling()
