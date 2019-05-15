from django.urls import path
from . import views
from . views import CriminalCreateView, CriminalDeleteView, CriminalListView, CriminalUpdateView, CriminalDetailView

app_name = 'judiciary'

urlpatterns = [
    path('add_criminal/', CriminalCreateView.as_view(), name='add_criminal'),
    path('', CriminalListView.as_view(), name='index'),
    path('<int:pk>/delete/', CriminalDeleteView.as_view(), name='delete'),
    path('<int:pk>/update/', CriminalUpdateView.as_view(), name='update'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('<int:pk>', CriminalDetailView.as_view(), name='more'),
]