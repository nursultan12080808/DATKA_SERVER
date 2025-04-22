from rest_framework import serializers
from datka_app.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('is_staff', 'is_active', 'password', 'is_superuser', 'groups', 'user_permissions')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = "__all__"


class DetailUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('is_staff', 'is_active', 'password', 'is_superuser', 'groups', 'user_permissions')


class DetailNewsSerializer(serializers.ModelSerializer):

    images = ImageSerializer(many = True)
    

    class Meta:
        model = News
        fields = '__all__'


class ListNewsSerializer(serializers.ModelSerializer):

    images = ImageSerializer(many = True)

    class Meta:
        model = News
        fields = "__all__"


class AdminstrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Adminstration
        fields = "__all__"


class JobsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Jobs
        fields = "__all__"


class EarthSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Earth
        fields = "__all__"


class AgriculturalSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Agricultural
        fields = "__all__"


class StateLandSerializer(serializers.ModelSerializer):

    class Meta:
        model = StateLand
        fields = "__all__"


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"


class ResolutionSerializer(serializers.ModelSerializer):

    images = ImageSerializer(many = True)

    class Meta:
        model = Resolution
        fields = "__all__"


class GlavaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Glava
        fields = "__all__"


class AdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = Admins
        fields = "__all__"