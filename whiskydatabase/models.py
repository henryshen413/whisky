from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify

ROLE_CHOICE = (
    ('Admin', 'Admin'),
    ('Drinker', 'Drinker'),
    ('Lover', 'Lover'),
    ('Pro', 'Pro'),
)

GRADES_CHOICES = (
    (0, '0'),
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)

PUBLISH_CHOICE = (
    ('Private', 'Private'),
    ('Public', 'Public'),
)

BOTTLING_CHOICE = (
    ('OB', 'OB'),
    ('IB', 'IB'),
)

BOOLEAN_CHOICE = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)

# Create your models here.
class UserRole(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, unique=True, related_name="role")
    role = models.CharField(max_length=10, choices=ROLE_CHOICE)
    class Meta:
        ordering = ['-id']

class Menu(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True)
    icon = models.CharField(max_length=255, default='fa fa-search', blank=True, null=True)
    status = models.BooleanField(default=True)
    lvl = models.IntegerField(blank=True)

    def __str__(self):
        return self.title

    def get_children(self):
        return self.menu_set.filter(status=True)

    def has_children(self):
        if self.get_children():
            return True
        return False

    def get_absolute_url(self):
        return reverse('selected_category', kwargs={"slug": self.title})

class Distillery(models.Model):
    is_active = models.BooleanField(default=False)
    name = models.CharField(max_length=100, unique=True)
    region = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    year_founded = models.IntegerField(default=0)
    owner = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='media/distillery/uploads/%Y/%m/%d/', blank=True, null=True)
    lon = models.FloatField()
    lat = models.FloatField()
    slug = models.SlugField(
        default='',
        editable=False,
        max_length=200,
    )

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('article-pk-slug-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class WhiskyInfo(models.Model):
    name = models.CharField(max_length=100, unique=True)
    brand_series = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    distillery = models.ForeignKey(Distillery, related_name='whisky_distillery', on_delete=models.CASCADE)
    year = models.IntegerField(default=0)
    abv = models.IntegerField(default=0)
    casktype = models.CharField(max_length=100)
    bottler = models.CharField(max_length=2, choices=BOTTLING_CHOICE)
    photo = models.ImageField(upload_to='whisky/uploads/%Y/%m/%d/', blank=True, null=True)
    chill_filtration = models.CharField(max_length=2, choices=BOOLEAN_CHOICE)
    artificial_coloring = models.CharField(max_length=2, choices=BOOLEAN_CHOICE)
    cask_num = models.CharField(max_length=15, blank=True)
    bottle_num =  models.CharField(max_length=15, blank=True)
    slug = models.SlugField(
        default='',
        editable=False,
        max_length=200,
    )

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('article-pk-slug-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class PersonalWhiskyNote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='per_user', on_delete=models.CASCADE)
    whisky = models.ForeignKey(WhiskyInfo, related_name='per_whisky', on_delete=models.CASCADE)
    flora = models.CharField(max_length=1, choices=GRADES_CHOICES)
    fruity = models.CharField(max_length=1, choices=GRADES_CHOICES)
    sweet = models.CharField(max_length=1, choices=GRADES_CHOICES)
    creamy = models.CharField(max_length=1, choices=GRADES_CHOICES)
    nutty = models.CharField(max_length=1, choices=GRADES_CHOICES)
    malty = models.CharField(max_length=1, choices=GRADES_CHOICES)
    salty = models.CharField(max_length=1, choices=GRADES_CHOICES)
    spicy = models.CharField(max_length=1, choices=GRADES_CHOICES)
    smoky = models.CharField(max_length=1, choices=GRADES_CHOICES)
    peaty = models.CharField(max_length=1, choices=GRADES_CHOICES)

class GeneralWhiskyNote(models.Model):
    whisky = models.OneToOneField(WhiskyInfo, on_delete=models.CASCADE, unique=True, related_name="gen_whisky")
    flora = models.IntegerField(default=0)
    fruity = models.IntegerField(default=0)
    sweet = models.IntegerField(default=0)
    creamy = models.IntegerField(default=0)
    nutty = models.IntegerField(default=0)
    malty = models.IntegerField(default=0)
    salty = models.IntegerField(default=0)
    spicy = models.IntegerField(default=0)
    smoky = models.IntegerField(default=0)
    peaty = models.IntegerField(default=0)

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='note_user')
    whisky = models.ForeignKey(WhiskyInfo, on_delete=models.CASCADE)
    note = models.TextField()
    publish_choice = models.CharField(max_length=10, choices=PUBLISH_CHOICE)
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


    
    