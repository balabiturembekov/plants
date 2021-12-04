from django.test import TestCase


class HomePageTest(TestCase):
    """ Test Case для домашней страницы """

    def test_home_page_view(self):
        """ Тест: представление домашней страницы возвращает правильный шаблон """
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
