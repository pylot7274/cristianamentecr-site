from django.db import models

# Create your models here.


class HomePage(models.Model):
    """Home/Landing page content.
       Using model approach in case dynamic content
       needs to be generated.
    """
    site_name = models.CharField(max_length=250)
    logo_image = models.ImageField(
        upload_to="home_landing/img", editable=False, default='cristianamente_logo.png')
    tagline = models.CharField(max_length=250)
    briefing = models.TextField()
