from rest_framework import serializers
from pokemon import models
from django.contrib.auth import get_user_model


class NestedPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Type
        fields = (
            'type',
        )

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username',)

class PokemonSerializer(serializers.ModelSerializer):
    pokemon_type = NestedPokemonSerializer(many=True, read_only=True, source='types')
    trainer = NestedUserSerializer(many=True, read_only=True, source='caught_by')
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
            'trainer',
            'pokemon_type',
        )
        model = models.Pokemon

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'caught')