from django.shortcuts import render

from .models import FooterCopy, Home, About, AboutChoose, Step, Question


def home_page(request):
    context = get_context_data()
    return render(request, 'home.html', context)


def get_context_data():
    """ Получение данных из моделей """
    home_data = Home.objects.first()
    about_data = About.objects.first()
    about_choose = AboutChoose.objects.all()
    steps = Step.objects.all()
    questions = Question.objects.all()
    footer_text = FooterCopy.objects.all()

    context = {
        'home': home_data,
        'about': about_data,
        'about_choose': about_choose,
        'steps': steps,
        'questions': questions,
        'footer_text': footer_text
    }
    return context
