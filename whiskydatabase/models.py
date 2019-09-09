from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from django.utils.crypto import get_random_string

ROLE_CHOICE = (
    ('Admin', 'Admin'),
    ('Drinker', 'Drinker'),
    ('Lover', 'Lover'),
    ('Pro', 'Pro'),
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

def path_and_rename(instance, filename):
    upload_to = 'user'
    ext = filename.split('.')[-1]
    # get filename
    filename = 'profile/{}.{}'.format(instance.user.username.split('@')[0]+'_'+get_random_string(length=15), ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

# Create your models here.
class UserRole(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, unique=True, related_name="role")
    role = models.CharField(max_length=10, choices=ROLE_CHOICE)
    class Meta:
        ordering = ['-id']

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, unique=True, related_name="profile")
    nickname = models.TextField(blank=True, null=True)
    profilepic = models.ImageField(upload_to=path_and_rename, blank=True, null=True)
    wishlist = models.IntegerField(default=0)

    class Meta:
        ordering = ['-id']
    def __str__(self):
        return user

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

class Country(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='country/uploads/%Y/%m/%d/', blank=True)
    
    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=20)
    country = models.ForeignKey(Country, related_name='region_country', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='region/uploads/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.name

class Distillery(models.Model):
    is_active = models.BooleanField(default=False)
    name = models.CharField(max_length=100, unique=True)
    region = models.ForeignKey(Region, related_name='distillery_region', on_delete=models.CASCADE)
    country = models.ForeignKey(Country, related_name='distillery_country', on_delete=models.CASCADE)
    year_founded = models.IntegerField(blank=True, null=True)
    owner = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='distillery/uploads/%Y/%m/%d/', blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    smws_code = models.IntegerField(default=0)
    official_site = models.CharField(max_length=150, blank=True, null=True)
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
    abv = models.FloatField(default=0)
    general_desc = models.TextField(blank=True, null=True)
    casktype = models.CharField(max_length=100, blank=True, null=True)
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
        return reverse('distillery-pk-slug-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class PersonalWhiskyNote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='per_user', on_delete=models.CASCADE)
    whisky = models.ForeignKey(WhiskyInfo, related_name='per_whisky', on_delete=models.CASCADE)
    flora = models.IntegerField(default=0)
    fruity = models.IntegerField(default=0)
    creamy = models.IntegerField(default=0)
    nutty = models.IntegerField(default=0)
    malty = models.IntegerField(default=0)
    spicy = models.IntegerField(default=0)
    smoky = models.IntegerField(default=0)
    peaty = models.IntegerField(default=0)

class GeneralWhiskyNote(models.Model):
    whisky = models.OneToOneField(WhiskyInfo, on_delete=models.CASCADE, unique=True, related_name="gen_whisky")
    flora = models.IntegerField(default=0)
    fruity = models.IntegerField(default=0)
    creamy = models.IntegerField(default=0)
    nutty = models.IntegerField(default=0)
    malty = models.IntegerField(default=0)
    spicy = models.IntegerField(default=0)
    smoky = models.IntegerField(default=0)
    peaty = models.IntegerField(default=0)
    total_notes_num = models.IntegerField(default=0)

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='note_user')
    whisky = models.ForeignKey(WhiskyInfo, on_delete=models.CASCADE)
    note = models.TextField()
    publish_choice = models.CharField(max_length=10, choices=PUBLISH_CHOICE)
    rating = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    whisky = models.ForeignKey(WhiskyInfo, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Bar(models.Model):
    name = models.CharField(max_length=100, unique=True)
    region = models.ForeignKey(Region, related_name='bar_region', on_delete=models.CASCADE)
    country = models.ForeignKey(Country, related_name='bar_country', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='bar/uploads/%Y/%m/%d/', blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    slug = models.SlugField(
        default='',
        editable=False,
        max_length=200,
    )

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


    
    