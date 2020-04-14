from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    #string.split() - string을 공백을 기준으로 나누어 리스트를 생성한다.
    words = text.split()
    word_dictionary = {}
    #<단어> : 몇번, <단어> : 몇번
    for word in words:
        if word in word_dictionary:
            #increase
            word_dictionary[word] += 1
        else:
            #add to dictionary
            word_dictionary[word] = 1

    #총 단어 수 = len(words)
    return render(request, 'result.html', {'full': text, 'total': len(words), 'dictionary' : word_dictionary.items()})
    