from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from groupy import Group, Member, Bot
import time


# chatbot = ChatBot('Asshole', trainer='chatterbot.trainers.ChatterBotCorpusTrainer')
# chatbot.train("chatterbot.corpus.english")
# chatbot.set_trainer(ListTrainer)
# for i in range(100):
# 	chatbot.train(['Do you like anime?','Anime is fucking gay','You are fucking gay','Kill yourself','Okay fine.',])
# 	chatbot.train(['Anime','You are a weeb', 'Oh yeah mr crabs',])
# 	chatbot.train(['traps', 'Traps are fucking gay'])
# 	chatbot.train(['Are traps gay?', 'Only if you want them to be, faggot fucker'])
# #while True:
#	words = input('')
#	print(chatbot.get_response(words))



print(str(Group.list()))
num = int(input('choose one: '))
groups = Group.list()
group = groups[num]

bot = Bot.create('Automated Asshole', group, 'https://pbs.twimg.com/profile_images/828786047207092224/gEMoTEQc.jpg', callback_url='https://www.lego.com')

#bot.post("BEHOLD! It is I, the Automated Assole!!")
#time.sleep(5)
#bot.post('Send me a message @owo to discover my infinite wisdom!')
while True:
	time.sleep(3)
	messages = group.messages()
	message = messages.newest
	print(message.text)
# #	if (message.text.startswith('@owo ')):
# 		text = message.text
# 		text = text[5:]
# 		print(text)
# 		response = chatbot.get_response(text)
# 		print(type(response))
# 		print(response)
# 		bot.post(str(response))

