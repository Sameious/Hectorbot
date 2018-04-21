import mod
bot = commands.Bot(command_prefix='!h', description='your description')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)

mod.message_cmd(bot)


bot.run('NDEzOTMxNDc4ODM4MTQ5MTIx.DWgA3A.9bHhJV_5pzm0ElvOXxfoC_pAT4Q')
