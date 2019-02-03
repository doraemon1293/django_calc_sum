from calc_sum import views
from django.urls import path

urlpatterns = [
    path('total/', views.my_view, name="total"),

]
