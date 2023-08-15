from django.shortcuts import render , redirect

from django.http import HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import spacy
import en_core_web_sm

nlp = spacy.load("en_core_web_sm")
lp = en_core_web_sm.load()
# Create your views here.

bot =ChatBot('chatbot', read_only=False,logic_adapter=['chatterbot.logic.BestMatch'])

list_to_train = ([

    "hi",#question
    "Hi there",#answer
    "what's your name",
    "iam chatin",
    "your mother",
    "lomm mtaa omkk ",
    'I need your assistance regarding my order',
'Please, Provide me with your order id',
'I have a complaint.',
'Please elaborate, your concern',
'How long it will take to receive an order ?',
'An order takes 3-5 Business days to get delivered.',
'Okay Thanks',
'No Problem! Have a Good Day!'


])

trainer = ListTrainer(bot)
trainer.train(list_to_train)


def index (request):
    return render(request, 'blog/index.html')
def specific (request): 
   
   return HttpResponse('list')
def getresponse(request):
    usermessage = request.GET.get('usermessage')
    chatans =   str(bot.get_response(usermessage))
    return HttpResponse (chatans)




    