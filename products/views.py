from django.urls import reverse

from sections.views import SectionView

from .classes import summarize
from .data import SECTIONS


class ProductsView(SectionView):
    """Reuses the generic section controller, but passes Product objects."""
    section_key = 'products'
    index_template = 'products.html'
    sections_data = SECTIONS

    def get_template_names(self):
        if self.subsection:
            return ['product_list.html']
        return [self.index_template]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.subsection:
            context['stats'] = summarize(self.subsection['items'])
        return context

    def get_index_context(self):
        """A nested dict: summary + categories, each with a list of Product."""
        categories = []
        all_products = []
        for slug, sub in self.sections_data[self.section_key]['subsections'].items():
            categories.append({
                'title': sub['title'],
                'intro': sub['intro'],
                'url': reverse('products-sub', kwargs={'slug': slug}),
                'products': sub['items'],
            })
            all_products.extend(sub['items'])
        return {'catalog': {
            'summary': summarize(all_products),
            'categories': categories,
        }}
