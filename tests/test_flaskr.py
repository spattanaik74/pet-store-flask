import unittest
from pet_store_flask.pet.views import app


class FlaskTest(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/pet/all")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get("/pet/all")
        self.assertEqual(response.content_type, "application/json")

    def test_content(self):
        tester = app.test_client(self)
        response = tester.get("/pet/2")
        self.assertTrue([
              {
                "catagory": "mix",
                "id": 2,
                "petname": "atom",
                "status": "available"
              }
            ], response.data)


if __name__ == '__main__':
    unittest.main()
