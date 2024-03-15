from django.db import models

# Create your models here.
class flower(models.Model):
    # firstname = models.CharField(max_length=50)
    # lastname = models.CharField(max_length=50)
    # dependants = models.IntegerField()
    # applicantincome = models.IntegerField()
    # coapplicantincome = models.IntegerField()
    # loanamt = models.IntegerField()
    # loanterm = models.IntegerField()
    # credithistory = models.IntegerField()
    # gender = models.CharField(max_length=15, choices=(
    #     ('Male', 'Male'),
    #     ('Female', 'Female'),
    # ))
    # married = models.CharField(max_length=15, choices=(
    #     ('Yes', 'Yes'),
    #     ('No', 'No')
    # ))
    # graduatededucation = models.CharField(max_length=15, choices=(
    #     ('Graduate', 'Graduated'),
    #     ('Not_Graduate', 'Not_Graduate')
    # ))
    # selfemployed = models.CharField(max_length=15, choices=(
    #     ('Yes', 'Yes'),
    #     ('No', 'No')
    # ))
    # area = models.CharField(max_length=15, choices=(
    #     ('Rural', 'Rural'),
    #     ('Semiurban', 'Semiurban'),
    #     ('Urban', 'Urban')
    # ))

    # def __str__(self):
    #     return self.firstname

    name = models.CharField(max_length=20)
    Sepal_Length = models.FloatField()
    Sepal_Width = models.FloatField()
    Petal_Length = models.FloatField()
    Petal_Width = models.FloatField()

    def __str__(self):
        return self.name