from django.urls import path,reverse
from .views import Profile,page,form
from django.urls import reverse
app_name='FindApp'
urlpatterns = [
    path('',Profile,name='profile'),
    path('page/<int:pk>/',page,name='page'),
    # path('form/<int:pk>/',form,name='form')
    path('form/',form,name='form')
]