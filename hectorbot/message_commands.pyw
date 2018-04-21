import stand_gen
from stand_gen import random_stand
ban_list_file = open('banlist.txt', 'r')
ban_list = ban_list_file.readline()
banned_user_list = ban_list.split(',')

def is_user_banned(user):
    if banned_user_list.count(user.id) == 0:
        return False
    else:
        return True
def message_cmd(bot):
    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
        if is_user_banned(message.author) == True:
            return
        if message.content == 'hector':
            await bot.send_message(message.channel, 'Oho! Did somebody call?')
        if message.content == "!hr":
            await bot.send_message(message.channel, "See ya!")
            await bot.logout()
        if message.content == "!hstand":
            await bot.send_message(message.channel, random_stand())
        if message.content == "!hstandname":
            await bot.send_message(message.channel, stand_name())
        if message.content.startswith('!hblockuser'):
            banned_user = message.mentions[0]
            with open('banlist.txt', 'a') as myfile:
                myfile.write('')
                myfile.write(banned_user.id)
                myfile.write(',')
            await bot.send_message(message.channel, '%a added to banlist' % banned_user.name)
        if message.content.startswith('!hstandadd'):
            target = message.content.split(' ', 1)
            name = target[1]
            if stand_gen.stand_exist == False:
                await bot.send_message(message.channel, "%a added to standlist" % name)
            else:
                await bot.send_message(message.channel, "%a is already in standlist!" % name)
        if message.content.startswith('!hstandremove'):
            target = message.content.split(' ', 1)
            name = target[1]
            stand_gen.remove_stand(name)
            if stand_gen.stand_exist(name) == False:
                await bot.send_message(message.channel, "Name doesn't exist!")
            else:
                await bot.send_message(message.channel, "Removing {0} from stand names list.".format(name))


