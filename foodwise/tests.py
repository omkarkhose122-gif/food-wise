from django.test import TestCase
from django.urls import reverse


class ChatbotTests(TestCase):
    def test_chatbot_requires_post(self):
        response = self.client.get(reverse('chatbot'))

        self.assertEqual(response.status_code, 405)

    def test_chatbot_rejects_empty_message(self):
        response = self.client.post(reverse('chatbot'), {'message': '   '})

        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())

    def test_chatbot_returns_calorie_answer(self):
        response = self.client.post(
            reverse('chatbot'),
            {'message': 'How many calories are in rice?'}
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn('Calorie', response.json()['reply'])

    def test_chatbot_returns_protein_answer(self):
        response = self.client.post(
            reverse('chatbot'),
            {'message': 'Suggest protein-rich foods'}
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn('protein', response.json()['reply'].lower())
