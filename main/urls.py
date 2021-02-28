from django.urls import path
import main.views as mv

urlpatterns = [
    path('', mv.landing, name='landing'),
    path('dkTemp',mv.dkTemp),
    path('dynamicPage',mv.dynamicPage),
    path('notice',mv.notice),
    path('news',mv.information),
    path('admissions',mv.admissionPage),
    path('activities',mv.activitiesPage),
]
