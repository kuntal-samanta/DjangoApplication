'''
    Serializers.py
   @ Author  Kuntal
   @ Company 
   @ version  0.1
   @date      10/12/2019
'''

from rest_framework import serializers
from ..models import Profile


class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['bio', 'location']
    
    def validate_bio(self, val):
        print("Field Validate")
        return val
    
    def validate(self, values):
        print("Final Validate Logic If Any")
        return values
    
    # def create(self, validated_data):
    #     pass
