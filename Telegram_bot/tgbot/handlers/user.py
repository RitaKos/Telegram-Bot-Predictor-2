from aiogram import Dispatcher, md
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import *
from random import Random, random, choice

topic1_list=[]
topic2_list=[]
topic3_list=[]
topic4_list=[]
new_list=[]


async def user_start(com: Message):
    '''
    Receive start command from user.
    Greeting user by name.
    :param command:
    :param message: str
    :return: str
    '''
    await com.answer(
        f"Hello, {com.from_user.first_name}! \nHm..Well, well.. \nI guess, you need my advice. Isn\'t it?")


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
    await com.answer(
        '''Hello! I am bot-oracle.
        No,no..Not that Oracle.. :D
        
        I can look into the future and help you to make a decision,
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
    topics=['/topic1','/topic2','/topic3','/topic4']
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
    Get file_id from received video, add it to list
    :param f: Massage
    :return: str
    '''
    file=str(f.video.file_id)
    topic1_list.append(file)
    return file
   # In progress: defining the right topic of video. As well, list should store data in file.
# Know it is updates every run process
   # text=file.get_file(f)
   # if text=='topic1':
   # if text == 'topic2':
   #     topic2_list.append(file_id)
   # if text == 'topic3':
  #      topic3_list.append(file_id)
  #  if text == 'topic4':
  #      topic4_list.append(file_id)
  #  else: new_list.append(file_id)



def register_file(dp: Dispatcher):
    '''
    Admin send video for getting file_id
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

    answer = choice(topic1_list)
    await mes.answer_video(video=answer,protect_content=True)


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

    if message.text.lower() in {'thank', 'thanks', 'thank you', 'thnks'}:
        return await message.reply(
            '''You are welcome! 
        
        And now let\'s try to find answers! 
        Choose the /topics, which is much closer to you problem'''
        )

    if message.text.lower() in {'you too', 'u too', 'and you too'}:
        return await message.reply(
            '''Thanks, I know it ))
        
        And now let\'s try to find answers!
        Choose the /topics, which is much closer to you problem'''
        )
    if message.text.lower() in {'yes', 'ok', 'yep', 'I do', 'it is', 'right guess', 'u guess', 'you guess'}:
        return await message.answer(
            ''' Good !
            Let\'s try to find answers! Choose the /topics, which is much closer to you problem ''')
    else:
        return await message.reply(
            '''I would talk about it another time, ok? 
            
            And now let\'s try to find answers! Choose the /topics, which is much closer to you problem.
            
            Have any questions? Click /about ''')


def register_user_mess(dp: Dispatcher):
    dp.register_message_handler(get_text_message, content_types=['text'], is_admin=False)

