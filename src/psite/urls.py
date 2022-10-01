from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, urlpatterns
from . import views
urlpatterns = [path('register/',views.registerpath),
               path('ureg/',views.ureg),
               path('login/',views.loginpath),
               path('ulogin/',views.ulogin),
               path('home/',views.homepath),
               path('events/',views.eventspath),
               path('booking/',views.bookingpath),
               path('aboutus/',views.aboutus),
               path('contactus/',views.contactpath),
               path('',views.registerpath),
               path('fetchall/',views.fetchall),
               path('bookingfetch/',views.bookingfetch),
               path('uorder/',views.uorder),
               path('ereg/',views.ereg),
               path('cpass/',views.cpass),
               path('getotp/',views.getotp),
               path('changepass/',views.changepass),
               path('SM/',views.sendSimpleEmail),
]
urlpatterns += staticfiles_urlpatterns()