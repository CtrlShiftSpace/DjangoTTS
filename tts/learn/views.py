from django.shortcuts import render

from learn.models import EnglishWord

# Create your views here.
def home(request):

    eng_words = EnglishWord.objects.all()
    context = {
        'eng_words': eng_words
    }
    return render(request, 'learn/home.html', context=context)