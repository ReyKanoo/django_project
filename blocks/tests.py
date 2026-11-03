import warnings

from django.contrib.auth.models import User
from django.core.paginator import UnorderedObjectListWarning
from django.test import TestCase

from .models import block


class InfoPageTest(TestCase):
    def test_page_renders_with_summary(self):
        response = self.client.get('/info/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Липов')
        self.assertContains(response, '56 лет')


class BlockListTest(TestCase):
    def test_block_list_pagination_is_ordered(self):
        user = User.objects.create_user(username='tester', password='pass12345')
        self.client.force_login(user)
        for i in range(4):
            block.objects.create(title=f'Задание {i + 1}', description='проверка пагинации')

        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter('always')
            response = self.client.get('/block/')

        self.assertEqual(response.status_code, 200)
        self.assertFalse(
            any(issubclass(w.category, UnorderedObjectListWarning) for w in caught),
            'Пагинация без порядка — добавь order_by в QuerySet',
        )
