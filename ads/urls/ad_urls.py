from django.urls import path

from ads.views import AdDetailView, AdUploadImageView, AdListView, AdCreateView

urlpatterns = [
    path('', AdListView.as_view()),
    path('<int:pk>', AdDetailView.as_view()),
    path('create/', AdCreateView.as_view()),
    path('<int:pk>/upload_image', AdUploadImageView.as_view())
]
