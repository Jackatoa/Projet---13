from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse
from django.core import mail


class HomePageTests(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_home_page_reverse(self):
        response = self.client.get(reverse('blog-home'))
        self.assertEquals(response.status_code, 200)

    def test_home_template(self):
        response = self.client.get(reverse('blog-home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/accueil.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, 'Le rendez-vous annuel')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'construction')
    
    def test_gestion_redirect(self):
        response = self.client.get('/gestion', follow=True)
        self.assertContains(response, 'Formulaire')
    
    def test_gestion_redirect_login(self):
        response = self.client.get('/gestion', follow=True)
        self.assertNotContains(response, 'Gérer')

    def test_gestion_require_login(self):
        response = self.client.get('/gestion')
        self.assertEquals(response.status_code, 301)

class EmailTest(TestCase):
    def test_send_email(self):
        mail.send_mail(
            'Subject here', 'Here is the message.',
            'from@example.com', ['to@example.com'],
            fail_silently=False,
        )
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Subject here')    