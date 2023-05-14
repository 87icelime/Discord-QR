bot = discord.Client(intents=intents)
slash = app_commands.CommandTree(bot)

@slash.command(name='qrcode', description='Generate a qrcode')
async def makeqrcode(interaction: discord.Interaction, url:str, bg_color:Literal['white','black', 'red', 'blue', 'green']=None, box_color:Literal['white', 'black', 'red', 'blue', 'green']=None, box_size:int=None, border_size:int=None):
    qr_box = box_size or 5 # QR CODE box size
    qr_border = border_size or 2 # QR Code Border Size  
    
    qr = qrcode.QRCode(
            version=2,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=qr_box,
            border=qr_border,
        )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color=f"{box_color or 'black'}", back_color=f"{bg_color or 'white'}")
    uid = uuid.uuid4().hex
    img.save(f"./database/qr/{uid}.png")
    qr_code = f"./database/qr/{uid}.png"
    
    await interaction.response.send_message("Here is your qrcode : ",file=discord.File(qr_code))
