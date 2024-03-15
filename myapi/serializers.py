from rest_framework import serializers
from myapi.models import flower

class flowerSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = flower
        fields = '__all__'