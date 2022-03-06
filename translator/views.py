from django.shortcuts import render
from . import translate_grammar_check


def about_view(request):
    return render(request, 'about.html')

def translator_view(request):
    if request.method =="POST":
        to_translate = request.POST['sentence']
        chosen_language = request.POST['language_selection']
        if to_translate == '':
            return render(request, 'translate.html')
        else:
            translated = translate_grammar_check.translating(to_translate, chosen_language )
            return render(request,'translate.html',{"translated_word" : translated, "original": to_translate})
    else:
        return render(request, 'translate.html')

def grammar_corr(request):
    if request.method == "POST":
        to_check = request.POST['sentence']
        if to_check == '':
            return render(request,'grammar_check.html')
        else:
            output = translate_grammar_check.grammar_spelling_check(to_check)
            return render(request, 'grammar_check.html', {"corrected":output, "old_sentence":to_check})
    else:
        return render(request,'grammar_check.html')