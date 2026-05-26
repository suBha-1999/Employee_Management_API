from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins, generics, viewsets
from .pagination import CustomPagination, CustomLimitOffsetPagination


# Create your views here.

#-----============ CLASS BASED VIEWS/ APIViews ==============------------
'''
class EmployeeView(APIView):
    def get(self, request):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EmployeeDetailView(APIView):
    def get(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        employee.delete()
'''

#====================== Mixins ====================
'''
class EmployeeView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.post(request)
    
class EmployeeDetailView(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)
'''

# ========================== Generics Views =============================
'''
class EmployeeView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'
'''

#====================Viewset ======================
'''
class EmployeeViewSet(viewsets.ViewSet):
    def list(self, request):
        students = Employee.objects.all()
        serializer = EmployeeSerializer(students, many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = EmployeeSerializer(Employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk):
        student = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk):
        student = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(student, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = get_object_or_404(Employee, pk=pk)
        student.delete()
        return Response({'massage': 'Deleted'}, status=status.HTTP_204_NO_CONTENT)
'''
# -------------------Pagination impliment in ModelViewSet ------------------------
class EmployeeViewSet(viewsets.ModelViewSet):
    # queryset = Employee.objects.all()

    #================Pagination=======================
    serializer_class = EmployeeSerializer
    # pagination_class = CustomPagination
    pagination_class = CustomLimitOffsetPagination
    #====================================================

    #=====================Filtering==========================
    def get_queryset(self):

        queryset = Employee.objects.all()

        # --------------------------------
        # Filter by designation
        # --------------------------------
        designation = self.request.query_params.get('designation')
        if designation:
            queryset = queryset.filter(
                designation__iexact=designation
            )

        # --------------------------------
        # Filter by employee name
        # --------------------------------
        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(
                name__icontains=name
            )

        # --------------------------------
        # Filter by emp_id range
        # --------------------------------
        emp_id_min = self.request.query_params.get('emp_id_min')
        emp_id_max = self.request.query_params.get('emp_id_max')
        if emp_id_min and emp_id_max:
            queryset = queryset.filter(
                emp_id__gte=emp_id_min,
                emp_id__lte=emp_id_max
            )

        # --------------------------------
        # Filter by salary range
        # --------------------------------
        salary_min = self.request.query_params.get('salary_min')
        salary_max = self.request.query_params.get('salary_max')
        if salary_min and salary_max:
            queryset = queryset.filter(
                salary__gte=salary_min,
                salary__lte=salary_max
            )
        return queryset