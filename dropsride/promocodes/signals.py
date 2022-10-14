import secrets

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Coupons

@receiver(post_save, sender=Coupons)
def generate_coupon_code(instance, created, *args, **kwargs):
    if created:
        id_string = str(instance.id)
        upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        random_string = "".join(secrets.choice(upper_alpha) for i in range(8))
        instance.code = (random_string + id_string)[-8:]
        instance.save()

