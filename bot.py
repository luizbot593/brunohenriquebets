import telebot

# 🔥 Token e ID já configurados:
API_TOKEN = '7837896313:AAEADUEtM1SbTPF3GJqJbbZX-VFPWikhWKo'
ID_DONO = 1559415861

bot = telebot.TeleBot(API_TOKEN)

# 📢 Mensagem de boas-vindas
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🚀 Bem-vindo ao Bruno Henrique Bets!\n\n👉 Use /gratis para receber sinais gratuitos.\n👉 Use /premium para saber como acessar o grupo VIP.\n👉 Use /gestao para dicas de gestão de banca.\n\n🤑 Bora bater a meta!")

# 🎯 Comando de sinais grátis
@bot.message_handler(commands=['gratis'])
def sinais_gratis(message):
    bot.reply_to(message, "🔥 Sinais Grátis:\n\n✅ Futebol: +1.5 HT\n✅ Basquete: Handicap -3.5\n\n⚽🏀 Aproveite!")

# 💎 Comando de premium
@bot.message_handler(commands=['premium'])
def premium(message):
    bot.reply_to(message, "💎 Para acessar nosso grupo VIP com sinais exclusivos, entre em contato:\n👉 @seuuser\nOu clique no link: https://t.me/seugrupo\n\n🚀 Bora lucrar juntos!")

# 📊 Comando de gestão
@bot.message_handler(commands=['gestao'])
def gestao(message):
    bot.reply_to(message, "📊 Gestão de Banca:\n\n➡️ Use no máximo 3% por entrada.\n➡️ Nunca faça all-in.\n➡️ Foque no longo prazo.\n\n✅ Disciplina gera resultado!")

# 🛠️ Comando secreto só para o dono enviar sinais personalizados
@bot.message_handler(commands=['enviar'])
def enviar(message):
    if message.from_user.id == ID_DONO:
        texto = message.text.split('/enviar ', 1)
        if len(texto) > 1:
            bot.send_message(message.chat.id, f"🚨 Novo Sinal:\n\n{texto[1]}")
        else:
            bot.reply_to(message, "⚠️ Envie no formato: /enviar SEU TEXTO AQUI")
    else:
        bot.reply_to(message, "❌ Você não tem permissão para usar esse comando.")

# 🚀 Rodando o bot
print('🤖 Bot está funcionando...')
bot.infinity_polling()
