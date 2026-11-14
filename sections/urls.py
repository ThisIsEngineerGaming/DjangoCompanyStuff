from django.urls import path

from . import views


def section_routes(prefix, view, name):
    """
    /<prefix>/                -> section overview
    /<prefix>/<slug>/         -> subsection (e.g. /contacts/france/)
    /<prefix>/<slug>          -> the same without the trailing slash
                                 (e.g. /contacts/france)
    """
    return [
        path(f'{prefix}/',                view.as_view(), name=name),
        path(f'{prefix}/<slug:slug>/',    view.as_view(), name=f'{name}-sub'),
        path(f'{prefix}/<slug:slug>',     view.as_view(), name=f'{name}-sub-noslash'),
    ]


def catch_all(prefix, view, name):
    # Any other remainder of the path (even with slashes) shows the section.
    return [path(f'{prefix}/<path:_>', view.as_view(), name=f'{name}-catchall')]


urlpatterns = [path('', views.HomeView.as_view(), name='home')]

# Base addresses and subsections first ...
urlpatterns += section_routes('news', views.NewsView, 'news')
urlpatterns += section_routes('management', views.ManagementView, 'management')
urlpatterns += section_routes('about', views.AboutView, 'about')
urlpatterns += section_routes('contacts', views.ContactsView, 'contacts')
urlpatterns += [path('contact/', views.ContactsView.as_view(), name='contact-alt')]
urlpatterns += [
    path('contact/<slug:slug>/', views.ContactsView.as_view(), name='contact-alt-sub'),
    path('contact/<slug:slug>', views.ContactsView.as_view(), name='contact-alt-sub-noslash'),
]

# ... catch-alls LAST (order matters!)
urlpatterns += catch_all('news', views.NewsView, 'news')
urlpatterns += catch_all('management', views.ManagementView, 'management')
urlpatterns += catch_all('about', views.AboutView, 'about')
urlpatterns += catch_all('contacts', views.ContactsView, 'contacts')
urlpatterns += catch_all('contact', views.ContactsView, 'contact-alt')
