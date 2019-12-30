import discord
import functions
import classes

TOKEN = ''

client = discord.Client()

@client.event
async def on_message(message):
    # prevent bot from talking to itself
    if message.author == client.user:
        return

    # commands
    # TODO: make commands based on DB

    # skips comparisons if message is not command
    if message.content.lower().startswith('!noticebot'.lower()):


        # output commands list
        if message.content.lower() == '!noticebot'.lower():
            msg = 'these are my commands: !noticeBot, !noticeBot sub, !noticeBot unsub, !noticeBot clearDB, !noticeBot announce'.format(message)
            await client.send_message(message.channel, msg)

        # clears database
        elif message.content.lower() == '!noticeBot clearDB'.lower():

            # TODO: make user id compare to list of authorized user ids
            if message.author.id == '174602020672503808':
                functions.clearStorage()
                msg = 'authorized user {0.author.mention}, clearing database'.format(message)
            else:
                msg = 'unauthorized user {0.author.mention}'.format(message)
            await client.send_message(message.channel, msg)

        # subscribes user to follow channel which message was sent in
        elif message.content.lower() == '!noticeBot sub'.lower():
            user1 = classes.User(message.author.name, message.author.id, [message.channel.id], message.author)

            if functions.userInList(user1, message.channel.id):
                msg = ('user {0.author.mention} already subbed to channel "' + message.channel.name + '"').format(message)
            else:
                msg = ('adding user {0.author.mention} to sublist for channel "' + message.channel.name +'"').format(message)
                functions.addUser(user1, message.channel.id)

            await client.send_message(message.channel, msg)

        elif message.content.lower() == '!noticeBot unsub'.lower():
            user1 = classes.User(message.author.name, message.author.id, [message.channel.id], message.author)

            if functions.userInList(user1, message.channel.id):
                msg = ('unsubbing user {0.author.mention} from sublist for channel "' + message.channel.name +'"').format(message)
                functions.removeUser(user1, message.channel.id)

            else:
                msg = ('User {0.author.mention} not in sublist for channel "' + message.channel.name +'"').format(message)

            await client.send_message(message.channel, msg)

        elif message.content.lower() == '!noticeBot announce'.lower():

            if message.author.id == '174602020672503808':
                msg = 'authorized user {0.author.mention}, announcing message'.format(message)
                await client.send_message(message.channel, msg)

                msg = 'enter channel ID'.format(message)
                await client.send_message(message.channel, msg)

                msg = await client.wait_for_message(author=message.author, channel=message.channel)
                channelID = msg.content

                msg = 'enter message'.format(message)
                await client.send_message(message.channel, msg)

                msg = await client.wait_for_message(author=message.author, channel=message.channel)
                announceMSG = msg.content

                msg = ('Sending message to channel with ID ' + channelID).format(message)
                await client.send_message(message.channel, msg)

                await client.send_message(client.get_channel(channelID), announceMSG)


            else:
                msg = 'unauthorized user {0.author.mention}'.format(message)
                await client.send_message(message.channel, msg)





    # sends messages to subscribed users
    for someUser in functions.getUsers():
        if (message.channel.id in someUser.subbedChannels and message.author.name != someUser.name):

            msg = message.author.name + " har skickat ett meddelande i servern " + message.server.name + " i kanalen " + message.channel.name.format(message)

            await client.send_message(someUser.userClassObject, msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)



# functions.addUser(user1)
list = functions.getUsers()

if (list != []):
    print("dessa är användarna")
    for user in list:
        print(user.name)
    else:
        print("no users after")
