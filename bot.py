import discord, qrcode, uuid, os
from dotenv import load_dotenv
from server import server 

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="I am not a Cool Bot"))
    print(f'Bot {client.user} on air!')


@client.event
async def on_message(message):
    if message.author != client.user:
       if message.content.startswith("?qr"):
        qrfind = message.content.split("?qr ", 1)[1]
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=20,
            border=1,
         )

        qr.add_data(qrfind)
        qr.make(fit=True)

        duid = uuid.uuid1()

        img = qr.make_image(fill_color="#ffeb34", back_color="#171718")
        img.save(f"./qrtest/{duid.hex}.png")
        userinfo = message.author.name + "#" + message.author.discriminator
        userid = message.author.id
        print(f"{userinfo} ({userid}) - created qr - {qrfind}") 
        await message.channel.send(file=discord.File(f"./qrtest/{duid.hex}.png"))

server()       
client.run(os.getenv('bottoken'))


