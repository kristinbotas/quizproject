from django.shortcuts import render

def startpage(request):
		return render(request, "startpage.html")

def startpage(request):
		return render(request, "startpage.html")

def quiz(request, quiz_number):
		return render(request, "quiz.html")

def question(request, quiz_number, question_number):
		return render(request, "question.html")		

def completed(request, quiz_number):
		return render(request, "completed.html")					

# Create your views here.
