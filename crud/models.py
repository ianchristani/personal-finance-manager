from django.db import models

# the table
class eventModel(models.Model):
    event = models.CharField(max_length = 150)
    total = models.DecimalField(max_digits = 9, decimal_places = 2)
    description = models.CharField(max_length = 250)
    pic  = models.ImageField(null = True, blank=True, upload_to = "media/", )
    date = models.DateField(auto_now = True)

    # displaying the colunms with names
    def __str__(self) -> str:
        return self.event
