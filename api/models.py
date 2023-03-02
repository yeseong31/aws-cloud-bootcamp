from django.db import models


class NotionDatabase(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Notion databases"
        db_table = 'notiondb'
    
    def __str__(self):
        return self.title
