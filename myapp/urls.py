from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'powerplants', views.PowerPlantViewSet)
router.register(r'units', views.UnitViewSet)
router.register(r'maintenance', views.MaintenanceViewSet)
router.register(r'inspections', views.InspectionViewSet)
router.register(r'staff', views.StaffViewSet)
router.register(r'resources', views.ResourceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
