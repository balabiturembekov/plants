
from django.db import models


class Home(models.Model):
    ''' Модель первой секций '''
    home_title = models.CharField(verbose_name='Заголовок H1', max_length=100)
    home_description = models.CharField(verbose_name='Дополняющий текст', max_length=300)
    
    def __str__(self):
        return self.home_title
    
    class Meta:
        verbose_name = 'Первая секция'


class About(models.Model):
    ''' Модель секций About '''
    about_title = models.CharField(verbose_name='Заголовок H2', max_length=100)
    about_description = models.CharField(verbose_name='Дополняющий текст', max_length=300)
    
    def __str__(self):
        return self.about_title
    
    class Meta:
        verbose_name = 'Секция о компаний'


class AboutChoose(models.Model):
    ''' Модель Aboutchoose '''
    text = models.CharField(verbose_name='Почему мы?', max_length=500)
    
    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = 'Почему мы?'


class Step(models.Model):
    ''' Модель Steps '''
    step_number = models.CharField(verbose_name='Номер шага', max_length=2)
    step_title = models.CharField(verbose_name='Заголовок', max_length=100)
    step_description = models.CharField(verbose_name='Описание', max_length=200)
    
    def __str__(self):
        return self.step_title
    
    
    class Meta:
        verbose_name = 'Шаги'


class Question(models.Model):
    ''' Модель Questions '''
    question_title = models.CharField(verbose_name='Вопрос?', max_length=200)
    question_description = models.CharField(verbose_name='Ответ', max_length=500)
    
    def __str__(self):
        return self.question_title
    
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class FooterCopy(models.Model):
    ''' Модель Footer '''
    copyright_text = models.CharField(verbose_name='Копирайт текст', max_length=200)
    
    def __str__(self):
        return self.copyright_text
    
    class Meta:
        verbose_name = 'Копирайт текст'

