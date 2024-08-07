from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('search', views.search, name='search'),
    # path('search_results', views.search_results, name='search_results'),
    # path('search_results/<int:id>', views.search_results, name='search_results'),
    # path('search_results/<int:id>/delete', views.delete, name='delete'),
    # path('search_results/<int:id>/edit', views.edit, name='edit'),
]