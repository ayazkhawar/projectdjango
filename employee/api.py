from rest_framework import generics
from rest_framework.response import Response
from .serializer import EmployeeSerializer
from .models import Employee
from rest_framework.permissions import IsAuthenticated

class EmployeeCreateApi(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeApi(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeUpdateApi(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDeleteApi(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
