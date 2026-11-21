from django.db import models


class Office(models.Model):
    """An office or showroom of the company (Contacts section)."""
    country = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)

    class Meta:
        ordering = ['country', 'city']

    def __str__(self):
        return f'{self.city}, {self.country}'


class Manager(models.Model):
    """A person from the Management section."""
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    is_board_member = models.BooleanField(default=False)
    office = models.ForeignKey(Office, null=True, blank=True,
                               on_delete=models.SET_NULL, related_name='managers')

    def __str__(self):
        return f'{self.name} ({self.position})'


class NewsCategory(models.Model):
    """Subsection of the News section: Company, Products, Events ..."""
    name = models.CharField(max_length=60)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=200, blank=True)
    sort_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['sort_order', 'name']
        verbose_name_plural = 'news categories'

    def __str__(self):
        return self.name


class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_at = models.DateField()
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE,
                                 related_name='articles')

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Slipper(models.Model):
    """A product of the company (Products section)."""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    image = models.CharField(max_length=100, blank=True,
                             help_text='File name inside static/img/')

    def __str__(self):
        return self.name
