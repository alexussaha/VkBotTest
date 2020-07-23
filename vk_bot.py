import requests
import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType
import wikipedia #Модуль Википедии


wikipedia.set_lang("RU")

vk_session = vk_api.VkApi(token='Token')

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:

   #Слушаем longpoll, если пришло сообщение то:
        if event.text == 'Бот' or event.text == 'бот': #Если написали заданную фразу
            if event.from_user: #Если написали в ЛС
                vk.messages.send( #Отправляем сообщение
                    user_id=event.user_id,
                    message='Привет',
                    random_id = random.random()
                )
        if event.text == 'Википедия' or event.text == 'Вики' or event.text == 'википедия' or event.text == 'вики' or event.text == 'Wikipedia' or event.text == 'wikipedia' or event.text == 'Wiki' or event.text == 'wiki':  # если нам пришло сообщение с текстом Википедия или Вики или ... или wiki
            if event.from_user:  # Если написали в KC
                vk.messages.send(
                    user_id=event.user_id,
                    message='Введите запрос',
                    random_id = random.random()
                )
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:  # Пинаем longpoll
                    if event.from_user:
                        try:
                            answer = str(wikipedia.summary(event.text))

                        except wikipedia.exceptions.DisambiguationError:
                            answer = "Переформулируй, плиз"
                        except wikipedia.exceptions.PageError:
                            answer = 'Неа... Не нашёл\n'
                        vk.messages.send(  # Если написали в ЛС
                            user_id=event.user_id,
                            message='Вот что я нашёл: \n' + answer,
                            random_id = random.random()
                    # Пишем "Вот что я нашёл" И то что вернёт нам api Wikipedia по запросу текста сообщения
                        )
                        break  # выходим из цикла
                continue
