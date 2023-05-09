from django.urls import path

from ads.views.cat import CatDetailView, CatListView, CatCreateView, CatUpdateView, CatDeleteView

urlpatterns = [
    path('', CatListView.as_view()),
    path('<int:pk>/', CatDetailView.as_view()),
    path('create/', CatCreateView.as_view()),
    path('update/<int:pk>/', CatUpdateView.as_view()),
    path('delete/<int:pk>/', CatDeleteView.as_view()),
]
