from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Sample


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class SampleResponseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sample
        fields = [
            'id',
            'description',
            'created_at'
        ]


class SampleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sample
        fields = [
            'description',
            'pop_a',
            'r_a',
            'k_a',
            'ab_a',
            'ac_a',
            'ad_a',
            'ae_a',
            'pop_b',
            'r_b',
            'k_b',
            'ab_b',
            'ac_b',
            'ad_b',
            'ae_b',
            'pop_c',
            'r_c',
            'k_c',
            'ab_c',
            'ac_c',
            'ad_c',
            'ae_c',
            'pop_d',
            'r_d',
            'k_d',
            'ab_d',
            'ac_d',
            'ad_d',
            'ae_d',
            'pop_e',
            'r_e',
            'k_e',
            'ab_e',
            'ac_e',
            'ad_e',
            'ae_e',
        ]



