
from rest_framework import serializers
from pokemon.models import Pokemon, Type
from users.models import CustomUser

class NestedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'type',
        )
        model = Type

class NestedPokemonSerializer(serializers.ModelSerializer):
    type_detail = NestedTypeSerializer(source='types', many=True)
    class Meta:
        fields = (
            'name',
            'image_front',
            'image_back',
            'height',
            'weight',
            'type_detail'
            
            
        )   
        model = Pokemon     

class PokemonSerializer(serializers.ModelSerializer):
    type_detail = NestedTypeSerializer(source='types', many=True)
    class Meta:
        fields = (
            'id',
            'number',
            'name',
            'height',
            'weight',
            'image_front',
            'image_back',
            'caught_by',
            'type_detail'
        )
        model = Pokemon


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'type',
            'pokemon'
        )
        model = Type

class UserSerializer(serializers.ModelSerializer):
    caught_detail = NestedPokemonSerializer(source='caught', many=True, read_only=True)
    class Meta: 
        fields = (
            'id',
            'username',
            'caught_detail',
            'caught',
            
        )
        model = CustomUser