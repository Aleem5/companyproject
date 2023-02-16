from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from department.models import Employee
from department.serializers import EmployeeSerializer


class EmployeeListTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('employee-list')
        self.employee1 = Employee.objects.create(name='Socrates')
        self.employee2 = Employee.objects.create(name='Plato', manager=self.employee1)
        self.employee3 = Employee.objects.create(name='Aristotle', manager=self.employee2)
        self.employee4 = Employee.objects.create(name='CEO', manager=None)

    def test_get_all_employees(self):
        response = self.client.get(self.url)
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], serializer.data)

