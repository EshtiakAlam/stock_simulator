from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    national_id = models.CharField(primary_key=True, unique=True, max_length=15)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()

class Company(models.Model):
    name = models.CharField(max_length=255)
    sector = models.CharField(max_length=255)
    nav = models.DecimalField(max_digits=20, decimal_places=10)
    dividend = models.DecimalField(max_digits=10, decimal_places=2)
    first_quarter = models.DecimalField(max_digits=15, decimal_places=2)
    second_quarter = models.DecimalField(max_digits=15, decimal_places=2)
    third_quarter = models.DecimalField(max_digits=15, decimal_places=2)

    @property
    def eps(self):
        total_earnings = self.first_quarter + self.second_quarter + self.third_quarter
        return total_earnings




# Create your models here.
class TradingStatus(models.Model):
    stock = models.ForeignKey(Company, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    share_price = models.DecimalField(max_digits=15, decimal_places=2)
    volume = models.IntegerField()
    total_trades = models.IntegerField()

    @property
    def pe_ratio(self):
        eps = self.stock.eps
        if eps == 0:
            return 0
        return self.share_price / eps

class News(models.Model):
    official_news = models.TextField()
    date = models.DateField()
    directors_share_buy = models.DecimalField(max_digits=15, decimal_places=2)
    directors_share_sell = models.DecimalField(max_digits=15, decimal_places=2)