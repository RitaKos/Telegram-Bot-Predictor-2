from aiogram import Dispatcher, md
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import *
from random import Random, random, choice
from  pathlib import Path

topic1_list=[]
topic1_file_list= Path('video1') #write list to file
topic1_list_full=topic1_file_list.read_text().rsplit() # get list from file

topic2_list=[]
topic2_file_list= Path('video2') #write list to file
topic2_list_full=topic2_file_list.read_text().rsplit() # get list from file

topic3_list=[]
topic3_file_list= Path('video3') #write list to file
topic3_list_full=topic3_file_list.read_text().rsplit() # get list from file

topic4_list=[]
topic4_file_list= Path('video4') #write list to file
topic4_list_full=topic4_file_list.read_text().rsplit() # get list from file

new_list=[]


async def user_start(com: Message):
    '''
    Receive start command from user.
    Greeting user by name.
    :param command:
    :param message: str
    :return: str
    '''
    user_location = com.from_user.language_code
    if user_location == 'ru':
        await com.answer(
        f"Привет, {com.from_user.first_name}! \nХм..так..так... \nКажется, кому-то нужен мой совет. Не так ли? ")
    else:
        await com.answer(
        f"Hello, {com.from_user.first_name}! \nHm..Well, well.. \nI guess, you need my advice. Isn\'t it? ")


def register_user(dp: Dispatcher):
    '''
    Register massage with start command in handler
    :param dp:
    :return:
    '''
    dp.register_message_handler(user_start, commands=['start'], content_types=['text'], is_admin=False)


async def user_about(com: Message):
    '''
    Answer to /about command received by user
    :param com:
    :return:
    '''
    user_location = com.from_user.language_code
    if user_location == 'ru':
        await com.answer(
            '''Привет! Я - бот оракул.
            Я могу посмотеть в будущее и помочь тебе
            с трудным решением. 
            Я знаю все об этом мире, но если расскажу тебе все как есть,
            это может лохо сказаться на реальтности.
            Но... я могу дать тебе некотрые подсказки ;)
            Сформулируй свой вопрос как можно четче в своей голове
            и выбери наиболее походящую тему из /topics .
            
            И еще.. Не забудь! Это наш с тобой секрет ;)
            
            '''
        )
    else:
        await com.answer(
        '''Hello! I am bot-oracle.
        No,no..Not that Oracle.. :D
        
        I can look into the future and help you to make a decision.
        I know everything in this world, but if I tell you this information directly
        it might be dangerous for our reality.
        But I can give you some hints ;)
        Formulate your question in your head and choose the topic from /topics, 
        witch is more closer to your problem.
        
        And, hey... Don't forget! It's our secret ;)
        
        '''
    )


def register_about(dp: Dispatcher):
    '''
    Register massage with /about command in handler
    :param dp:
    :return:
    '''
    dp.register_message_handler(user_about, commands=['about'], content_types=['text'], is_admin=False)


async def user_topics(com: Message):
    '''
    Send topics list to user
    :param com:
    :return:
    '''
    topics = ['/topic1', '/topic2', '/topic3', '/topic4']
    user_location = com.from_user.language_code
    if user_location == 'ru':
        await com.answer(md.text(md.bold('Итак, что ты хочешь спросить?'),
                                 md.text('🔸', md.bold('Делать или не делать:'), md.code(topics[0])),
                                 md.text('🔸', md.bold('Что ждет впереди:'), md.code(topics[1])),
                                 md.text('🔸', md.bold('Вопрос о некотором человеке:'), md.code(topics[2])),
                                 md.text('🔸', md.bold('Что мне нужно делать в ситуации:'), md.code(topics[3])),
                                 sep='\n',
                                 ))
    else:
        await com.answer(md.text(md.bold('What you want to know?'),
                     md.text('🔸', md.bold('Do or not to do:'), md.code(topics[0])),
                     md.text('🔸', md.bold('What is behind:'), md.code(topics[1])),
                     md.text('🔸', md.bold('About some person:'), md.code(topics[2])),
                     md.text('🔸', md.bold('What do you need:'), md.code(topics[3])),
                     sep='\n',
                     ))


def register_topics(dp: Dispatcher):
    '''
    Register massage with /topics command in handler
    :param dp:
    :return:
    '''
    dp.register_message_handler(user_topics, commands=['topics'], content_types=['text'], is_admin=False)

async def get_file_id(f: Message):
    '''
    Get file_id from received video1, add it to list
    :param f: Massage
    :return: str
    '''
    file = str(f.video.file_id)
    if  str(f.caption) == 't1':
            topic1_list.append(file)
            try:
                topic1_file_list.write_text('\n'.join(topic1_list))
                await f.answer(f'File {file} is added to the list 1')
            except FileNotFoundError:
                await f.answer('Not found file for writing')
            finally:
                return file

    if  str(f.caption) =='t2':
            topic2_list.append(file)
            try:
                topic2_file_list.write_text('\n'.join(topic2_list))
                await f.answer(f'File {file} is added to the list 2')
            except FileNotFoundError:
                await f.answer('Not found file for writing')
            finally:
                return file

    if  str(f.caption) == 't3':
            topic3_list.append(file)
            try:
                topic3_file_list.write_text('\n'.join(topic3_list))
                await f.answer(f'File {file} is added to the list 3')
            except FileNotFoundError:
                await f.answer('Not found file for writing')
            finally:
                return file

    if  str(f.caption) == 't4':
            topic4_list.append(file)
            try:
                topic4_file_list.write_text('\n'.join(topic4_list))
                await f.answer(f'File {file} is added to the list 4')
            except FileNotFoundError:
                await f.answer('Not found file for writing')
            finally:
                return file
    else:
            await f.answer(f'File {file} topic is not defined')
    return file


def register_file(dp: Dispatcher):
    '''
    Admin send video1 for getting file_id
    :param dp:
    :return:
    '''
    dp.register_message_handler(get_file_id, content_types=['video'])

async def cmd_topic1(mes: Message):
    '''
    Send answer to user according his request (topic1).
    Choice is random from local storage.
    :param mes:
    :return:
    '''
    user_location = mes.from_user.language_code
    if user_location == 'ru':
        answer = choice(topic1_list_full)
        await mes.answer_video(video=answer,protect_content=True)
    else: pass

def register_topic1(dp: Dispatcher):
    '''
    Register massage with /topic1 command in handler
    :param dp:
    :return:
    '''
    dp.register_message_handler(cmd_topic1, commands=['topic1'], content_types=['text'])

async def get_text_message(message: Message):
    '''
    Receive text message from user and answer.
    :param message: str
    :return: str
    '''

    if message.text.lower() in {'hi', 'hello', 'good afternoon', 'good morning', 'good evening'}:
        return await message.answer('Hello!!!You looking great today!')
    if message.text.lower() in {'привет', 'приветик', 'здарова', 'здравствуй', 'салют','хай'}:
        return await message.answer('Ой, привет! Ты выглядишь супер сегодня!')

    if message.text.lower() in {'thank', 'thanks', 'thank you', 'thnks'}:
        return await message.reply(
            '''You are welcome! 
        
        And now let\'s try to find answers! 
        Choose the /topics, which is much closer to you problem'''
        )
    if message.text.lower() in {'спасибо', 'пасиб', 'мило', 'спасибо за комплимент', 'спс'}:
        return await message.answer(
            '''Обращайся) 
    
                    А сейчас давай попробуем найти ответы на твои вопросы! 
                    Выбери вопрос из /topics, который максимально близок к твоему вопросу'''
        )

    if message.text.lower() in {'you too', 'u too', 'and you too'}:
        return await message.reply(
            '''Thanks, I know it ))
        
        And now let\'s try to find answers!
        Choose the /topics, which is much closer to you problem'''
        )
    if message.text.lower() in {'и ты', 'ты тоже', 'и ты ничего', 'и ты тоже'}:
        return await message.reply(
            '''Спасибо, я в курсе ))

        А сейчас давай попробуем найти ответы на твои вопросы! 
        Выбери вопрос из /topics, который максимально близок к твоему вопросу'''
        )
    if message.text.lower() in {'yes', 'ok', 'yep', 'I do', 'it is', 'right guess', 'u guess', 'you guess'}:
        return await message.answer(
            ''' Good !
            Let\'s try to find answers! Choose the /topics, which is much closer to you problem ''')
    if message.text.lower() in {'да', 'ок', 'ага', 'может быть', 'наверное', 'возможно', 'угадал', 'верно'}:
        return await message.answer(
            ''' Отлично !
                Давай попробуем найти ответы на твои вопросы! 
                Выбери вопрос из /topics, который максимально близок к твоему вопросу ''')
    else:
        user_location = message.from_user.language_code
        if user_location == 'ru':
            return await message.reply(
                '''Давай-ко об этом поболтаем позже? 

                А сейчас давай попробуем найти ответы на твои вопросы! 
                Выбери вопрос из /topics, который максимально близок к твоему вопросу.

                Хочешь узнать обо мне побольше, кликни /about ''')
        else:
            return await message.reply(
            '''I would talk about it another time, ok? 
            
            And now let\'s try to find answers! Choose the /topics, which is much closer to you problem.
            
            Have any questions? Click /about ''')


def register_user_mess(dp: Dispatcher):
    dp.register_message_handler(get_text_message, content_types=['text'], is_admin=False)

