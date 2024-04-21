from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
     
    class Meta:
        db_table = "Users"
    
    def __str__(self) -> str:
        return super().__str__()