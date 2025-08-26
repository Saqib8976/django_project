from django.shortcuts import render , redirect
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.

def analyze_txt(request):
    # getting the text from analyze_text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capitalized = request.POST.get('capitalized', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount' , 'off')

    # analyzing text
    analyze = ""
    punctuations = """!"#$%&'()*+,-./:;<=>?@[\]^_{|}~`"""

    if removepunc == 'on' and capitalized == 'on' and newlineremover == 'on':
        analyze=''
        for char in djtext:
            if char not in punctuations and char != '\n':
                analyze += char.upper()
        params = {'purpose': 'punctuation and newline removed with character upper case ', "analyzed_text": analyze}
        djtext = analyze
        # return render(request, 'analyze_text.html', params)

    if removepunc == 'on':
        for char in djtext:
            if char not in punctuations:
                analyze += char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyze}
        djtext = analyze
        # return render(request, 'analyze_text.html', params)

    if capitalized == 'on':
        analyze = ''
        for char in djtext:
            analyze += char.upper()
        params = {'purpose': 'capitalize text', 'analyzed_text': analyze}
        djtext = analyze
        # return render(request,'analyze_text.html', params)

    if newlineremover == 'on':
        analyze = ''
        for char in djtext:
            if char != '\n' and char != '\r':
                analyze += char
        params = {'purpose': 'newline removed', 'analyzed_text': analyze}
        djtext = analyze
        # return render(request,'analyze_text.html', params)

    if extraspaceremover == 'on':
        analyze = ''
        for index , char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyze += char
        params = {'purpose': 'extraspace removed', 'analyzed_text': analyze}
        djtext = analyze
        # return render(request,'analyze_text.html', params)

    if charcount == 'on':
        count = 0
        for char in djtext:
            if char != ' ':
                count += 1
        params = {'purpose': 'character count', "statement": "\n character count is ", "count": count , "analyzed_text": analyze }

    # use this if want to use new page
    # if removepunc != 'on' and capitalized != 'on' and newlineremover != 'on' and charcount != 'on' and extraspaceremover != 'on':
    #     return render(request,"Error.html",{'error': 'please on atleast one toggle...!'})
    #     return redirect("/")

    if all(v != 'on' for v in [removepunc, capitalized, newlineremover, charcount, extraspaceremover]):
        messages.error(request, "Please turn on at least one toggle!")
        return redirect("/")

    return render(request,'analyze_text.html', params)








    # else:
    #     params = {'purpose': 'Punctuations', 'analyzed_text': djtext}
    #     return render(request, 'analyze_text.html',params)

