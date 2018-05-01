from django.conf.urls import include, url

app_name="controle_backend"

urlpatterns = (

    url(r'^controle-list/',include('controle.urls',namespace='controle')),



)


