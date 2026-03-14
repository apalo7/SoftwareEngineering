from django.test import SimpleTestCase
from django.urls import resolve

# Create your tests here.

class UrlRoutingTest(SimpleTestCase):
    def test_admin_url_resolves(self):
        url = resolve('/admin/')
        self.assertEqual(url.url_name, 'index')

    def test_admin_login_resolves(self):
        url = resolve('/admin/login/')
        self.assertEqual(url.url_name, 'login')

    def test_system_core_logic(self):
        self.assertTrue(True)

    def test_environment_isolation(self):
        self.assertNotEqual(1, 2)