import json

from rest_framework.test import APITestCase
from django.urls import reverse_lazy

import time


class TestAnnee(APITestCase):
    url = reverse_lazy('is-bissextile')

    # premier test avec en entree une année valide bissextile
    def test_valid_bis(self):
        response = self.client.post(self.url, data={'value': 1900})
        self.assertEquals(response.status_code, 200)
        expected = {
            "isbissextile": False
        }
        self.assertEqual(expected, response.json())

    # second test avec en entree une année valide non bissextile
    def test_valid_not_bis(self):
        response = self.client.post(self.url, data={'value': 2000})
        self.assertEquals(response.status_code, 200)
        expected = {
            "isbissextile": True
        }
        self.assertEqual(expected, response.json())

    def test_float(self):
        response = self.client.post(self.url, data={'value': 182.2})
        self.assertEquals(response.status_code, 400)
        expected = {
            "value": ["A valid integer is required."]
        }
        self.assertEqual(expected, response.json())

    def test_str(self):
        response = self.client.post(self.url, data={'value': "oui"})
        self.assertEquals(response.status_code, 400)
        expected = {
            "value": ["A valid integer is required."]
        }
        self.assertEqual(expected, response.json())


# test pour une range valide


class TestRange(APITestCase):
    url = reverse_lazy('is-bissextile-range')

    def test_valid_range(self):
        response = self.client.post(self.url, data={"first_year": 2000, "second_year": 2010})
        self.assertEquals(response.status_code, 201)
        self.assertEquals(response.data, {'Annees bissextiles': [2000, 2004, 2008]})

# tests pour une range invalide

    def test_invalid_range(self):
        response = self.client.post(self.url, data={"first_year": 2000, "second_year": 1900})
        self.assertEquals(response.status_code, 400)
        self.assertEquals(response.data, {'error': 'Les annees de debut et de fin sont incorrectes.'})

    def test_egal_range(self):
        response = self.client.post(self.url, data={"first_year": 2000, "second_year": 2000})
        self.assertEquals(response.status_code, 400)
        self.assertEquals(response.data, {'error': 'Les annees de debut et de fin sont incorrectes.'})

    def test_str_range(self):
        response = self.client.post(self.url, data={"first_year": "un", "second_year": "deux"})
        self.assertEquals(response.status_code, 400)
        self.assertEquals(response.data, {'error': 'Invalid Serializer'})

    def test_null_range(self):
        response = self.client.post(self.url, data={"first_year": "", "second_year": ""})
        self.assertEquals(response.status_code, 400)
        self.assertEquals(response.data, {'error': 'Invalid Serializer'})


class TestArchive(APITestCase):
    url = reverse_lazy('historique')

    def test_archive(self):
        response = self.client.get(self.url, data={"first_year": 2000, "second_year": 2000, "value": 1900})
        self.assertEquals(response.status_code, 200)

    def test_empty_archive(self):
        response = self.client.get(self.url, data={})
        self.assertEquals(response.status_code, 200)

