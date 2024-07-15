import discord

client = discord.Client()

def get_token():
    token = input("Введите токен бота Discord: ").strip()
    return token

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # Пример ответа на сообщение
    if message.content.lower() == 'привет':
        await message.channel.send('ку братан')

# Получаем токен от пользователя
token = get_token()

# Запускаем бота с полученным токеном
client.run(token)
