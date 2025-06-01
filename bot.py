import telebot
import os

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

# Lista de usuários premium
premium_users = []

# Mensagem de boas-vindas
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🤖 Bem-vindo ao Bruno Henrique Bets!\nReceba sinais de Futebol e Basquete!\n\nMenu:\n/sinal - Receber sinal grátis\n/premium - Assinar Premium\n/gestao - Dicas de Gestão\n/suporte - Falar com o suporte")

# Comando de sinal grátis
@bot.message_handler(commands=['sinal'])
def send_signal(message):
    bot.reply_to(message, "⚽ SINAL GRÁTIS ⚽\nJogo: Time A x Time B\nMercado: Over 1.5 gols\nOdd: 1.80\nHorário: 20h00")

# Comando de gestão
@bot.message_handler(commands=['gestao'])
def send_gestao(message):
    bot.reply_to(message, "💰 Gestão de Banca 💰\nRecomendamos usar 1-2% da sua banca por entrada.\nDisciplina é a chave do sucesso!")

# Comando premium
@bot.message_handler(commands=['premium'])
def send_premium(message):
    bot.reply_to(message, "🚀 Quer receber sinais ilimitados?\nFale com nosso suporte:\n@SeuUserDoSuporte\n\nApós pagamento, enviaremos seu acesso.")

# Comando suporte
@bot.message_handler(commands=['suporte'])
def send_suporte(message):
    bot.reply_to(message, "📞 Suporte:\nFale conosco no Telegram: @SeuUserDoSuporte")

# Comando para liberar usuário premium (manual)
@bot.message_handler(commands=['liberar'])
def liberar_usuario(message):
    if str(message.from_user.id) == "SEU_ID":  # Seu ID de admin aqui
        try:
            username = message.text.split()[1]
            premium_users.append(username)
            bot.reply_to(message, f"✅ {username} agora é usuário PREMIUM!")
        except:
            bot.reply_to(message, "❌ Use o comando corretamente: /liberar @usuario")
    else:
        bot.reply_to(message, "❌ Você não tem permissão para usar esse comando.")

# Rodar o bot
bot.polling()
