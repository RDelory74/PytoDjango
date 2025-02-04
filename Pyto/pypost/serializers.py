from rest_framework import serializers
from .models import Post

class PostSerializers (serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        extra_kwargs = { # !!!!! kwargs !!!!!!
            'title': {'required':True},
            'content': {'required':True},
            'created_at': {'read_only': True}
        }

#fields = ['title','content']

