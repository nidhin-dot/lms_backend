
from rest_framework import serializers

from accounts.models import User



class TrainerSerializer(serializers.ModelSerializer):

    class Meta:

        model=User

        fields=["id","name","email","passowrd","phone","dob"]

    def create(self, validated_data):
        
        return User.objects.create_user(**validated_data)
