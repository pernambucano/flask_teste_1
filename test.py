from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

    # Make sure everything is ok
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_page_load(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue('Please login' in response.data)

    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post('/login',
                               data=dict(username="admin", password="admin"),
                               follow_redirects=True
                               )
        self.assertIn('You were just logged in!', response.data)

    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post('/login',
                               data=dict(username="wrong", password="wrong"),
                               follow_redirects=True)
        self.assertIn('Invalid credentials. Please try again.', response.data)

    def test_logout(self):
        tester = app.test_client(self)
        tester.post('/login',
                    data=dict(username="admin", password="admin"),
                    follow_redirects=True)
        response = tester.get('/logout', follow_redirects=True)
        self.assertIn('You were just logged out!', response.data)

    def test_main_route_requires_login(self):
        tester = app.test_client(self)
        response = tester.get('/', follow_redirects=True)
        self.assertIn('You need to login first', response.data)

    def test_logout_requires_login(self):
        tester = app.test_client(self)
        response = tester.get('/logout', follow_redirects=True)
        self.assertIn('You need to login first', response.data)

    def test_post_show_up(self):
        tester = app.test_client(self)
        response = tester.post('/login',
                               data=dict(username="admin",
                                         password="admin"),
                               follow_redirects=True)
        self.assertIn(b'Good', response.data)

if __name__ == '__main__':
    unittest.main()
