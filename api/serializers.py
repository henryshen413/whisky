from whiskydatabase.models import WhiskyInfo, Distillery, Region, Country
from rest_framework import serializers
from django.utils.html import strip_tags
from django.utils.text import Truncator

class DistillerySerializer(serializers.HyperlinkedModelSerializer):
    country = serializers.SerializerMethodField('get_country_name')
    region = serializers.SerializerMethodField('get_region_name')

    def get_country_name(yself, obj):
        return obj.country.name

    def get_region_name(yself, obj):
        return obj.region.name

    class Meta:
        model = Distillery
        fields = ['name', 'region', 'country', 'owner', 'lon', 'lat']

class WhiskySerializer(serializers.HyperlinkedModelSerializer):
    distillery = DistillerySerializer()
    
    class Meta:
        model = WhiskyInfo
        exclude = ('url',)

""" class MorePostSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField()

    def get_date(self, obj):
        return obj.created_on.strftime("%b. %d, %Y")

    def get_username(self, obj):
        user = obj.user
        if user.profile.nickname:
            name = user.profile.nickname
        elif user.username != user.email:
            name = user.username
        elif user.last_name:
            name = user.last_name + ' ' + user.first_name
        else:
            name = user.username
        return name

    def get_content(self, obj):
        return Truncator(strip_tags(obj.content.rstrip())).words(5)

    class Meta:
        model = Post
        fields = ['slug', 'date', 'username', 'title', 'content', 'featured_image']
 """
