import unittest
import myapp

class TestMyapp(unittest.TestCase):

    def setUp(self):
        myapp.app.testing = True
        self.app = myapp.app.test_client()

    def test_home(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        #self.assertEqual(rv.data, b'Hello World!\n')

    def test_about(self):
        rv = self.app.get('/about')
        self.assertEqual(rv.status, '200 OK')
        #self.assertEqual(rv.data, b'Hello World!\n')

    def test_name(self):
        #name = 'alex'
        #rv = self.app.get(f'/{name}')
        rv = self.app.get('/alex')
        self.assertEqual(rv.status, '200 OK')
        #self.assertIn(bytearray(f"{name}", 'utf-8'), rv.data)

if __name__ == '__main__':
    unittest.main()