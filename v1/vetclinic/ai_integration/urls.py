from django.urls import path
from . import views
from .views import symptom_checker, ai_chat


app_name = "ai_integration"  # This registers the namespace

urlpatterns = [
    # Remove the self-inclusion to prevent recursion
    # path('ai/', include('ai_integration.urls')),
    path('symptoms-checker/', symptom_checker, name='symptoms_checker'),
    path('chat/', ai_chat, name='ai_chat'),
]