from django.contrib import admin
from django.urls import path
import api.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_all', api.views.GetAll.as_view()),
    path('get_by_id/<institution_id>', api.views.GetById.as_view()),
    path('search', api.views.Search.as_view()),
    path('create', api.views.Create.as_view()),
    path('delete/<institution_id>', api.views.Delete.as_view()),
    path('update/<institution_id>', api.views.Update.as_view()),
]
