from rest_framework import serializers
from .models import *

class BotUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'