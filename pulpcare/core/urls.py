from django.urls   import  path
from .views import (mainpage, CreateWebsite, websites, getwebsite)

urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('create', CreateWebsite.as_view(), name="Create Website"),
    path('websites', websites, name="Created Websites"),
    path('seewebsites/<slug:id>', getwebsite, name="show website")
]