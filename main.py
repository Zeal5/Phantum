import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('?attack'):
        await message.channel.send('https://tenor.com/view/slap-bear-slap-me-you-gif-17942299')

    if message.content.startswith('?pet'):
        await message.channel.send('https://tenor.com/view/cat-frank-the-cat-gif-7392174')

    if message.content.startswith('?like'):
        await message.channel.send('https://tenor.com/view/moti-hearts-gif-20367288')









client.run('OTM0MjE2NDE2NzYzMTk1NDAy.Yes21g.NqEOu429kz4pRLt2yL4Wj_Bhgsg')