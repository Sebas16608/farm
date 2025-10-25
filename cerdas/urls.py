from django.urls import path
from .views import CerdaView, CeloView

urlpatterns = [
    path("cerdas/", CerdaView.as_view(), name="Cerdas-list"),
    path("cerdas/<int:pk>/", CerdaView.as_view(), name="Cerdas-detail"),
    path("celo/", CeloView.as_view(), name="celos-list"),
    path("celo/<int:pk>/", CeloView.as_view(), name="celo-detail")
]