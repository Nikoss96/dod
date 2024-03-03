import requests
import telebot
#from telegram import Update
#from telegram.ext import CallbackContext, CommandHandler, Updater
# Токен бота
#Main_test_bot
bot_token = '7124695171:AAGrVLxDoOCOWt0LivOnZRuK8usCp00sSGM'


bot = telebot.TeleBot(bot_token)

#Клавиатуры внутри бота
keyboard_main_menu = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
keyboard_main_menu.row('Развлечения','Спорт')

keyboard_sport1 = telebot.types.InlineKeyboardMarkup()
keyboard_sport1.add(telebot.types.InlineKeyboardButton(text="Просмотр кино",callback_data="sport1_false") )
keyboard_sport1.add(telebot.types.InlineKeyboardButton(text="Баскетбольный матч",callback_data="sport1_true") )
keyboard_sport1.add(telebot.types.InlineKeyboardButton(text="Гитарный вечер",callback_data="sport1_false") )

keyboard_sport2 = telebot.types.InlineKeyboardMarkup()
keyboard_sport2.add(telebot.types.InlineKeyboardButton(text="Привести сборную России",callback_data="sport2_false") )
keyboard_sport2.add(telebot.types.InlineKeyboardButton(text="Построить огромную баскетбольную площадку",callback_data="sport2_false") )
keyboard_sport2.add(telebot.types.InlineKeyboardButton(text="Позвать сборную Вышки",callback_data="sport2_true") )


keyboard_sport3 = telebot.types.InlineKeyboardMarkup()
keyboard_sport3.add(telebot.types.InlineKeyboardButton(text="100",callback_data="sport3_true") )
keyboard_sport3.add(telebot.types.InlineKeyboardButton(text="500",callback_data="sport3_true") )
keyboard_sport3.add(telebot.types.InlineKeyboardButton(text="10000",callback_data="sport3_false") )

keyboard_fin = telebot.types.InlineKeyboardMarkup()
keyboard_fin.add(telebot.types.InlineKeyboardButton(text="За месяц",callback_data="fin_true") )
keyboard_fin.add(telebot.types.InlineKeyboardButton(text="За 2 недели",callback_data="fin_false") )
keyboard_fin.add(telebot.types.InlineKeyboardButton(text="За день до мероприятия",callback_data="fin_false_agressive") )


keyboard_ent1 = telebot.types.InlineKeyboardMarkup()
keyboard_ent1.add(telebot.types.InlineKeyboardButton(text="Кругосветное путешествие",callback_data="ent1_false") )
keyboard_ent1.add(telebot.types.InlineKeyboardButton(text="Фиджитал футбол",callback_data="ent1_false2") )
keyboard_ent1.add(telebot.types.InlineKeyboardButton(text="Фестиваль",callback_data="ent1_true") )

keyboard_ent2 = telebot.types.InlineKeyboardMarkup()
keyboard_ent2.add(telebot.types.InlineKeyboardButton(text="День студента",callback_data="ent2_true") )
keyboard_ent2.add(telebot.types.InlineKeyboardButton(text="Хэллоуин",callback_data="ent2_false") )
keyboard_ent2.add(telebot.types.InlineKeyboardButton(text="Фестиваль по Data Science",callback_data="ent2_false") )


keyboard_ent3 = telebot.types.InlineKeyboardMarkup()
keyboard_ent3.add(telebot.types.InlineKeyboardButton(text="23 февраля",callback_data="ent3_false") )
keyboard_ent3.add(telebot.types.InlineKeyboardButton(text="25 января",callback_data="ent3_true") )
keyboard_ent3.add(telebot.types.InlineKeyboardButton(text="5 октября",callback_data="ent3_false") )

keyboard_restart3 = telebot.types.InlineKeyboardMarkup()
keyboard_restart3.add(telebot.types.InlineKeyboardButton(text="Да",callback_data="restart3_true") )
keyboard_restart3.add(telebot.types.InlineKeyboardButton(text="Тоже да, но ниже",callback_data="restart3_true") )
keyboard_restart3.add(telebot.types.InlineKeyboardButton(text="Однозначно",callback_data="restart3_true") )
keyboard_restart3.add(telebot.types.InlineKeyboardButton(text="Конечно",callback_data="restart3_true") )



#Инит для обработки колбека
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "sport1_false":
        bot.answer_callback_query(call.id, "Это не совсем та тематика!")
    elif call.data == "sport1_true":
        bot.send_message(call.from_user.id, f"Отлично! Хороший вариант! Поговори с Аней, она поможет)")
        bot.send_photo(call.from_user.id, photo=open('pictures\\ann.png', 'rb'))
        bot.send_message(call.from_user.id, f"Привет! Я — Аня, мать одного шпицового дракона, медиапродюсер музыкальной группы за пределами Вышки и пленочный фотограф выходного дня. Люблю горы, ганпаудер и тишину. Курирую спортивные и туристические студенческие клубы, телеграм-канал <Пусть меня поддержат> и знаю все о внеакадемической мобильности \n\n Что ты хочешь на свое мероприятие?",reply_markup=keyboard_sport2)
    elif call.data == "sport2_false":
        bot.answer_callback_query(call.id, f"Не очень реалистично, хоть и классно)")
    elif call.data == "sport2_true":
        bot.send_message(call.from_user.id, f"Супер, сделаем!")
        bot.send_photo(call.from_user.id, photo=open('pictures\\sonya.png', 'rb'))
        bot.send_message(call.from_user.id, f"Привет! Меня зовут Соня, люблю смотреть в небо, петь, пока никто не слышит, и учить языки. В Вышке курирую все развлекательные студенческие сообщества и помогаю в организации мероприятий! \n\n Сколько человек хочешь у нас разместить?",
                         reply_markup=keyboard_sport3
                         )
    elif call.data == "sport3_false":
        bot.answer_callback_query(call.id, f"Так много мы не уместим(")
    elif call.data == "sport3_true":
        bot.send_message(call.from_user.id, f"Самое то!")
        bot.send_photo(call.from_user.id, photo=open('pictures\\olya2.png', 'rb'))
        bot.send_message(call.from_user.id, f"Я — Оля, люблю какао, котиков и спать. Являюсь куратором студактивов, отвечаю за бронирование аудиторий, пропуска и СЭД, который вэри сэд. Не отвечаю в тг тем кто не котик и без какао. \n\n Теперь нам нужно оформить всё это официально. Насколько заранее пришлешь мне все документы?",
                         reply_markup=keyboard_fin
                         )
    elif call.data == "ent1_false":
        bot.answer_callback_query(call.id, "Это не совсем та тематика!")
    elif call.data == "ent1_false2":
        bot.answer_callback_query(call.id, "Это спортивное мероприятие!")
    elif call.data == "ent1_true":
        bot.send_message(call.from_user.id, f"Хороший выбор! Поговори с Эмилией, она поможет)")
        bot.send_photo(call.from_user.id, photo=open('pictures\\milya.png', 'rb'))
        bot.send_message(call.from_user.id, f"Всем привет! Меня зовут Маховая Эмилия и я люблю ОЧЕНЬ ГОРЯЧИЙ капучино с корицей и фисташковый круассан. Курирую Просветительские организации, а еще являюсь менеджером Кураторов Вышки. Всегда очень рада поболтать с вами, посмеяться в Т323 и обсудить с вами все на свете! \n\n Давай выберем что-то, подходящее для всех СО. Можешь придумать?",reply_markup=keyboard_ent2)
    elif call.data == "ent2_false":
        bot.answer_callback_query(call.id, f"Боюсь, что слишком специфично!")
    elif call.data == "ent2_true":
        bot.send_message(call.from_user.id, f"Класс! Туда как раз можно позвать всех-всех! \n Сходи-ка теперь к Даше, вдруг она против...")
        bot.send_photo(call.from_user.id, photo=open('pictures\\dasha.png', 'rb'))
        bot.send_message(call.from_user.id, f"Привет! Я — Даша, люблю латте с фисташковым сиропом, миндальный круассан, театры, мопсов и психологию. Являюсь куратором киноклубов, отвечаю за телеграм-канал ЦПСИ и помогаю ГосВышке с организацией встреч. \n\n Идея мне очень нравится, давай только уточним, в какой день ты бы провел мероприятие?",
                         reply_markup=keyboard_ent3
                         )
    elif call.data == "ent3_false":
        bot.answer_callback_query(call.id, f"Это какой-то другой праздник...")
    elif call.data == "ent3_true":
        bot.send_message(call.from_user.id, f"Да! Тогда запланируем на следующий год. Оля поможет с оформлением, зайди к ней.")
        bot.send_photo(call.from_user.id, photo=open('pictures\\olya2.png', 'rb'))
        bot.send_message(call.from_user.id, f"Я — Оля, люблю какао, котиков и спать. Являюсь куратором студактивов, отвечаю за бронирование аудиторий, пропуска и СЭД, который вэри сэд. Не отвечаю в тг тем кто не котик и без какао. \n\n Теперь нам нужно оформить всё это официально. Насколько заранее пришлешь мне все документы?",
                         reply_markup=keyboard_fin
                         )
    elif call.data == "fin_true":
        bot.send_message(call.from_user.id, f"Так мы точно всё успеем, спасибо!")
        bot.send_photo(call.from_user.id, photo=open('pictures\\vorona.png', 'rb'))
        bot.send_message(call.from_user.id, f"Квест пройден! \n\n Мы обожаем инициативных студентов, подписывайся скорей:")
        bot.send_photo(call.from_user.id, photo=open('pictures\\links.png', 'rb'))
        bot.send_message(call.from_user.id, f"Хочешь ещё раз?",reply_markup=keyboard_restart3)
    elif call.data == "fin_false":
        bot.send_message(call.from_user.id, f"Еле-еле успеем, мы быстрые!) Но в следующий раз сделай это заранее!")
        bot.send_photo(call.from_user.id, photo=open('pictures\\vorona.png', 'rb'))
        bot.send_message(call.from_user.id, f"Квест пройден! \n\n Мы обожаем инициативных студентов, подписывайся скорей:")
        bot.send_photo(call.from_user.id, photo=open('pictures\\links.png', 'rb'))
        bot.send_message(call.from_user.id, f"Хочешь ещё раз?",reply_markup=keyboard_restart3)
    elif call.data == "fin_false_agressive":
        bot.answer_callback_query(call.id, f"А ты забавный)")
    elif call.data == "restart3_true":
        bot.send_message(call.from_user.id, f"/start")


        



@bot.message_handler(commands=['start'])
def start_message(message):
    user_id = message.from_user.username
    bot.send_message(message.chat.id, 'Привет!')
    bot.send_message(message.chat.id, 'В нашем боте ты сможешь попробовать себя в организации мероприятия вместе с ЦПСИ!')
    bot.send_message(message.chat.id, 'Выбери направление: \n - Развлечения; \n - Спорт.', reply_markup=keyboard_main_menu)
    
@bot.message_handler(content_types=['text'])
def default_test(message):
    if message.text.lower() == 'спорт':
        bot.send_photo(message.chat.id, photo=open('pictures\\natalya2.png', 'rb'))
        bot.send_message(message.chat.id, 'Всем привет! Я — Наталия, директор ЦПСИ. Курирую национальные клубы, помогаю студентам в реализации их идей, проектов и мероприятий! Взаимодействую с подразделениями всей Вышки в том числе для проведения культурно-массовых мероприятий 🌞 \n\n Здорово, что ты выбрал спорт! Какое мероприятие бы сделал? ', reply_markup=keyboard_sport1)
    elif message.text.lower() == 'в начало':
        bot.send_message(message.chat.id, 'Играй заново!)', reply_markup=keyboard_main_menu)
    elif message.text.lower() == 'развлечения':
        bot.send_photo(message.chat.id, photo=open('pictures\\natalya2.png', 'rb'))
        bot.send_message(message.chat.id, 'Всем привет! Я — Наталия, директор ЦПСИ. Курирую национальные клубы, помогаю студентам в реализации их идей, проектов и мероприятий! Взаимодействую с подразделениями всей Вышки в том числе для проведения культурно-массовых мероприятий 🌞 \n\n Нам всем не помешает развлечься! Какую тему для мероприятия выберешь? ', reply_markup=keyboard_ent1)
        #bot.send_message(message.chat.id, '🔧Ветка на реконструкции🔧')
        
bot.polling()