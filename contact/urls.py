from django.urls import path
from contact import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'contact'

urlpatterns = [
    path('<int:contact_id>/', views.contact, name='contact'),  # type:ignore
    path('search/', views.search, name='search'),  # type:ignore
    path('', views.index, name='index'),  # type:ignore
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
