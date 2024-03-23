from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('log', views.log, name='log'),
   path('gallery', views.gallery, name='gallery'),
   path('ngos', views.ngos, name='ngos'),
   path('state', views.state, name='state'),
   path('hotel', views.hotel, name='hotel'),
   path('budget', views.budget, name='budget'),
   path('events', views.events, name='events'),
   path('bookingform', views.bookingform, name='bookingform'),
   path('contact', views.contact, name='contact'),
   path('about', views.about, name='about'),
   path('search', views.search, name="search"),
    path('tourist', views.tourist, name="tourist"),
   path('signup', views.handleSignUp, name="handleSignUp"),
   path('login', views.handleLogin, name="handleLogin"),
   path('logout', views.handelLogout, name="handleLogout"),
    path('home', views.homepage,name="homepage"),
#    path('about', views.aboutpage,name="aboutpage"),
 #   path('contact', views.contactpage,name="contactpage"),
    path('user', views.user_log_sign_page,name="userloginpage"),
    path('user/login', views.user_log_sign_page,name="userloginpage"),
    path('user/bookings', views.user_bookings,name="dashboard"),
    path('user/book-room', views.book_room_page,name="bookroompage"),
    path('user/book-room/book', views.book_room,name="bookroom"),
    path('user/signup', views.user_sign_up,name="usersignup"),
    path('staff/', views.staff_log_sign_page,name="staffloginpage"),
    path('staff/login', views.staff_log_sign_page,name="staffloginpage"),
    path('staff/signup', views.staff_sign_up,name="staffsignup"),
    path('logout', views.logoutuser,name="logout"),
    path('staff/panel', views.panel,name="staffpanel"),
    
    path('staff/panel/add-new-location', views.add_new_location,name="addnewlocation"),
    path('staff/panel/edit-room', views.edit_room),
    path('staff/panel/add-new-room', views.add_new_room,name="addroom"),
    path('staff/panel/edit-room/edit', views.edit_room),
    path('staff/panel/view-room', views.view_room),
   
 

]
