from django.urls import path
from .views import ShowResult
urlpatterns = [
    
    path('output/',ShowResult.as_view(), name="result")
]