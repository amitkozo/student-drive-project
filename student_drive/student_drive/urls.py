from django.contrib import admin
from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView # הוספנו עבור דף התנאים
from django.contrib.auth import views as auth_views # ייבוא מערכת ההתחברות המובנית

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('logout/', views.logout_view, name='logout'),
    path('analytics/', views.analytics_dashboard, name='analytics'),
    # הוספת נתיב לדף התנאים שיצרנו קודם
    path('terms/', TemplateView.as_view(template_name='core/terms.html'), name='terms'),
    path('download/<int:document_id>/', views.download_file, name='download_file'),
    # נתיב ההתחברות (Login)
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    # נתיב הפרופיל האישי
    path('profile/', views.profile, name='profile'),
]

# מאפשר להציג קבצים שהועלו (Media) בזמן פיתוח
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)