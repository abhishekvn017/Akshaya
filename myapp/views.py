from rest_framework import viewsets
from .models import PowerPlant, Unit, Maintenance, Inspection, Staff, Resource
from .serializers import PowerPlantSerializer, UnitSerializer, MaintenanceSerializer, InspectionSerializer, StaffSerializer, ResourceSerializer

class PowerPlantViewSet(viewsets.ModelViewSet):
    queryset = PowerPlant.objects.all()
    serializer_class = PowerPlantSerializer

class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

class MaintenanceViewSet(viewsets.ModelViewSet):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer

class InspectionViewSet(viewsets.ModelViewSet):
    queryset = Inspection.objects.all()
    serializer_class = InspectionSerializer

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
