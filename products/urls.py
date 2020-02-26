from django.conf.urls import url, include
from .views import all_products, all_massage, all_packages, all_face


urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^massage/$', all_massage, name='products'),
    url(r'^packages/$', all_packages, name='products'),
    url(r'^face/$', all_face, name='products')
]