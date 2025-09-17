from django.urls import path


from . import views

urlpatterns=[
    path('books', views.BookView.as_view(), name = 'Book'),
    path('book/<int:pk>',views.SingleBookView.as_view(), name = 'Single_Book' ),
]