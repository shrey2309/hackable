from django.urls import path
from .views import safe, unsafe, sqlsafe, sqlunsafe

urlpatterns = [

    path('', safe),
    path('unsafe', unsafe),
    path('s-sql-inection', sqlsafe),
    path('u-sql-inection', sqlunsafe)
]
#check