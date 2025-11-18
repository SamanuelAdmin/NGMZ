from django.urls import path

from . import views


urlpatterns = [
    path('', views.index_view, name='index'),
    path('category/', views.category_view, name='category'),
    path('category/<slug:category>/', views.category_view, name='category'),
    path('product/<slug:tag>/', views.product_view, name='product'),
    path('about/', views.about_view, name='about'),
    path('contacts/', views.contacts_view, name='contacts'),
    path('changelang/<slug:lang_code>', views.change_language, name='set_language'),
]


