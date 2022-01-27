from django.urls import path

from .views import get_alumnos, alumno, login_token

urlpatterns = [
    path('', get_alumnos),
    path('<int:id_alumno>', alumno),
    #path('add', add_alumno),
    path('login-token/<slug:token>/<slug:password>', login_token)
    
]
