from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("<int:product_id>/", views.detail, name="detail"),
    path("<int:product_id>/results", views.results, name="results"),
    path("<int:product_id>/sale/", views.sale, name="sale"),
]
