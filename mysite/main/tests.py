from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Memories
from datetime import datetime
from allauth.socialaccount.models import SocialAccount

class TestViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_add_memory_view(self):
        response = self.client.get(reverse('main:add_memory'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/add_memory.html')

    def test_check_memory_view(self):
        social_account = SocialAccount.objects.create(
            user=self.user, 
            provider='vk',
            uid='test_uid',
            extra_data={'photo_max_orig': 'https://test.com/avatar.jpg'}
        )
        response = self.client.get(reverse('main:check_memory'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/check_memory.html')

    def test_edit_memory_view(self):
        today = datetime.today()
        memory = Memories.objects.create(
            user=self.user, 
            name_memorie='Test Memory', 
            description_memorie='Test Description', 
            date_memorie=today,
            place='Test Place'
        )
        response = self.client.get(reverse('main:edit_memory', args=[memory.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/edit_memory.html')

