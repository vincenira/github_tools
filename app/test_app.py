from routes import appflask
import unittest
class BasicTestCase(unittest.TestCase):
    def test_home(self):
            tester = appflask.test_client()
            response = tester.get('/', content_type='html/text')
            self.assertEqual(response.status_code, 200)

    def test_other(self):
            tester = appflask.test_client()
            response = tester.get('a', content_type='html/text')
            self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
        unittest.main()