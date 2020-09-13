from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='news'),
    # path('structure/<int:branch_id>/', view_branch(), name="view_branch"),
]
