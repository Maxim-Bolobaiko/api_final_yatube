from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Post, Group, Follow, User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Group


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="username", read_only=True
    )

    class Meta:
        fields = "__all__"
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field="username"
    )

    class Meta:
        fields = "__all__"
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username",
        default=serializers.CurrentUserDefault(),
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="username"
    )

    class Meta:
        fields = "__all__"
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=["user", "following"],
            )
        ]

    def validate_following(self, data):
        if self.context.get("request").user == data:
            raise serializers.ValidationError(
                "Невозможно подписаться на себя!"
            )
        return data
