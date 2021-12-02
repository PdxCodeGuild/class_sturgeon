from django.db.models import fields
from rest_framework import serializers
from pokemon.models import Pokemon, Type


class pokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('name','number','height', 'weight', 'image_front', 'image_back', 'caught_by') 
    
class typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('type','pokemon')