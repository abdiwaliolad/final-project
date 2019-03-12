from django.urls import path
from . import views

urlparttens=[

    path('gettracks/',views.gettracks, name='gettracks')

]