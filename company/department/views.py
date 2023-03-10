from rest_framework import viewsets
from department.models import Employee
from department.serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows employees to be viewed or edited.
    """

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
