from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import viewsets

# Model View Set 
class EmployeeModelViewSet(viewsets.ModelViewSet):
	queryset=Employee.objects.all()
	serializer_class=EmployeeSerializer

# Read Only Model View Set
class EmployeeReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
	queryset=Employee.objects.all()
	serializer_class=EmployeeSerializer
