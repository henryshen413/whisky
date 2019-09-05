from whiskydatabase.models import WhiskyInfo, Distillery, Region, Country
from rest_framework import serializers

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

