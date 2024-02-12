from django.db import models


class RatingOptions(models.TextChoices):
    RATE_G = "G"
    RATE_PG = "PG"
    RATE_PG_13 = "PG-13"
    RATE_R = "R"
    RATE_NC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default="", blank=True)
    rating = models.CharField(
        max_length=20, choices=RatingOptions.choices, default=RatingOptions.RATE_G
    )
    synopsis = models.TextField(null=True, default="", blank=True)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="movies"
    )

    orders = models.ManyToManyField("users.User", through="movies_orders.MovieOrder")
