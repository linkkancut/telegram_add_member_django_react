from django.shortcuts import render
from .serializers import GroupMemberSerializer
from rest_framework import viewsets
from .models import GroupMember


class GroupMemberView(viewsets.ModelViewSet):
    serializer_class = GroupMemberSerializer
    queryset = GroupMember.objects.all()
