from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


# Create your tests here.
class TestDogListCreate(APITestCase):
    def setUp(self):
        self.dogList_url = reverse('dog-list')
        self.dog_data = {
            "name": "Cooper",
            "price": 250000,  # If you give as string "250000" they aumetically typecasing it to numeric value in serializers
            "breed": "Golden Retriever",
            "description": "They are one of the most popular dogs in the world. They have got the cutest face and perrsonalities",
        }
        return super().setUp()

    def test_post_to_dogList(self):
        response = self.client.post(self.dogList_url, self.dog_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_to_dogList(self):
        response = self.client.get(self.dogList_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# After a class executed automatically destroy test database for alias 'default'

class TestDogRetrieveUpdateDestroy(APITestCase):
    def setUp(self):
        self.dogList_url = reverse('dog-list')
        self.dogDetails_url = reverse('dog-details', kwargs={'pk':1})
        self.dog_data = {
            "name": "Cooper",
            "price": 250000,  # If you give as string "250000" they aumetically typecasing it to numeric value in serializers
            "breed": "Golden Retriever",
            "description": "They are one of the most popular dogs in the world. They have got the cutest face and perrsonalities",
        }

        self.new_dog_data = {
            "name": "Charlie",
            "price": 62000,
            "breed": "BullDog",
            "description": "They are one of the most popular dogs in the world. They have got the cutest face and perrsonalities",
        }
        response = self.client.post(self.dogList_url, self.dog_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        return super().setUp()

    def test_get_to_dogDetails(self):
        response = self.client.get(self.dogDetails_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_to_dogDetails(self):
        response = self.client.put(self.dogDetails_url, self.new_dog_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)

    def test_delete_to_dogDetails(self):
        response = self.client.delete(self.dogDetails_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

