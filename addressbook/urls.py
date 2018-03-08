from django.urls import path #from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LoginView, LogoutView
import contacts.views


urlpatterns = [
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),

    path(r'', contacts.views.ListContactView.as_view(),
        name='contacts-list',),
    path(r'(?<int:pk>\d+)/', contacts.views.ContactView.as_view(),
        name='contacts-view',),
    path(r'new', contacts.views.CreateContactView.as_view(),
        name='contacts-new',),
    path(r'edit/(?<int:pk>\d+)/', contacts.views.UpdateContactView.as_view(),
        name='contacts-edit',),
    path(r'edit/(?<int:pk>\d+)/addresses', contacts.views.EditContactAddressView.as_view(),
        name='contacts-edit-addresses',),
    path(r'delete/(?<int:pk>\d+)/', contacts.views.DeleteContactView.as_view(),
        name='contacts-delete',),
]

urlpatterns += staticfiles_urlpatterns()
