from django.test import TestCase


class InfoPageTest(TestCase):
    def test_page_renders_with_summary(self):
        response = self.client.get('/info/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Липов')
        self.assertContains(response, '56 лет')
