from django.urls import include, path

urlpatterns = [
    # All routes live in the "sections" app.
    path('', include('sections.urls')),
    # The second app: the product catalog.
    path('', include('products.urls')),
]

# Any unknown address (outside the known sections) shows a custom 404 page.
handler404 = 'sections.views.page_not_found'
