from department.models import Employee
from rest_framework import serializers


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    # manager_name = serializers.CharField(source='manager.name', read_only=True)
    manager_name = serializers.PrimaryKeyRelatedField(allow_null=True, queryset=Employee.objects.all())
    # do so, to get `manager_name` field, even for CEO, who dont have manager`

    class Meta:
        model = Employee
        fields = ['emp_id', 'name', 'manager_name']