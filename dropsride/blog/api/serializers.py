from rest_framework import exceptions, serializers
from taggit.models import Tag
from taggit.serializers import TaggitSerializer, TagListSerializerField

from ..models import News


class TagSerializer(TaggitSerializer, serializers.ModelSerializer):
    # tags = TagListSerializerField()

    class Meta:
        model = Tag
        fields = "__all__"


class NewsSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = News
        fields = [
            "image",
            "slug",
            "title",
            "summary",
            "keywords",
            "tags",
            "content",
            "author",
            "publisher",
            "published_date",
            "draft",
            "featured",
            "url",
        ]
        read_only_fields = ["slug"]
        extra_kwargs = {"url": {"view_name": "api:news-detail", "lookup_field": "slug"}}

    def create(self, validated_data):
        tags = validated_data.pop("tags", [])
        instance = super().create(validated_data)
        instance.author = self.context["request"].user
        instance.save(update_fields=["author"])
        instance.tags.add(*tags)
        return instance

    def update(self, instance, validated_data):
        tags = validated_data.pop("tags", [])
        instance = super().update(instance, validated_data)
        instance.tags.add(*tags)
        return instance
