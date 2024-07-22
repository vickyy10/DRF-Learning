from rest_framework import serializers

from .models import Person

class PesronModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'


# class PesronSerializer(serializers.Serializer):

#     name=serializers.CharField()
#     age=serializers.IntegerField()
#     place=serializers.CharField()

    