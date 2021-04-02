from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import static, status


class RegisterTestCase(APITestCase):

    def setUp(self):
        self.my_url = reverse('create')


    def test_user_create(self):
        data =  {
        "username": "gera.k",
        "email": "gera010393@gmail.com",
        "password": "123456",
        "confirm_password":"123456",
        "dossier":{
            "id": 1,
            "full_name": "Gera Kash",
            "date_birth": "1947-08-24",
            "address": "Prospect Chyngyz Aitmatov",
            "department": "AF",
            "phone": "+971555337032",
            "experience": 5,
            "cars": [
                {
                    "id": 1,
                    "car_model": "Roadster",
                    "car_type": "private",
                    "year": 2020,
                    "country": "USA",
                    "color": "Bur",
                    "mark": "Ford",
                    "wheel_type": "RH",
                    "car_number": "G 0193 E",

                }
            ]
        }
    }
        self.post_data = self.client.post(self.my_url,data,format='json')
        self.assertEqual(self.post_data.status_code,status.HTTP_201_CREATED)


    def test_password_dont_match(self):
        data =  {
        "username": "gera.k",
        "email": "gera010393@gmail.com",
        "password": "pbkdf2_sha256$216000$ZYuMkJSxtpqI$vyt/ybVOP+gKuplOygkLaP8nNYMRPsq1HYMDPrdF/V0=",
        "dossier": {
            "id": 1,
            "image": "/IMG_20181111_203109_403.jpg",
            "full_name": "Gera Kash",
            "date_birth": "1947-08-24",
            "address": "Prospect Chyngyz Aitmatov",
            "department": "AF",
            "phone": "+971555337032",
            "experience": 5,
            "cars": [
                {
                    "id": 1,
                    "car_model": "Roadster",
                    "car_type": "private",
                    "year": 2020,
                    "country": "USA",
                    "color": "Bur",
                    "mark": "Ford",
                    "wheel_type": "RH",
                    "car_number": "G 0193 E",

                }
            ]
        }
    }

        self.post_data = self.client.post(self.my_url,data,format='json')
        self.assertEqual(self.post_data.status_code,status.HTTP_400_BAD_REQUEST)


    def test_full_name(self):
        data = {
            "username": "gera.k",
            "email": "gera010393@gmail.com",
            "password": "pbkdf2_sha256$216000$ZYuMkJSxtpqI$vyt/ybVOP+gKuplOygkLaP8nNYMRPsq1HYMDPrdF/V0=",
            "dossier": {
                "id": 1,
                "image": "/IMG_20181111_203109_403.jpg",
                "full_name": "GeraKash1234567890",
                "date_birth": "1947-08-24",
                "address": "Prospect Chyngyz Aitmatov",
                "department": "AF",
                "phone": "+971555337032",
                "experience": 5,
                "cars": [
                    {
                        "id": 1,
                        "car_model": "Roadster",
                        "car_type": "private",
                        "year": 2020,
                        "country": "USA",
                        "color": "Bur",
                        "mark": "Ford",
                        "wheel_type": "RH",
                        "car_number": "G 0193 E",

                    }
                ]
            }
        }

        self.post_data = self.client.post(self.my_url, data, format='json')
        self.assertEqual(self.post_data.status_code, status.HTTP_400_BAD_REQUEST)

    def test_date_birth(self):
        data = {
            "username": "gera.k",
            "email": "gera010393@gmail.com",
            "password": "pbkdf2_sha256$216000$ZYuMkJSxtpqI$vyt/ybVOP+gKuplOygkLaP8nNYMRPsq1HYMDPrdF/V0=",
            "dossier": {
                "id": 1,
                "image": "/IMG_20181111_203109_403.jpg",
                "full_name": "GeraKash1234567890",
                "date_birth": "199000098776664",
                "address": "Prospect Chyngyz Aitmatov",
                "department": "AF",
                "phone": "+971555337032",
                "experience": 5,
                "cars": [
                    {
                        "id": 1,
                        "car_model": "Roadster",
                        "car_type": "private",
                        "year": 2020,
                        "country": "USA",
                        "color": "Bur",
                        "mark": "Ford",
                        "wheel_type": "RH",
                        "car_number": "G 0193 E",

                    }
                ]
            }
        }

        self.post_data = self.client.post(self.my_url, data, format='json')
        self.assertEqual(self.post_data.status_code, status.HTTP_400_BAD_REQUEST)


    def test_email(self):
        data = {
            "username": "gera.k",
            "email": "gera01hsxnxmksjxlskx,sxls,;xs;x,.s;x.s393@gmcvbnmyopujsaail.com",
            "password": "pbkdf2_sha256$216000$ZYuMkJSxtpqI$vyt/ybVOP+gKuplOygkLaP8nNYMRPsq1HYMDPrdF/V0=",
            "dossier": {
                "id": 1,
                "image": "/IMG_20181111_203109_403.jpg",
                "full_name": "GeraKash1234567890",
                "date_birth": "1947-08-24",
                "address": "Prospect Chyngyz Aitmatov",
                "department": "AF",
                "phone": "+971555337032",
                "experience": 5,
                "cars": [
                    {
                        "id": 1,
                        "car_model": "Roadster",
                        "car_type": "private",
                        "year": 2020,
                        "country": "USA",
                        "color": "Bur",
                        "mark": "Ford",
                        "wheel_type": "RH",
                        "car_number": "G 0193 E",

                    }
                ]
            }
        }

        self.post_data = self.client.post(self.my_url, data, format='json')
        self.assertEqual(self.post_data.status_code, status.HTTP_400_BAD_REQUEST)


    def test_phone(self):
            data = {
                "username": "gera.k",
                "email": "gera01hsxnxmksjxlskx,sxls,;xs;x,.s;x.s393@gmcvbnmyopujsaail.com",
                "password": "pbkdf2_sha256$216000$ZYuMkJSxtpqI$vyt/ybVOP+gKuplOygkLaP8nNYMRPsq1HYMDPrdF/V0=",
                "dossier": {
                    "id": 1,
                    "image": "/IMG_20181111_203109_403.jpg",
                    "full_name": "GeraKash1234567890",
                    "date_birth": "1947-08-24",
                    "address": "Prospect Chyngyz Aitmatov",
                    "department": "AF",
                    "phone": "087363534244242424225525678998765678",
                    "experience": 5,
                    "cars": [
                        {
                            "id": 1,
                            "car_model": "Roadster",
                            "car_type": "private",
                            "year": 2020,
                            "country": "USA",
                            "color": "Bur",
                            "mark": "Ford",
                            "wheel_type": "RH",
                            "car_number": "G 0193 E",

                        }
                    ]
                }
            }

            self.post_data = self.client.post(self.my_url, data, format='json')
            self.assertEqual(self.post_data.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_without_cars(self):
        data = {
            "username": "gera.k",
            "email": "gera010393@gmail.com",
            "password": "123456",
            "confirm_password":"123456",
            "dossier":{
            "id": 1,
            "full_name": "Gera Kash",
            "date_birth": "1947-08-24",
            "address": "Prospect Chyngyz Aitmatov",
            "department": "AF",
            "phone": "+971555337032",
            "experience": 5,
            "cars":[]
            }
        }


        self.post_data = self.client.post(self.my_url, data, format='json')
        self.assertEqual(self.post_data.status_code, status.HTTP_201_CREATED)







