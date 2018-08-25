from django.conf.urls import url
from notes import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^login/$', auth_views.login, name="login"),
    url(r'^logout/$', auth_views.logout, {'next_page': '/notes/login'}, name="logout"),
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^new_note/',views.new_note,name="new_note"),
    url(r'^create_note/',views.create_note,name="create_note"),
    url(r'manage_all_notes',views.manage_all_notes,name="manage_all_notes"),
    url(r'delete/(?P<id>\d+)',views.delete,name="delete"),
    url(r'update/(?P<id>\d+)',views.update,name="update")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)