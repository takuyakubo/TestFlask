from unittest import TestCase


class ServerTestCase(TestCase):
    def setUp(self):
        super().setUp()
        from server import app
        self.app = app

    def test_not_found(self):
        with self.app.test_client() as c:
            rv = c.get('/something')
        self.assertEqual(rv.status_code, 404)

    def test_get_root(self):
        with self.app.test_client() as c:
            rv = c.get('/')
        self.assertEqual(rv.status_code, 200)
        ret_data = rv.get_data().decode('utf-8')
        self.assertEqual('Hello!', ret_data)
