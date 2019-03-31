from django.conf.urls import url
from .views import SoonView
urlpatterns = [

    url('', view=SoonView.as_view(),name='soon'),
]