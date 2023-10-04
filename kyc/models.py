from django.db import models
from accounts.models import User

# Create your models here.
KYC_CHOICES =(
  ("National ID", "National ID"),
  ("International Passport", "International Passport"),
  ("Voter ID", "Voter ID"),
  ("Driving License", "Driving License"),
)

class KYC(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  kyc_type = models.CharField(max_length=20, choices=KYC_CHOICES)
  kyc_number = models.CharField(max_length=20)
  kyc_image = models.ImageField(upload_to='/media/kyc_images/', blank=True)
  kyc_status = models.BooleanField(default=False)
  kyc_date = models.DateField(auto_now_add=True)

  def __str__(self):
    return self.kyc_type

  class Meta:
    verbose_name_plural = "KYC"
    db_table = "KYC"
    indexes = [
      models.Index(fields=['user','kyc_type', 'kyc_number', 'kyc_image', 'kyc_status', 'kyc_date'])
    ]
    ordering = ['-kyc_date']




