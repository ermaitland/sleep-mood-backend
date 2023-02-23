from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from django.db import IntegrityError

from .models import Mood
from .serializers.common import MoodSerializer

class MoodListView(APIView):

    def get(self, _request):
        mood = Mood.objects.all()
        serialized_moods = MoodSerializer(mood, many=True)
        return Response(serialized_moods.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        mood_to_add = MoodSerializer(data=request.data)
        try: 
            mood_to_add.is_valid()
            mood_to_add.save()
            return Response(mood_to_add.data, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            res = {
              "detail": str(e)
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({"detail": "Unprocessable entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)