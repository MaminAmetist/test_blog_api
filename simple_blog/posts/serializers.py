import os
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post

User = get_user_model()


class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "title",
            "description",
            "body",
            "image"
        ]

    def validate_title(self, value):
        if len(value) > 100:
            return serializers.ValidationError("Max title length is 100 characters")
        return value

    def validate_description(self, value):
        if len(value) > 200:
            return serializers.ValidationError(
                "Max description length is 200 characters"
            )
        return value

    def clean_image(self, value):
        initial_path = value.path
        new_path = settings.MEDIA_ROOT + value.name
        os.rename(initial_path, new_path)
        return value


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "author",
            "image",
            "description",

        ]


class PostDetailSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "slug",
            "title",
            "description",
            "body",
            "author",
            "image",
            "created_at",
            "updated_at",
        ]

    def get_slug(self, obj):
        return obj.slug
