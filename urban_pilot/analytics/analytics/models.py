from django.db import models

# Create your models here.


class Locations(models.Model):
    """Locations from the users"""

    # zip code
    zip_code = models.CharField(
        max_length=5,
        blank=False,
        null=False,
        verbose_name="zip_code",
    )

    # city
    city = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name="ciudad",
    )

    # county
    county = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name="zip_code",
    )

    # state
    state = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name="zip_code",
    )

    # # country
    # country = models.CharField(
    #     max_length=100,
    #     blank=False,
    #     null=False,
    #     default="US",
    #     verbose_name="country",
    # )

    # number of users
    users_ammount = models.PositiveIntegerField(
        verbose_name="ammount of users in the location",
        null=False,
        blank=False,
        default=0,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        db_table = "user_locations"
        unique_together = ["zip_code", "city", "county", "state"]
        verbose_name = ("Location")
        verbose_name_plural = ("Locations")

    def __str__(self: object) -> str:
        return str(self.zip_code)
