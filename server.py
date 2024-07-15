import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    print('------')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Respond with "hi" to any message
    if message.content:
        await message.channel.send('hi')

# Replace 'your_bot_token' with your actual bot token
client.run('your_bot_token')
