from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated

class DaysListView(APIView):
    # permission_classes = (IsAuthenticated, )

    def get(self, request):
        