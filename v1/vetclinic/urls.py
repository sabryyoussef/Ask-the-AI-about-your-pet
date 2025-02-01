from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Ensure no recursive includes or patterns
    # path('some-pattern/', include('some_app.urls')),  # Example
] 