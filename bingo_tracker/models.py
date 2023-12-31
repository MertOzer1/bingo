from django.db import models

# Create your models here.


class BingoSheet(models.Model):
    number1 = models.IntegerField()
    number2 = models.IntegerField()
    number3 = models.IntegerField()
    number4 = models.IntegerField()
    number5 = models.IntegerField()
    number6 = models.IntegerField()
    number7 = models.IntegerField()
    number8 = models.IntegerField()
    number9 = models.IntegerField()
    number10 = models.IntegerField()
    number11 = models.IntegerField()
    number12 = models.IntegerField()
    number13 = models.IntegerField()
    number14 = models.IntegerField()
    number15 = models.IntegerField()

    def __str__(self):
        return f"Bingo Sheet {self.id}"