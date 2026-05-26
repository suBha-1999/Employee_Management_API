from django.urls import path, include
from .  import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('employees', views.EmployeeViewSet, basename='EmployeeViewSet')

urlpatterns = [
    #=====================APIView url ===========================================================
    # path('employee/', views.EmployeeView.as_view(), name='EmployeeView'),
    # path('employee/<int:pk>/', views.EmployeeDetailView.as_view(), name='EmployeeDetail'),
    # ===========================================================================================

    # ============================= ViewSet =====================================================
    path('', include(router.urls))
]
