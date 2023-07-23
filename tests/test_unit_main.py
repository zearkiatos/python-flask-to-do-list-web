from flask_testing import TestCase
from flask import current_app, url_for
from main import app


class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    def test_app_exists(self):
        self.assertIsNotNone(current_app)

    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_index_get(self):
        response = self.client.get(url_for('index'))

        self.assert_redirects(response)

    def test_home_get(self):
        response = self.client.get(url_for('home'))

        self.assert200(response)
