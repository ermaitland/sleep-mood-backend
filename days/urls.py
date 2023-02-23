from django.urls import path
from .views import DaysDetailView, DaysListView

urlpatterns = [
  path('', DaysListView.as_view()),
  path('pk/', DaysDetailView.as_view())
]