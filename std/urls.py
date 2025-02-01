from django.urls import path
from . views import *

urlpatterns = [
    path("",home),
    path("home/",home),
    path("std/add-std/",std_add),
    path("std/delete-std/<int:roll>",delete_std),
    path("std/update-std/<int:roll>/",update_std),
    path("std/do-update-std/<int:roll>",do_update_std),

]
