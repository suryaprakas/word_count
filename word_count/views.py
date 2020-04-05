from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html', {'Name':"This is surya!!"})

def about(request):
    print('Hello')
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split()
    word_dictionary = {}
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    print(word_dictionary)
    sorted_res = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)
    print(sorted_res)
    return render(request, 'count.html',{'fulltext':fulltext,'count':len(word_list), 'word_dictionary':sorted_res})