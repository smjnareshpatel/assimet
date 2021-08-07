
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name', 'last_name', 'email','phone_no','is_active','password')
        extra_kwargs = {'password': {'write_only': True}}
        
    def validate_email(self, value):
        user_qs = User.objects.filter(email__iexact=value)
        if user_qs.exists():
            raise serializers.ValidationError("User with this email already registered")
        return value

    def validate_first_name(self, value):
        user_qs = User.objects.filter(first_name__iexact=value)
        if user_qs.exists():
            raise serializers.ValidationError("User with this first_name already registered")
        return value

    def validate_phone_no(self, value):
        user_qs = User.objects.filter(phone_no__iexact=value)
        if user_qs.exists():
            raise serializers.ValidationError("User with this first_name already registered")
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        f_name = validated_data.get('first_name')
        l_name = validated_data.get('last_name')
        username = f_name + ' ' + l_name
        user = User(**validated_data, username=username)
        user.set_password(password)
        user.save()
        
        return user

    # def update(self, instance, validated_data):
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.phone_no = validated_data.get('phone_no', instance.phone_no)
    #     instance.is_active = validated_data.get('is_active', instance.is_active)
    #     instance.save()

    #     return instance


class UserSerializerUpdate(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name', 'last_name', 'email','phone_no','is_active')

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_no = validated_data.get('phone_no', instance.phone_no)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()

        return instance