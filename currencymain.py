import telebot
from telebot import types
import json
import requests
token = "1158025589:AAFMG9lSb1fSzGKTE2Uo-FKrq29GdmObx1o"
bot = telebot.TeleBot(token)


response = requests.get('https://minfin.com.ua/api/currency/ratelist/?currency1=usd&currency2=uah&converter_type=midbank')
json_data = json.loads(response.text)
usd_a = json_data['data']['rates']['buy']['USD']
usd_a = float(usd_a)
eur_a = json_data['data']['rates']['buy']['EUR']
eur_a = float(eur_a)
gbp_a = json_data['data']['rates']['buy']['GBP']
gbp_a = float(gbp_a)
rub_a = json_data['data']['rates']['buy']['RUB']
rub_a = float(rub_a)





joinedFile = open("db.txt", "r")
joinedUsers = set ()
for line in joinedFile:
    joinedUsers.add(line.strip())
joinedFile.close()

@bot.message_handler(commands=['start'])
def startJoin(message):
    try:
        if not str(message.chat.id) in joinedUsers:
            joinedFile = open("db.txt", "a")
            joinedFile.write(str(message.chat.id) + " " + message.from_user.username + "\n")
            joinedUsers.add(str(message.chat.id))
    except TypeError:
        if not str(message.chat.id) in joinedUsers:
            joinedFile = open("db.txt", "a")
            joinedFile.write(str(message.chat.id) + "\n")
            joinedUsers.add(str(message.chat.id))
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Сhoose the currency you want to convert to", reply_markup=keyboard())

@bot.message_handler(commands=['dbsend'])
def mess1(message):
    f = open("db.txt", "rb")
    bot.send_document(message.from_user.id, data=f)

@bot.message_handler(commands=['special'])
def mess2(message):
    for user in joinedUsers:
        bot.send_message(user, message.text[message.text.find(' '):])



def keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('USD🇺🇸')
    btn2 = types.KeyboardButton('EUR🇪🇺')
    btn3 = types.KeyboardButton('GBP🇬🇧')
    btn4 = types.KeyboardButton('RUB🇷🇺')
    markup.add(btn1, btn2, btn3, btn4)
    return markup
def kb_usd():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True, row_width=2)
    usd_btn1 = types.KeyboardButton('usd -> UAH🇺🇦')
    usd_btn2 = types.KeyboardButton('usd -> EUR🇪🇺')
    usd_btn3 = types.KeyboardButton('usd -> GBP🇬🇧')
    usd_btn4 = types.KeyboardButton('usd -> RUB🇷🇺')
    markup.add(usd_btn1, usd_btn2, usd_btn3, usd_btn4)
    return markup

def kb_eur():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True, row_width=2)
    eur_btn1 = types.KeyboardButton('eur -> UAH🇺🇦')
    eur_btn2 = types.KeyboardButton('eur -> USD🇺🇸')
    eur_btn3 = types.KeyboardButton('eur -> GBP🇬🇧')
    eur_btn4 = types.KeyboardButton('eur -> RUB🇷🇺')
    markup.add(eur_btn1, eur_btn2, eur_btn3, eur_btn4)
    return markup

def kb_gbp():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True, row_width=2)
    gbp_btn1 = types.KeyboardButton('gbp -> UAH🇺🇦')
    gbp_btn2 = types.KeyboardButton('gbp -> USD🇺🇸')
    gbp_btn3 = types.KeyboardButton('gbp -> EUR🇪🇺')
    gbp_btn4 = types.KeyboardButton('gbp -> RUB🇷🇺')
    markup.add(gbp_btn1, gbp_btn2, gbp_btn3, gbp_btn4)
    return markup

def kb_rub():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True, row_width=2)
    rub_btn1 = types.KeyboardButton('rub -> UAH🇺🇦')
    rub_btn2 = types.KeyboardButton('rub -> USD🇺🇸')
    rub_btn3 = types.KeyboardButton('rub -> EUR🇪🇺')
    rub_btn4 = types.KeyboardButton('rub -> GBP🇬🇧')
    markup.add(rub_btn1, rub_btn2, rub_btn3, rub_btn4)
    return markup


@bot.message_handler(content_types=['text'])
def anymsg(message):
    #first step
    if message.text == 'USD🇺🇸':
        bot.send_message(message.from_user.id, "Choose the currency you want to convert USD to, than enter needed value", reply_markup=kb_usd())
    if message.text == 'EUR🇪🇺':
        bot.send_message(message.from_user.id, "Choose the currency you want to convert EUR to, than enter needed value", reply_markup=kb_eur())
    if message.text == 'GBP🇬🇧':
        bot.send_message(message.from_user.id, "Choose the currency you want to convert GBP to, than enter needed value", reply_markup=kb_gbp())
    if message.text == 'RUB🇷🇺':
        bot.send_message(message.from_user.id, "Choose the currency you want to convert RUB to, than enter needed value", reply_markup=kb_rub())

    #second step(usd to)
    if message.text == 'usd -> UAH🇺🇦':
        bot.register_next_step_handler(message, usd_uah)
    if message.text == 'usd -> EUR🇪🇺':
        bot.register_next_step_handler(message, usd_eur)
    if message.text == 'usd -> GBP🇬🇧':
        bot.register_next_step_handler(message, usd_gbp)
    if message.text == 'usd -> RUB🇷🇺':
        bot.register_next_step_handler(message, usd_rub)

    #second step(eur to)
    if message.text == 'eur -> UAH🇺🇦':
        bot.register_next_step_handler(message, eur_uah)
    if message.text == 'eur -> USD🇺🇸':
        bot.register_next_step_handler(message, eur_usd)
    if message.text == 'eur -> GBP🇬🇧':
        bot.register_next_step_handler(message, eur_gbp)
    if message.text == 'eur -> RUB🇷🇺':
        bot.register_next_step_handler(message, eur_rub)

    #second step(gbp to)
    if message.text == 'gbp -> UAH🇺🇦':
        bot.register_next_step_handler(message, gbp_uah)
    if message.text == 'gbp -> USD🇺🇸':
        bot.register_next_step_handler(message, gbp_usd)
    if message.text == 'gbp -> EUR🇪🇺':
        bot.register_next_step_handler(message, gbp_eur)
    if message.text == 'gbp -> RUB🇷🇺':
        bot.register_next_step_handler(message, gbp_rub)


    #second step(rub to)
    if message.text == 'rub -> UAH🇺🇦':
        bot.register_next_step_handler(message, rub_uah)
    if message.text == 'rub -> USD🇺🇸':
        bot.register_next_step_handler(message, rub_usd)
    if message.text == 'rub -> EUR🇪🇺':
        bot.register_next_step_handler(message, rub_eur)
    if message.text == 'rub -> GBP🇬🇧':
        bot.register_next_step_handler(message, rub_gbp)



#USD
def usd_uah(message):
    try:
        message.text = float(message.text)
        texto1 = f'{message.text*usd_a}'
        texto1 = float(texto1)
        usd_txt = round(texto1, 2)
        bot.reply_to(message, usd_txt)
        bot.send_message(message.from_user.id, "Return to homepage...Сhoose the currency you want to convert to", reply_markup=keyboard())
    except ValueError:
        bot.reply_to(message, "Enter only numbers. Press needed and enter value again")

def usd_eur(message):
    try:
        message.text = float(message.text)
        texto1 = f'{message.text*usd_a/eur_a}'
        texto1 = float(texto1)
        eur_txt = round(texto1, 2)
        bot.reply_to(message, eur_txt)
        bot.send_message(message.from_user.id, "Return to homepage...Сhoose the currency you want to convert to", reply_markup=keyboard())
    except ValueError:
        bot.reply_to(message, "Enter only numbers. Press needed and enter value again")

def usd_gbp(message):
    try:
        message.text = float(message.text)
        texto1 = f'{message.text*usd_a/gbp_a}'
        texto1 = float(texto1)
        gbp_txt = round(texto1, 2)
        bot.reply_to(message, gbp_txt)
        bot.send_message(message.from_user.id, "Return to homepage...Сhoose the currency you want to convert to", reply_markup=keyboard())
    except ValueError:
        bot.reply_to(message, "Enter only numbers. Press needed and enter value again")

def usd_rub(message):
    try:
        message.text = float(message.text)
        texto1 = f'{message.text*usd_a/rub_a}'
        texto1 = float(texto1)
        rub_txt = round(texto1, 2)
        bot.reply_to(message, rub_txt)
        bot.send_message(message.from_user.id, "Return to homepage...Сhoose the currency you want to convert to", reply_markup=keyboard())
    except ValueError:
        bot.reply_to(message, "Enter only numbers. Press needed and enter value again")
#EURO
def eur_uah(message):
    try:
        message.text = float(message.text)
        texto1 = f'{message.text*eur_a}'
        texto1 = float(texto1)
        eur_txt = round(texto1, 2)
        bot.reply_to(message, eur_txt)
        bot.send_message(message.from_user.id, "Return to homepage...Сhoose the currency you want to convert to", reply_markup=keyboard())
    except ValueError:
        bot.reply_to(message, "Enter only numbers. Press needed and enter value again")


def eur_usd(message):
    try:
        message.text = float(message.text)
        texto1 = f'{message.text*eur_a/usd_a}'
        texto1 = float(texto1)
        eur_txt = round(texto1, 2)
        bot.reply_to(message, eur_txt)
        bot.send_message(message.from_user.id, "Return to homepage...Сhoose the currency you want to convert to", reply_markup=keyboard())
    except ValueError:
        bot.reply_to(message, "Enter only numbers. Press needed and enter value again")


def eur_gbp(message):
    try:
        message.text = float(message.text)
        texto1 = f'{message.text*eur_a/gbp_a}'
        texto1 = float(texto1)
        eur_txt = round(texto1, 2)
        bot.reply_to(message, eur_txt)
        bot.send_message(message.from_user.id, "Return to homepage...Сhoose the currency you want to convert to", reply_markup=keyboard())
    except ValueError:
        bot.reply_to(message, "Enter only numbers. Press needed and enter value again")

def eur_rub(message):
    try:
        message.text = float(message.text)
        texto1 = f'{message.text*eur_a/rub_a}'
        texto1 = float(texto1)
        eur_txt = round(texto1, 2)
        bot.reply_to(message, eur_txt)
        bot.send_message(message.from_user.id, "Return to homepage...Сhoose the currency you want to convert to", reply_markup=keyboard())
    except ValueError:
        bot.reply_to(message, "Enter only numbers. Press needed and enter value again")

#BRITAIN
def gbp_uah(message):
    try:
        message.text = float(message.text)
        texto1 = f'{message.text*gbp_a}'
        texto1 = float(texto1)
        gbp_txt = round(texto1, 2)
        bot.reply_to(message, gbp_txt)
        bot.send_message(message.from_user.id, "Return to homepage...Сhoose the currency you want to convert to", reply_markup=keyboard())
    except ValueError:
        bot.reply_to(message, "Enter only numbers. Press needed and enter value again")


def gbp_usd(message):
    try:
        message.text = float(message.text)
        texto1 = f'{message.text*gbp_a/usd_a}'
        texto1 = float(texto1)
        gbp_txt = round(texto1, 2)
        bot.reply_to(message, gbp_txt)
        bot.send_message(message.from_user.id, "Return to homepage...Сhoose the currency you want to convert to", reply_markup=keyboard())
    except ValueError:
        bot.reply_to(message, "Enter only numbers. Press needed and enter value again")


def gbp_eur(message):
    try:
        message.text = float(message.text)
        texto1 = f'{message.text*gbp_a/eur_a}'
        texto1 = float(texto1)
        gbp_txt = round(texto1, 2)
        bot.reply_to(message, gbp_txt)
        bot.send_message(message.from_user.id, "Return to homepage...Сhoose the currency you want to convert to", reply_markup=keyboard())
    except ValueError:
        bot.reply_to(message, "Enter only numbers. Press needed and enter value again")

def gbp_rub(message):
    try:
        message.text = float(message.text)
        texto1 = f'{message.text*gbp_a/rub_a}'
        texto1 = float(texto1)
        gbp_txt = round(texto1, 2)
        bot.reply_to(message, gbp_txt)
        bot.send_message(message.from_user.id, "Return to homepage...Сhoose the currency you want to convert to", reply_markup=keyboard())
    except ValueError:
        bot.reply_to(message, "Enter only numbers. Press needed and enter value again")

#RUB
def rub_uah(message):
    try:
        message.text = float(message.text)
        texto1 = f'{message.text*rub_a}'
        texto1 = float(texto1)
        rub_txt = round(texto1, 2)
        bot.reply_to(message, rub_txt)
        bot.send_message(message.from_user.id, "Return to homepage...Сhoose the currency you want to convert to", reply_markup=keyboard())
    except ValueError:
        bot.reply_to(message, "Enter only numbers. Press needed and enter value again")

def rub_usd(message):
    try:
        message.text = float(message.text)
        texto1 = f'{message.text*rub_a/usd_a}'
        texto1 = float(texto1)
        rub_txt = round(texto1, 2)
        bot.reply_to(message, rub_txt)
        bot.send_message(message.from_user.id, "Return to homepage...Сhoose the currency you want to convert to", reply_markup=keyboard())
    except ValueError:
        bot.reply_to(message, "Enter only numbers. Press needed and enter value again")

def rub_eur(message):
    try:
        message.text = float(message.text)
        texto1 = f'{message.text*rub_a/eur_a}'
        texto1 = float(texto1)
        rub_txt = round(texto1, 2)
        bot.reply_to(message, rub_txt)
        bot.send_message(message.from_user.id, "Return to homepage...Сhoose the currency you want to convert to", reply_markup=keyboard())
    except ValueError:
        bot.reply_to(message, "Enter only numbers. Press needed and enter value again")

def rub_gbp(message):
    try:
        message.text = float(message.text)
        texto1 = f'{message.text*rub_a/gbp_a}'
        texto1 = float(texto1)
        rub_txt = round(texto1, 2)
        bot.reply_to(message, rub_txt)
        bot.send_message(message.from_user.id, "Return to homepage...Сhoose the currency you want to convert to", reply_markup=keyboard())
    except ValueError:
        bot.reply_to(message, "Enter only numbers. Press needed and enter value again")











if __name__ == '__main__':
    bot.polling(none_stop=True)
