from rest_framework import serializers
from .models import Employee
from django.core.exceptions import ValidationError
import re

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

#================================ Validators ====================================
    # Validate email
    def validate_email(self, value):
        if not value.endswith("@company.com"):
            raise serializers.ValidationError(
                "Email must end with @company.com"
            )
        return value


    # Validate salary
    def validate_salary(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Salary must be positive"
            )
        return value


    # Validate emp_id
    def validate_emp_id(self, value):

        pattern = r'^EMP\d+$'

        if not re.match(pattern, value):
            raise serializers.ValidationError(
                "emp_id must be like EMP001"
            )

        return value