from django.urls import path
from . import views

urlpatterns = [
    path('sites/', views.site_index, name="site_index"),
    path('sites/add/', views.add_site, name="add_site"),
    path('sites/<int:site_id>/update/', views.update_site, name="update_site"),
    path('sites/<int:site_id>/', views.get_site, name="get_site"),
    path('sessions/', views.session_index, name="session_index"),
    path('sessions/add/', views.add_session, name="add_session"),
    path('sessions/<int:session_id>/update/', views.update_session, name="update_session"),
    path('sessions/<int:session_id>/', views.get_session, name="get_session"),
    path('profiles/', views.profile_index, name="profile_index"),
    path('profiles/<int:profile_id>/update/', views.update_profile, name="update_profile"),
    path('profiles/<int:profile_id>/', views.get_profile, name="get_profile"),
    path('signup/', views.sign_up, name="sign_up"),
    path('organizations/<int:organization_id>/', views.get_organization, name="get_organization"),
]