from .views import CerdaView, ControlCeloView
from django.urls import path

urlpatterns = [
    path("cerda/", CerdaView.as_view(), name="cerda-list"),
    path("cerda/<int:pk>/", CerdaView.as_view(), name="cerdas-detail"),
    path("contro-celo/", ControlCeloView.as_view(), name="celo-list"),
    path("control-celo/<int:pk>/", ControlCeloView.as_view(), name="celo-detail"),
]