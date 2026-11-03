from django.test import TestCase


class IndexPageTest(TestCase):
    def test_block_list_link_is_on_its_own_line(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h1>Здравствуйте!</h1>')
        self.assertContains(response, '<p class="page-cta">')
