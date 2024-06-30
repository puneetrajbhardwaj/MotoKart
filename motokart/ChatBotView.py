from regex import E
from assets.data.model_refined import *
from django.http import JsonResponse
from django.shortcuts import render
# r=chat('hiii')
def ShowChat(request):
    try:
        return render(request,'Chatbot.html')
    except Exception as e:
        print(e)    
        return render(request,'Chatbot.html')



def ChatBot(request):
    try:
        msg=request.GET['msg']
        result=chat(msg)
        return JsonResponse(result,safe=False)
    except Exception as e:
        print('error:',e)
        return JsonResponse([],safe=False)
 

