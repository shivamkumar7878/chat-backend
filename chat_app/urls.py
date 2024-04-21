from django.urls import path
from .views import ChatLoginView, ChatSignupView

urlpatterns = [
    path("signup", ChatSignupView.as_view(), name="signup"),
    path("signin", ChatLoginView.as_view(), name="signin"),
]
