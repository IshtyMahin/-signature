from django.db import models

class Signature(models.Model):
    original_image = models.ImageField(upload_to='original_signatures/')
    uploaded_signature = models.ImageField(upload_to='uploaded_signatures/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Signature {self.id}"
