from flask_testing import TestCase
from flask import url_for
from app import create_app


class AuthTest(TestCase):
    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    def test_auth_blueprint_exists(self):
        self.assertIn('auth', self.app.blueprints)

    def test_auth_login_get(self):
        response = self.client.get(url_for('auth.login'))

        self.assert200(response)

    def test_auth_login_template(self):
        response = self.client.get(url_for('auth.login'))

        self.assert200(response)
        self.assertTemplateUsed('login.html')

    def test_login_post(self):
        response = self.client.post(url_for('auth.login'))

        self.assertTrue(response.status_code, 405)

    def test_auth_login_post(self):
        fake_form = {
            'username': 'fake',
            'password': 'fake-password'
        }

        response = self.client.post(url_for('auth.login'), data=fake_form)

        self.assertRedirects(response, url_for('auth.login'))
