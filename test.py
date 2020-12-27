import unittest
import json
import urllib3
from flask_testing import TestCase
from pp.app import *
import base64


class MyTest(unittest.TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        db.session.commit()
        db.create_all()

    def tearDown(self):
        db.session.commit()
        db.drop_all()

    def test_user_post(self):

        client=app.test_client()

        response = client.post(
            '/user',
            data=json.dumps({
                "first_name": "Vitalii",
                "last_name": "Yarmus",
                "birthday": "2002-11-13",
                "email": "qwerty129@gmail.com",
                "phone_number": "+380983057271",
                "password": "qwertyOp"
                }).encode('utf-8'),
            headers={'Content-Type': 'application/json'}
        )
        self.assertEqual(response.status_code, 201)

        json_token= response.data.decode('utf8').replace("'",'"')
        return json.loads(json_token).get('id')

    def test_user_methods(self):

        client=app.test_client()

        user_id = self.test_user_post()
        response = client.get('/user/'+user_id)
        self.assertEqual(response.status_code, 200)

        response = client.post(
            '/user',
            data=json.dumps({
                "first_name": "Vitalii",
                "last_name": "Yarmus",
                "email": "qwerty129@gmail.com",
                "password": "qwertyOp"
                }).encode('utf-8'),
            headers={'Content-Type': 'application/json'}
        )
        self.assertEqual(response.status_code, 409)

        response = client.post('/user')
        self.assertEqual(response.status_code, 400)

        response = client.post(
            '/user',
            data=json.dumps({}).encode('utf-8'),
            headers={'Content-Type': 'application/json'}
        )
        self.assertEqual(response.status_code, 400)

        response = client.post(
            '/user/provisor',
            data=json.dumps({
                "first_name": "Vitaliko",
                "last_name": "Yarmusko",
                "email": "qwerty129@gmail.comko",
                "password": "qwertyOpko"
                }).encode('utf-8'),
            headers={'Content-Type': 'application/json'}
        )
        self.assertEqual(response.status_code, 201)

        response = client.post(
            '/user/provisor',
            data=json.dumps({
                "first_name": "Vitalii",
                "last_name": "Yarmus",
                "email": "qwerty129@gmail.com",
                "password": "qwertyOp"
                }).encode('utf-8'),
            headers={'Content-Type': 'application/json'}
        )
        self.assertEqual(response.status_code, 409)

        response = client.post('/user/provisor')
        self.assertEqual(response.status_code, 400)

        response = client.post(
            '/user/provisor',
            data=json.dumps({}).encode('utf-8'),
            headers={'Content-Type': 'application/json'}
        )
        self.assertEqual(response.status_code, 400)
        
        response = client.get('/user/1')
        self.assertEqual(response.status_code, 400)

        response = client.get('/user/7868d318-486c-11eb-acec-98fa9b4c4e6d')
        self.assertEqual(response.status_code, 404)

    def test_medicine_post(self):

        client=app.test_client()

        response = client.post(
            '/medicine',
            data=json.dumps({
                "name": "smth)",
                "price": 300,
                "amount": 6
            }).encode('utf-8'),
            headers={'Content-Type': 'application/json'}
        )
        self.assertEqual(response.status_code, 201)

        json_token= response.data.decode('utf8').replace("'",'"')
        return json.loads(json_token).get('id') 

    def test_medicine_methods(self):

        client=app.test_client()

        response = client.get('/medicine')
        self.assertEqual(response.status_code, 404)

        medicine_id = self.test_medicine_post()
        response = client.get('/medicine/'+medicine_id)
        self.assertEqual(response.status_code, 200)

        response = client.get('/medicine')
        self.assertEqual(response.status_code, 200)

        response = client.post('/medicine')
        self.assertEqual(response.status_code, 400)

        response = client.post(
            '/medicine',
            data=json.dumps({}).encode('utf-8'),
            headers={'Content-Type': 'application/json'}
        )
        self.assertEqual(response.status_code, 400)
        
        response = client.get('/medicine/1')
        self.assertEqual(response.status_code, 400)

        response = client.get('/medicine/7868d318-486c-11eb-acec-98fa9b4c4e6d')
        self.assertEqual(response.status_code, 404)

        response = client.put(
            '/medicine/'+medicine_id,
            data=json.dumps({
                "name": "smth1)",
                "price": 300,
                "amount": 6
            }).encode('utf-8'),
            headers={'Content-Type': 'application/json'}
        )
        self.assertEqual(response.status_code, 200)

        response = client.put('/medicine/1')
        self.assertEqual(response.status_code, 400)

        response = client.put('/medicine/7868d318-486c-11eb-acec-98fa9b4c4e6d')
        self.assertEqual(response.status_code, 404)

        response = client.delete('/medicine/'+medicine_id)
        self.assertEqual(response.status_code, 200)

        response = client.delete('/medicine/1')
        self.assertEqual(response.status_code, 400)

        response = client.delete('/medicine/7868d318-486c-11eb-acec-98fa9b4c4e6d')
        self.assertEqual(response.status_code, 404)

    def test_buy_methods(self):

        client=app.test_client()

        medicine_id = self.test_medicine_post()
        response = client.post(
            '/buy',
            data=json.dumps({
               "medicine_id": medicine_id,
               "amount": 4
            }).encode('utf-8'),
            headers={'Content-Type': 'application/json'}
        )
        print(response.data)
        self.assertEqual(response.status_code, 201)
        
        user_id = self.test_user_post()
        medicine_id = self.test_medicine_post()
        response = client.post(
            '/buy',
            data=json.dumps({
               "user_id": user_id,
               "medicine_id": medicine_id,
               "amount": 4
            }).encode('utf-8'),
            headers={'Content-Type': 'application/json'}
        )
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
