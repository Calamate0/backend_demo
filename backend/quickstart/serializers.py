from django.contrib.auth.models import User, Group
from rest_framework import serializers
from quickstart.models import OmniClass23

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'url', 'email','groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['name', 'url']
        
        
class OmniClass23Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OmniClass23
        fields = ['idOmc23', 'numMat', 'Codigo', 'descriEng', 'descriSpa', 'Nivel', 'regFinal']