from xml.etree.ElementInclude import include

from django.urls import path
from .views import index, contato
urlpatterns = [
    path('', index),
    path('contato/', index),

]