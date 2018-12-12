import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Welcome to the Chart Bot')
    print('Sent message to ' + member.name)
async def on_ready():
    print("I am On")
    await client.change_presence (game=discord.Game(name="With your Charts"))
    
    


@client.event
async def on_message(message):
    if message.content.startswith('hello'):
        msg = "Yo How are you".format(message)
        await client.send_message(message.channel, msg)
    if message.content == '!chart VAAH':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1bXG0jUNIWY44ITrlGy5_8K9RtpvLQw20/view?usp=sharing')
    if message.content == '!chart VAAU':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1_xOs6LI9nUrwWEm_7yphgechRwBxj-fR/view?usp=sharing')
    if message.content == '!chart VABO':
        await client.send_message(message.channel,'https://drive.google.com/file/d/17M45MInthI3quY8o61LhG7Ozd8lskWXJ/view?usp=sharing')
    if message.content == '!chart VABB':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1CGyPyH7-Blk-6kJNDeMg0HTxS_xjHMQp/view?usp=sharing')
    if message.content == '!chart VABP':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1CciHPfkCbranffGlQEVwOkYEkVA0n-QA/view?usp=sharing')
    if message.content == '!chart VABV':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1MDTJtGy8g5Lsl3rk-32VipQwhUX6woyv/view?usp=sharing')
    if message.content == '!chart VAGD':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1Tbyh3NymdJ1IA6iFFud6geboYerc2yHs/view?usp=sharing')
    if message.content == '!chart VAID':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1u0Dysaa4ZJCtM_h4OBo9g0z98Xdr3AM9/view?usp=sharing')
    if message.content == '!chart VAUD':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1n3Py8sa8eYhLr2kh928ZEzDioIr0HcYw/view?usp=sharing')
    if message.content == '!chart VASU':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1BTYDu2UZmQBb78t5Ogz9TUo1ljcuyCr3/view?usp=sharing')
    if message.content == '!chart VAPR':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1ECOBVlVLzmVUPXLIOuX-vBOw07J4oOXs/view?usp=sharing')
    if message.content == '!chart VANP':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1qtkDSqHx4WWpfFNz-OU6hfQiFW7YboHd/view?usp=sharing')
    if message.content == '!chart VAKP':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1DJ0sm0c4ooFU23Ub6K3avL8FYnfO757T/view?usp=sharing')
    if message.content == '!chart VAJL':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1M_G7kRx4Mv5siaotsq_BIMFboi-orBdz/view?usp=sharing')
    if message.content == '!chart VAJB':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1rhcEfNJASmXV2z9NPpDnRH8KwRnThhpB/view?usp=sharing')
    if message.content == '!chart VERP':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1N96MDw-fcBJS7UTQR7U8iVw7a-WrhlEY/view?usp=sharing')
    if message.content == '!chart VERC':
        await client.send_message(message.channel,'https://drive.google.com/file/d/16ii_QNjL8R50znqwORCbYoxQdYYqWiga/view?usp=sharing')
    if message.content == '!chart VEPT':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1P8gjFPpcUehjofcCEmWsgOF1HLd1W51E/view?usp=sharing')
    if message.content == '!chart VEMR':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1wfrhFLcsfQ-PcbAkQQemMkTVTh5-_FBA/view?usp=sharing')
    if message.content == '!chart VEMN':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1Ow0Iil9MqvY2mUbggRd6oQf0G6oJC1ef/view?usp=sharing')
    if message.content == '!chart VELR':
        await client.send_message(message.channel,'https://drive.google.com/file/d/11_xqFK1uGtdsB3y-XT_1t9UEACpQaDtR/view?usp=sharing')
    if message.content == '!chart VELP':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1Im0GThlMZWQVquW3qV9H4ZrxSX47hyXd/view?usp=sharing')
    if message.content == '!chart VEKO':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1OjY6XoR2I1iNQprzb3tKKclhRHo3FCyy/view?usp=sharing')
    if message.content == '!chart VEJS':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1obiIAkRT8dOJEL1T_Ouxi4GayHULIL5x/view?usp=sharing')
    if message.content == '!chart VEIM':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1HVo0sTFx6oH2a92s6sJIL65nUouB9RrG/view?usp=sharing')
    if message.content == '!chart VEGY':
        await client.send_message(message.channel,'https://drive.google.com/file/d/17XL3_GwypDZvBHWhOXxPGP6d555nZ4cc/view?usp=sharing')
    if message.content == '!chart VEGT':
        await client.send_message(message.channel,'https://drive.google.com/file/d/16LlYxpAt-YMU77GjEb9gaCD8AcN0-ehT/view?usp=sharing')
    if message.content == '!chart VEDG':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1-eTvOLUJLRVrVmof2DnttZI9jWsv2bxE/view?usp=sharing')
    if message.content == '!chart VECC':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1FDzXwQkVvA_8Dk5-XrYDP79ANwMML4Or/view?usp=sharing')
    if message.content == '!chart VEBS':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1xGiJjgjFqaW_qWdjHyGe2p_7Yt7BFGah/view?usp=sharing')
    if message.content == '!chart VEBN':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1loajwHcTPlMZb9Y2Flti5xLtODHCAENH/view?usp=sharing')
    if message.content == '!chart VEBD':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1Gl9C5vHtTYSKcg100GznCqsz0SWheqj4/view?usp=sharing')
    if message.content == '!chart VEAT':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1BvSvFcH_8aUa8EvJ3FyGQm4967jEIj4a/view?usp=sharing')
    if message.content == '!chart VIPT':
        await client.send_message(message.channel,'https://drive.google.com/file/d/10aUCgT4Pmecm97MpCjcehKK5-7o767TP/view?usp=sharing')
    if message.content == '!chart VILK':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1TrRXehOfBPIaGnCRYgWqwuUYfij0YE8p/view?usp=sharing')
    if message.content == '!chart VILD':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1bVpsA2eB6ASMDKT-ZY0VRKSf-5QxPUiq/view?usp=sharing')
    if message.content == '!chart VIKO':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1ObSESaMdkmrqVEG6qblsuv5ouUjAo4Mb/view?usp=sharing')
    if message.content == '!chart VIJP':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1dAVZAjn2S-Pn6VXY4K0x-LTXwvuDb9ik/view?usp=sharing')
    if message.content == '!chart VIDP':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1ok9fylJr2UuuGivih0wpiZ7yioOWI3X3/view?usp=sharing')
    if message.content == '!chart VIDN':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1FbbhdhfSJ98YB9oNw_yewpVTkt8VDQAr/view?usp=sharing')
    if message.content == '!chart VIDD':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1fGeYXzS0981Q2o5a1w9BfikKP5RwbmYI/view?usp=sharing')
    if message.content == '!chart VIAR':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1SMPH-IpvRkU4XjW5ZH5SRgN6o9vzRoO4/view?usp=sharing')
    if message.content == '!chart VOVZ':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1F-El0GaK3PDqUVvKqwUDFp-wpcuW5Vqi/view?usp=sharing')
    if message.content == '!chart VOTV':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1KyaHxUga0NEixzcv1Rz9Vqc6cB5G7rRr/view?usp=sharing')
    if message.content == '!chart VOTR':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1j2Lb82dkJoSltZLd9Gp3sdY2FXS_187T/view?usp=sharing')
    if message.content == '!chart VOTP':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1W4bQomFaaI040bQeA3v0VLpE_huzdj1T/view?usp=sharing')
    if message.content == '!chart VOTK':
        await client.send_message(message.channel,'https://drive.google.com/file/d/17DDkQRPNcyUydtJlSnjAfZQp0LVATEkm/view?usp=sharing')
    if message.content == '!chart VORY':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1yjrl4KlJpkLylVBTsXplZCINDN6aBowF/view?usp=sharing')
    if message.content == '!chart VOND':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1hTOsbulK80put01skvYjnqJ0dlAKrzOm/view?usp=sharing')
    if message.content == '!chart VOMY':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1UYwqRwmeZYZ8t4LAsLve30rG4fthJA72/view?usp=sharing')
    if message.content == '!chart VOMM':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1CU1unJaoaDajRcPbivnQGtbYkOaGEsX6/view?usp=sharing')
    if message.content == '!chart VOML':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1B01Wfjee7E9dZ-hx0VUfFL-u5d97-6PP/view?usp=sharing')
    if message.content == '!chart VOMD':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1LbH9rvm6PcFnDgasb4h0sPsGya5p2PhO/view?usp=sharing')
    if message.content == '!chart VOJV':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1YkWBMjZ9kB9rTbFYSvzMkFwJjnGUXQuc/view?usp=sharing')
    if message.content == '!chart VOHY':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1Rfmch3fOcwQuNrLuuw5M-Mna_okjHLS6/view?usp=sharing')
    if message.content == '!chart VOHS':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1Sm4CxYpGKeFxUsCaVgkfaIlpdk6tvZSF/view?usp=sharing')
    if message.content == '!chart VOHB':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1EGw-7vYlc-bgjQepHxNH8nN0zEOwh9tK/view?usp=sharing')
    if message.content == '!chart VOGO':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1ztJytvhq-t1GzfpnESWF9neIVI3x2onY/view?usp=sharing')
    if message.content == '!chart VOCL':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1kATnewSL6DTLV-qk9XHc1dSWqIWggx8y/view?usp=sharing')
    if message.content == '!chart VOCI':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1SaL22PV3u2XJMkrctKPQPHMThLBcH4B_/view?usp=sharing')
    if message.content == '!chart VOCB':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1hKa0ucHZiBP8kIq7HQtv0aswe8XDAsyK/view?usp=sharing')
    if message.content == '!chart VOBZ':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1xEQmlwakF4jOiOpIK7npkR0O48kpOIsm/view?usp=sharing')
    if message.content == '!chart VOBM':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1SfBmbAvw3cW7FTMx4ZfbsCCOac70A9sN/view?usp=sharing')
    if message.content == '!chart VOBL':
        await client.send_message(message.channel,'https://drive.google.com/file/d/1ibOhOm9ErAA5EfEge-Pc4J9zbgIaMFCw/view?usp=sharing')
    if message.content == 'Hi':
        await client.send_message(message.channel,'Wassup')
    if message.content == 'how to use this':
        await client.send_message(message.channel,'type !chart (ICAO) it should work. If you face problems contact Ayaan Ahmad')
client.run(os.getenv('TOKEN'))
