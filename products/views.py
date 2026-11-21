from sections.views import SectionView

from .data import SECTIONS


class ProductsView(SectionView):
    """Reuses the generic section controller with this app's own data."""
    section_key = 'products'
    index_template = 'products.html'
    sections_data = SECTIONS

    def get_index_context(self):
        return {'products': self.all_items()}
