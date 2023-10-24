from django.db import  models


# Create your models here.

class Mark(models.Model):
    mark_id = models.AutoField(primary_key=True)
    mark_name = models.CharField(max_length=100, null=True, blank=True)
    mark_logo = models.ImageField(upload_to = 'media/mark', null=True,blank=True)
    mark_image = models.ImageField(upload_to="media/mark", null=True, blank=True)

    def __str__(self):
        return f"{self.mark_name}"

class Car(models.Model):
    DRIVETYPE = [('4WD','4WD'),('2WD','2WD')]
    FUELTYPE = [('DIESEL','DIESEL'),('GASOLINE','GASOLINE'),('GAS','GAS')]
    TRANSMISSION = [('MANUAL','MANUAL'),('AUTOMATIK','AUTOMATIK')]
    car_id = models.AutoField(primary_key=True)
    car_image = models.ImageField(upload_to='media/car',null=True,blank=True)
    car_name = models.CharField(max_length=100, null=True, blank=True)
    car_text = models.TextField(max_length=300,null=True,blank=True)
    car_price = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    car_style = models.CharField(max_length=100,null=True,blank=True)
    car_excolor = models.CharField(max_length=100,null=True,blank=True)
    car_intcolor = models.CharField(max_length=100,null=True,blank=True)
    car_mpg1 = models.IntegerField(null=True,blank=True)
    car_mpg2 = models.IntegerField(null=True,blank=True)
    car_engine = models.CharField(max_length=100,null=True,blank=True)
    car_drivetype = models.CharField(max_length=4,choices=DRIVETYPE,default='4WD',null=True,blank=True)
    car_fueltype = models.CharField(max_length=10,choices=FUELTYPE,default='GASOLINE',null=True,blank=True)
    car_transmission = models.CharField(max_length=10,choices=TRANSMISSION,default='MANUAL',null=True,blank=True)
    car_ns = models.CharField(max_length=100,null=True,blank=True)
    car_dpp = models.CharField(max_length=100,null=True,blank=True)
    car_fjdssp = models.CharField(max_length=100,null=True,blank=True)
    car_rrstp = models.CharField(max_length=100,null=True,blank=True)
    car_wcp = models.CharField(max_length=100,null=True,blank=True)
    car_cp = models.CharField(max_length=100,null=True,blank=True)
    car_bwlp = models.CharField(max_length=100,null=True,blank=True)
    car_edp = models.CharField(max_length=100,null=True,blank=True)
    car_lccvp = models.CharField(max_length=100,null=True,blank=True)
    car_sp = models.CharField(max_length=100,null=True,blank=True)
    car_8s = models.CharField(max_length=100,null=True,blank=True)
    car_dvd = models.CharField(max_length=100,null=True,blank=True)
    car_dp = models.CharField(max_length=100,null=True,blank=True)
    car_fccvp = models.CharField(max_length=100,null=True,blank=True)
    car_pcapp = models.CharField(max_length=100,null=True,blank=True)
    car_vcp = models.CharField(max_length=100,null=True,blank=True)
    car_amfm = models.CharField(max_length=100,null=True,blank=True)
    car_mark = models.ForeignKey(Mark,on_delete=models.CASCADE,null=True,blank=True)
    car_rating = models.TextField(max_length=300 ,null=True , blank=True)

    def __str__(self):
        return f"{self.car_name}"

class Image(models.Model):
    
    image_id = models.AutoField(primary_key=True)
    image_image = models.ImageField(upload_to="media/carimage",null=True,blank=True)
    image_car = models.ForeignKey(Car,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return f"{self.image_image}"

class Book(models.Model):
    BookNow_id = models.AutoField(primary_key=True)
    BookNow_pick = models.CharField(max_length=40,default="HEADQUARTER",null=True,blank=True)
    BookNow_dropoff = models.CharField(max_length=40,default="TIRANA INTERNATION AIRPORT",null=True,blank=True)
    BookNow_datep = models.DateTimeField(null=True,blank=True)
    BookNow_dated = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return f"{self.BookNow_id}"

class Subscribes(models.Model):
    subscribe_email = models.EmailField()
    
    def __str__(self):
        return f"{self.subscribe_email}"

