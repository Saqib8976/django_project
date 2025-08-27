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
    charcount = request.POST.get('charcount', 'off')
    numberemover = request.POST.get('numberemover', 'off')

    # analyzing text
    analyze = ""
    punctuations = """!"#$%&'()*+,-./:;<=>?@[\]^_{|}~`"""

    # frome here to line 72 code is optional , if you want to pass dynemic value which is params
    # according to toggle on then do this but its not complete code
    # because if user turn on all toggle except one which is remove punc then user not get the param value according to toggle on
    if all(v == 'on' for v in [removepunc, capitalized, newlineremover, extraspaceremover, charcount, numberemover]):

        analyze = ''
        count = 0
        numbers = '0123456789'

        # Loop through each character in the text
        for i, char in enumerate(djtext):
            # Skip punctuation, newlines, and carriage returns
            if char not in punctuations and char not in ['\n', '\r'] and char not in numbers:
                # it remove extra spaces
                if not (djtext[i] == " " and djtext[i+1] == " "):
                    analyze += char.upper()  # Convert to uppercase and add to result
            if char != ' ':
                count +=1

        # Prepare the result to send to the template
        params = {'purpose': 'Removed punctuation, newlines, extra spaces, with uppercase', 'analyzed_text': analyze,
                  'statement': "\n your character count is", count:"count"}
        return render(request, 'analyze_text.html', params)

    if all(v == 'on' for v in [removepunc, capitalized, newlineremover, extraspaceremover, charcount]):

        analyze = ''
        count = 0

        # Loop through each character in the text
        for i, char in enumerate(djtext):
            # Skip punctuation, newlines, and carriage returns
            if char not in punctuations and char not in ['\n', '\r']:
                # it remove extra spaces
                if not (djtext[i] == " " and djtext[i+1] == " "):
                    analyze += char.upper()  # Convert to uppercase and add to result
            if char != ' ':
                count +=1

        # Prepare the result to send to the template
        params = {'purpose': 'Removed punctuation, newlines, extra spaces, with uppercase', 'analyzed_text': analyze,
                  'statement': "\n your character count is", count:"count"}
        return render(request, 'analyze_text.html', params)

    if all(v == 'on' for v in [removepunc, capitalized, newlineremover, extraspaceremover]):

        analyze = ''

        # Loop through each character in the text
        for i, char in enumerate(djtext):
            # Skip punctuation, newlines, and carriage returns
            if char not in punctuations and char not in ['\n', '\r']:
                # it remove extra spaces
                if not (djtext[i] == " " and djtext[i+1] == " "):
                    analyze += char.upper()  # Convert to uppercase and add to result

        # Prepare the result to send to the template
        params = {'purpose': 'Removed punctuation, newlines, extra spaces, with uppercase', 'analyzed_text': analyze}
        return render(request, 'analyze_text.html', params)

    if removepunc == 'on' and capitalized == 'on' and newlineremover == 'on':
        analyze = ''
        for char in djtext:
            if char not in punctuations and char not in ['\n', '\r']:
                analyze += char.upper()
        params = {'purpose': 'punctuation and newline removed with character upper case ', "analyzed_text": analyze}
        return render(request, 'analyze_text.html', params)

    if removepunc == 'on' and capitalized == 'on':
        analyze=''
        for char in djtext:
            if char not in punctuations:
                analyze += char.upper()
        params = {'purpose': 'removed punctuation with character upper case ', "analyzed_text": analyze}
        return render(request, 'analyze_text.html', params)

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
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyze += char
        params = {'purpose': 'extraspace removed', 'analyzed_text': analyze}
        djtext = analyze
        # return render(request,'analyze_text.html', params)

    if numberemover == 'on':
        analyze = ''
        numbers = '0123456789'
        for char in djtext:
            if char not in numbers:
                analyze += char

        params = {'purpose': 'number removed', 'analyzed_text': analyze}
        djtext = analyze

    if charcount == 'on':
        count = 0
        analyze = ''
        for char in djtext:
            analyze += char
            if char != ' ':
                count += 1

        params = {'purpose': 'character count', "statement": "\n character count is", "count": count, "analyzed_text": analyze}
        djtext = analyze
        # return render(request, 'analyze_text.html', params)

    # use this if want to use new page to pass message or Error
    # if removepunc != 'on' and capitalized != 'on' and newlineremover != 'on' and charcount != 'on' and extraspaceremover != 'on':
    #     return render(request,"Error.html",{'error': 'please on atleast one toggle...!'})
    #     return redirect("/")

    # here we are going to pass message on same page according to conditions
    if all(v != 'on' for v in [removepunc, capitalized, newlineremover, charcount, extraspaceremover, numberemover]):
        messages.error(request, "Please turn on at least one toggle!")
        return redirect("/")

    return render(request, 'analyze_text.html', params)

