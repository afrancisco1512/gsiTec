from django.conf.urls import url
import views
urlpatterns = [
    url(r'^CrearTicket/', views.CrearTicket),
    url(r'^', views.home),
]