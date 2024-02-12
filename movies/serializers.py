from rest_framework import serializers
from movies.models import RatingOptions, Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    duration = serializers.CharField(required=False)
    rating = serializers.ChoiceField(
        choices=RatingOptions.choices, default=RatingOptions.RATE_G
    )
    synopsis = serializers.CharField(required=False)
    added_by = serializers.SerializerMethodField()

    def get_added_by(self, instance):
        return instance.user.email

    def create(self, validated_data):
        movie = Movie.objects.create(**validated_data)
        return movie
