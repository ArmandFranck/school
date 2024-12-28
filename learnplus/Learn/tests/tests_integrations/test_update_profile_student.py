from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from student.models import Student


class UpdateProfilTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="student", password="password")
        self.student = Student.objects.create(user=self.user, bio="Old Bio")
        self.client.login(username="student", password="password")

    def test_update_profil(self):
        response = self.client.post(
            reverse("update_profil"),
            {
                "nom": "NewLastName",
                "prenom": "NewFirstName",
                "email": "newemail@test.com",
                "bio": "New Bio",
            },
        )
        self.student.refresh_from_db()
        self.assertEqual(self.student.bio, "New Bio")
