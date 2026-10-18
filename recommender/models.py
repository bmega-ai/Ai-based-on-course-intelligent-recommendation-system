from django.db import models

class Domain(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    skills = models.TextField()
    learning_path = models.TextField()
    platforms = models.TextField()
    youtube_link = models.URLField(max_length=500, blank=True, null=True)
    coursera_link = models.URLField(max_length=500, blank=True, null=True)
    fcc_link = models.URLField(max_length=500, blank=True, null=True)
    guvi_link = models.URLField(max_length=500, blank=True, null=True)
    google_search_link = models.URLField(max_length=500, blank=True, null=True)


    def __str__(self):
        return self.name