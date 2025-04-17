from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Items(models.Model):
    ICE_CREAM_CHOICES = [
        ('Chocolate', 'Chocolate'),
        ('Mango ', 'Mango'),
        ('Strawberry', 'Strawberry'),
        ('Vanilla', 'Vanilla'),
        ('Salted Caramel', 'Salted Caramel'),
        ('Mint Chocolate Chip', 'Mint Chocolate Chip'),
        ('Pineapple Coconu ', 'Pineapple Coconu'),
        ('Cookies & Cream ','Cookies & Cream'),
        ('Blue Barry','Blue Barry'),
    ]
    
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    date = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=22, choices=ICE_CREAM_CHOICES)
    dec = models.TextField(default='')
    avalible_ch = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    # Maintain Custamers Record
    
class Customers(models.Model):
    ice_name = models.ForeignKey('Items', on_delete=models.CASCADE, related_name='customers')
    quantity = models.IntegerField(default=1)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    address = models.TextField()
    order_id = models.TextField(default=0)
    email=models.EmailField(default='')
    date = models.DateTimeField(default=timezone.now)
    bill = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}, From: {self.address}"
    
# Multy Images
class IceCreamImage(models.Model):
    person = models.ForeignKey(Items, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"Image for {self.person.name}"
    
class card(models.Model):
    nameoncard=models.TextField()
    cardno=models.TextField()
    amount=models.IntegerField()
    cvc=models.IntegerField()
    
    def __str__(self):
        return f"Card Holder Name, {self.nameoncard} ANd Card No. {self.cardno}"
    
    
# One-to-Many Relationship (Ice Reviews)
class IceReviews(models.Model):
    
    ice = models.ForeignKey(Items, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(Customers, on_delete=models.CASCADE)
    order_id = models.TextField(default=0)
    rating = models.IntegerField(default=0)  # Fixed field type
    review = models.TextField()
    
    def __str__(self):
        return f'{self.user.name} Review for {self.ice.name}'

# Many-to-Many Relationship (Stores)
class Stores(models.Model):
    name = models.CharField(max_length=255)
    location = models.TextField()
    # Ak sa zida stores ma ak sa zida types ke Ice-Creem ho sakte ha
    ice_type = models.ManyToManyField(Items, related_name='stores')

    def __str__(self):
        return self.name

# One-to-One Relationship (Ice Certificate)
class IceCertificate(models.Model):
    # Jab be ham certifcate da ga ak he ice-Creem ko da ga or ak he certifcate da ga
    ice = models.OneToOneField(Items, on_delete=models.CASCADE, related_name="certificate")
    commission=models.TextField(default="")
    image = models.ImageField(upload_to='images/')
    certificate_no = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()
    
    def __str__(self):
        return f"Certificate For {self.ice.name}"
