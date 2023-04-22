from rest_framework import exceptions, serializers
from taggit.models import Tag
from taggit.serializers import TaggitSerializer, TagListSerializerField

from dropsride.settings.api.serializers import LocalizationSerializer

from ..models import Applicants, Careers, Teams


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = "__all__"
        read_only_fields = ["slug"]
        extra_kwargs = {
            "url": {"view_name": "api:department-detail", "lookup_field": "slug"}
        }


class CareerSerializer(serializers.ModelSerializer):
    # related_careers = serializers.SerializerMethodField()
    # team = TeamSerializer(many=False, read_only=False)
    # location = LocalizationSerializer(many=True, read_only=False)

    class Meta:
        model = Careers
        fields = [
            "title",
            "slug",
            "summary",
            "keywords",
            "team",
            "location",
            "salary",
            "competency",
            "content",
            "published_date",
            "draft",
            # "related_careers",
            "url",
        ]
        read_only_fields = ["slug"]
        extra_kwargs = {
            "url": {"view_name": "api:career-detail", "lookup_field": "slug"}
        }

    # def get_related_careers(self, obj):
    #     return obj.related_careers()

    # def get_or_create_locations(self, locations):
    #     location_ids = []
    #     for location in locations:
    #         location_instance, created = Localization.objects.get_or_create(uuid=location.get('uuid'), defaults=package)
    #         location_ids.append(location_instance.uuid)
    #     return location_ids

    # def create_or_update_locations(self, locations):
    #     location_ids = []
    #     for location in locations:
    #         location_instance, created = Localization.objects.update_or_create(uuid=location.get('uuid'), defaults=package)
    #         location_ids.append(location_instance.uuid)
    #     return location_ids

    # def create(self, validated_data):
    #     location = validated_data.pop('location', [])
    #     team = validated_data.pop('team')
    #     career = Careers.objects.create(**validated_data)
    #     career.location.set(self.get_or_create_locations(location))
    #     career.team_id = team_id
    #     return career

    # # def update(self, instance, validated_data):
    # #     package = validated_data.pop('package', [])
    # #     instance.package.set(self.create_or_update_packages(package))
    # #     fields = ['order_id', 'is_cod']
    # #     for field in fields:
    # #         try:
    # #             setattr(instance, field, validated_data[field])
    # #         except KeyError:  # validated_data may not contain all fields during HTTP PATCH
    # #             pass
    # #     instance.save()
    # #     return instance

    # def update(self, instance, validated_data):
    #     team = validated_data.pop('team')
    #     location = validated_data.pop('location', [])
    #     instance.team_id = team.id
    #     instance.location.set(self.create_or_update_locations(location))
    #     for attr, value in validated_data.items():
    #         setattr(instance, attr, value)
    #     instance.save()
    #     return instance


class ApplicantSerializer(serializers.ModelSerializer):
    # position = CareerSerializer(many=False)
    # location = LocalizationSerializer(many=False)

    class Meta:
        model = Applicants
        fields = [
            "position",
            "first_name",
            "middle_name",
            "last_name",
            "email",
            "phone_number",
            "gender",
            "age",
            "location",
            "file",
            "cover_letter",
            "disability",
            "consent",
            "country",
        ]

    # def get_or_create_locations(self, locations):
    #     location_ids = []
    #     for location in locations:
    #         location_instance, created = Localization.objects.get_or_create(uuid=location.get('uuid'), defaults=package)
    #         location_ids.append(location_instance.uuid)
    #     return location_ids

    # def create_or_update_locations(self, locations):
    #     location_ids = []
    #     for location in locations:
    #         location_instance, created = Localization.objects.update_or_create(uuid=location.get('uuid'), defaults=package)
    #         location_ids.append(location_instance.uuid)
    #     return location_ids

    # def create(self, validated_data):
    #     location = validated_data.pop('location')
    #     position = validated_data.pop('position')
    #     applicant = Applicants.objects.create(**validated_data)
    #     applicant.location.uuid = location
    #     applicant.position.id = position
    #     applicant.save()
    #     return applicant

    # def update(self, instance, validated_data):
    #     package = validated_data.pop('package', [])
    #     instance.package.set(self.create_or_update_packages(package))
    #     fields = ['order_id', 'is_cod']
    #     for field in fields:
    #         try:
    #             setattr(instance, field, validated_data[field])
    #         except KeyError:  # validated_data may not contain all fields during HTTP PATCH
    #             pass
    #     instance.save()
    #     return instance

    # def update(self, instance, validated_data):
    #     position = validated_data.pop('position')
    #     location = validated_data.pop('location')
    #     instance.position.id = position #.get('uuid', position.id)
    #     instance.location.uuid = location #.get('uuid', location.uuid)
    #     for attr, value in validated_data.items():
    #         setattr(instance, attr, value)
    #     instance.save()
    #     return instance
