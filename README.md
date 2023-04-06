# QR Generator Discord bot
a python discord bot generates QR code for any kind of URLs 
Want to donate me? <br> Ethereum Wallet : 
> 0x76bD98E5E44ECc9114684f90ad3812Db2E71e744
## Begineer GUIDE 
* Add your bot token after ``bottoken=`` in ``.env`` file. 
* If you want to use a different storage to store the data, must change the store location to ``img.save(f"./Your_Folder/Your_Folder/{duid.hex}.png")``. Otherwise you may face some errors. 
* If you do not want to make a server page for you, delete ``server.py`` file and ``server()`` from ``bot.py`` 
* Do not delete the ``qrtest`` folder, Its really necessary to run the bot and store qr images in that folder. Meantime if you are running out of host then you can delete the images stored inside the folder.
* If you are running error while trying to run the bot, make sure you've downloaded every packages(discord, qrcode, uuid, os, dotenv)


## Sample 
### Discord Channel Input 
> ?qr [URL] \
> example : ?qr https://github.com/87icelime
### Discord User Interface 
![ Discord outpout](qrbot_example.PNG)


### Console Output 
![ Console Output](console_example.png)

You can always check your console to find if someone is generating a malware or scam website using your BOT. 
> Note : Must tell your users that you are storing the QR code and link before they start using your BOT. Keep everyone's privacy secret from other users.

### [Project LICENSE](LICENSE)

> Feel free to open an issue if you face any issue. 

