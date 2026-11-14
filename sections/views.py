from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView

from .data import SECTIONS


class HomeView(TemplateView):
    template_name = 'home.html'
    extra_context = {'section': 'home'}


class SectionView(TemplateView):
    """
    Base class-based controller for a section with subsections.

    * /<section>/            -> section overview (index_template)
    * /<section>/<slug>/     -> subsection page, if the slug is known
    * /<section>/<anything>  -> unknown slug or deeper path: the overview
                                is shown (the "catch-all" behaviour).
    """
    section_key = None       # key in SECTIONS, also the URL name of the section
    index_template = None    # template of the section overview

    def get(self, request, *args, **kwargs):
        subsections = SECTIONS[self.section_key]['subsections']
        self.subsection = subsections.get(kwargs.get('slug'))
        return super().get(request)

    def get_template_names(self):
        if self.subsection:
            return ['subsection.html']
        return [self.index_template]

    def get_index_context(self):
        """Extra context for the section overview; override in subclasses."""
        return {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = SECTIONS[self.section_key]

        subnav = [{
            'title': 'Overview',
            'url': reverse(self.section_key),
            'active': self.subsection is None,
        }]
        cards = []
        for slug, sub in data['subsections'].items():
            url = reverse(f'{self.section_key}-sub', kwargs={'slug': slug})
            subnav.append({
                'title': sub['title'],
                'url': url,
                'active': sub is self.subsection,
            })
            cards.append({'title': sub['title'], 'intro': sub['intro'], 'url': url})

        context.update(
            section=self.section_key,
            section_title=data['title'],
            subnav=subnav,
            subsection_cards=cards,
            subsection=self.subsection,
        )
        if not self.subsection:
            context.update(self.get_index_context())
        return context

    def all_items(self):
        """Items of all subsections, each tagged with its subsection title."""
        items = []
        for sub in SECTIONS[self.section_key]['subsections'].values():
            for item in sub['items']:
                items.append({**item, 'category': sub['title']})
        return items


class NewsView(SectionView):
    section_key = 'news'
    index_template = 'news.html'

    def get_index_context(self):
        news = sorted(self.all_items(), key=lambda i: i['date'], reverse=True)
        return {'news': news}


class ManagementView(SectionView):
    section_key = 'management'
    index_template = 'management.html'

    def get_index_context(self):
        return {'managers': self.all_items()}


class AboutView(SectionView):
    section_key = 'about'
    index_template = 'about.html'


class ContactsView(SectionView):
    section_key = 'contacts'
    index_template = 'contacts.html'


def page_not_found(request, exception=None):
    return render(request, '404.html', {'section': None}, status=404)
