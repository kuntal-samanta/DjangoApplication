from rest_framework import serializers, fields
from .models import *



class All_User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username']




################################################################################
class All_School_Serializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'school_name']


class All_Standerd_Serializer(serializers.ModelSerializer):
    school = All_School_Serializer()

    class Meta:
        model = Standerd
        fields = ['id', 'standerd_name', 'school']


class All_Tag_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'tag_name', 'created_at']


class All_Author_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'author_name', 'author_email']


class All_Book_Serializer(serializers.ModelSerializer):
    author = All_Author_Serializer()
    tag = All_Tag_Serializer(many=True)
    for_standerd = All_Standerd_Serializer()

    class Meta:
        model = Book
        fields = ['id', 'book_name', 'book_page', 'author', 'tag', 'for_standerd']
        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=Event.objects.all(),
        #         fields=['room_number', 'date']
        #     )
        # ]
    
    # def validate_<model_feild_name>(self, value):
    #     return value

    # def validate(self, data):
    #     return data

    # def create(self, validated_data):
    #     pass

    # def update(self, instance, validated_data):
    #     pass

    # def save(self):
    #     pass

################################################################################


"""
class ContactForm(serializers.Serializer):
    email = serializers.EmailField()
    message = serializers.CharField()
"""


