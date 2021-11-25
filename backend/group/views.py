from django.shortcuts import render
from .serializers import GroupSerializer
from rest_framework import viewsets
from .models import Group


class GroupView(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
