from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated

from .models import Days
from .serializers.populated import PopulatedDaysSerializer
from .serializers.common import DaysSerializer

class DaysListView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        is_staff = request.user.is_staff
        is_user = request.user.id
        if is_staff:
            days = Days.objects.all()
        else: 
            days = Days.objects.filter(user=request.user.id)
        serialized_days = PopulatedDaysSerializer(days, many=True)
        return Response(serialized_days.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        request.data['user'] = request.user.id
        day_to_add = DaysSerializer(data=request.data)
        try:
            day_to_add.is_valid()
            day_to_add.save()
            return Response(day_to_add.data, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            res = {
              "detail": str(e)
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({"detail": "Unprocessable Entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
  
class DaysDetailView(APIView):
    permission_classes = (IsAuthenticated, )

    def get_day(self,pk):
        try:
            return Days.objects.get(pk=pk)
        except:
            raise NotFound(detail="Cannot Find the Day")
    
    def get(self,pk):
        try:
            days = self.get_day(pk=pk)
            serialized_day = PopulatedDaysSerializer(days)
            return Response(serialized_day.data, status=status.HTTP_200_OK)
        except Days.DoesNotExist:
            raise NotFound(detail="Cannot find Day")
    
    def put(self,request,pk):
        day_to_edit = self.get_day(pk=pk)
        is_user = request.user.id
        if not is_user:
            raise PermissionDenied()
        updated_day = DaysSerializer(day_to_edit, data=request.data)
        try:
            updated_day.is_valid()
            updated_day.save()
            day = self.get_day(pk=pk)
            serialized_day = PopulatedDaysSerializer(day)
            return Response(serialized_day.data, status=status.HTTP_200_OK)
        except AssertionError as e:
            return Response({"detail":str(e)},  status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            res = {
              "detail": "Unprocessable Entity"
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    def delete(self, request, pk):
        try:
            day_to_delete = Days.objects.get(pk=pk)
            if day_to_delete != request.user:
                raise PermissionDenied()
            day_to_delete.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Days.DoesNotExist:
            raise NotFound(detail="Day not found") 

        

