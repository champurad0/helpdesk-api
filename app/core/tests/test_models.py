"""
Test for models
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    """Test models"""

    def test_create_user_with_email_successful(self):
        """Test creating a user with their store number"""
        email = "store@example.com"
        password = "1234"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normaliezed(self):
        """Test email is normalized for new users"""
        sample_emails = [
            ["test1@Example.com", "test1@example.com"],
            ["Test2@ExamPle.com", "Test2@example.com"],
            ["TEST3@EXAMPLE.COM", "TEST3@example.com"],
            ["test4@example.COM", "test4@example.com"],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, "sample123")
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """test that creating a user without an email raises an error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("", "test123")

    def test_create_superuser(self):
        """testing creating a super user"""
        user = get_user_model().objects.create_superuser(
            "test@example.com", "password1"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
