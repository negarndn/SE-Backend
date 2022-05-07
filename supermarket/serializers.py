from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ['username', 'first_name', 'last_name', 'mode', 'password']

        extra_kwargs = {
            'password': {
                'write_only': True,

            }
        }

    def create(self, validated_data):
        try:
            user = models.UserProfile.objects.create_user(
                username=validated_data['username'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                password=validated_data['password'],
            )
            if validated_data['phone']:
                user.phone = validated_data['phone']
<<<<<<< HEAD
            if validated_data['student_id']:
                user.student_id = validated_data['student_id']
=======
>>>>>>> 6c0390487d9d704aece46e24d17518410ca8b7d9
            user.save()
            return user

        except Exception as e:
            error = {'message': ",".join(e.args) if len(e.args) > 0 else 'Unknown Error'}
            raise serializers.ValidationError(error)

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta(UserSerializer.Meta):
        model = models.UserProfile
        fields = ['username', 'first_name', 'last_name', 'mode', 'password']

        extra_kwargs = {
                'password': {
                    'read_only': True,
                },
                'username': {
                    'read_only': True,
                },
                 'first_name': {
                    'read_only': True,
                },
                 'last_name': {
                    'read_only': True,
                },
                 'mode': {
                    'read_only': True,
                },

            }

    def create(self, validated_data):
        return None
