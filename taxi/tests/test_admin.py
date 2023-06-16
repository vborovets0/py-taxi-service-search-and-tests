from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class DriverAdminTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin12345",
        )
        self.client.force_login(self.admin_user)
        self.driver = get_user_model().objects.create_user(
            username="tests",
            password="test1234",
            license_number="TES12345"
        )

    def test_driver_license_listed(self):
        """
        Test that driver's license_number is
        in list_display on driver admin page
        """
        url = reverse("admin:taxi_driver_changelist")
        response = self.client.get(url)

        self.assertContains(response, self.driver.license_number)

    def test_driver_detailed_license_listed(self):
        """
        Test that driver's license_number is
        in list_display on driver detail admin page
        """
        url = reverse("admin:taxi_driver_change", args=[self.driver.id])
        response = self.client.get(url)
        self.assertContains(response, self.driver.license_number)