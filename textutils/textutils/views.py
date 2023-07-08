from django.http import HttpResponse 
from django.shortcuts import render

# views in url django

# def index(request):
#     return HttpResponse('''<h1>Hello Pritam</h1> <a href="https://github.com/somuthehunter"> Pritam Dutta Github link </a> <br/> 
#                         <a href="https://www.google.com/"> link to go in Google </a>
#                         <br/><a href="https://www.youtube.com/channel/UCax2yH6ZnQpOba2y4j6ehHA"> Pritam Dutta Youtube link </a>
#                         <br/><a href="https://www.facebook.com/"> Pritam Dutta facebook link </a>''')
   

# def about(request):
#     return HttpResponse('<h1>About Pritam Dutta </h1>')


# pipeline in django 


# def index(request):
#     return HttpResponse('''<h1>Home</h1>  <button> <a href="http://127.0.0.1:8000/removepunc">Remove Punctuation</a></button>
#                         <br/><br/><button> <a href="http://127.0.0.1:8000/capfirst">Capitalize first word</a></button>
#                         <br/><br/><button> <a href="http://127.0.0.1:8000/newlineremove"> remove new lines</a></button>
#                         <br/><br/><button> <a href="http://127.0.0.1:8000/spaceremove"> Remove Space</a></button>
#                         <br/><br/><button> <a href="http://127.0.0.1:8000/charcount"> Count character</a></button>''')

# def removepunc(request):
#     return HttpResponse('''Remove Punctuation <button> <a href="http://127.0.0.1:8000"> Back </a></button>''')

# def capfirst(request):
#     return HttpResponse("Capitalize first word")

# def newlineremove(request):
#     return HttpResponse("Remove new lines")

# def spaceremove(request):
#     return HttpResponse("space remover")

# def charcount(request):
#     return HttpResponse("character count")


# using templates 

def index(request):
    params = { 'name':'pritam','place':'Mars'}
    return render(request,'index.html',params)

def analyze(request):
    #get the text
    djtext=request.POST.get('text','default')#for post request
    #check the checkbox
    removepunc =request.POST.get('removepunc','off')
    fullcaps =request.POST.get('fullcaps','off')
    newlineremover =request.POST.get('newlineremover','off')
    spaceremover =request.POST.get('spaceremover','off')
    charcount =request.POST.get('charcount','off')
    # analyzed = djtext
    #check if the checkbox is on 
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if(spaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            # It is for if a extraspace is in the last of the string
            if char == djtext[-1]:
                    if not(djtext[index] == " "):
                        analyzed = analyzed + char

            elif not(djtext[index] == " " and djtext[index+1]==" "):                        
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
    
    

    
    if(removepunc != "on" and newlineremover!="on" and spaceremover!="on" and fullcaps!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)

    #     return HttpResponse("Error! please check the checkbox")
    # return HttpResponse('''Remove Punctuation <button> <a href="http://127.0.0.1:8000"> Back </a></button>''')
    return render(request,'analyze.html',params)
def about(request):
    return render(request,'about.html')