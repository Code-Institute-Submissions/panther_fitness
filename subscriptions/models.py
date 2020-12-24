from django.db import models


class Programme(models.Model):

    class Meta:

        verbose_name_plural = 'Programme'

    programme_duration = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False,
                                default=0)
    image_url = models.URLField(max_length=1100, null=True, blank=True)
    image_file = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.programme_duration
