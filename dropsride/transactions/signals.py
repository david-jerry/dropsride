from django.core.cache import cache
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from dropsride.utils.utilities import is_model_instance_changed

from .models import Transaction


@receiver(pre_save, sender=Transaction)
def clear_cache(sender, instance, **kwargs):
    if is_model_instance_changed(instance):
        if cache.has_key(f"users_{instance.owner.id}") and cache.has_key("all_users"):
            cache.delete(f"users_{instance.owner.id}")
            cache.delete(f"all_users")
        cache.delete_pattern("transactions:*")


@receiver(post_save, sender=Transaction)
def create_transaction_slug(sender, instance, created, **kwargs):
    if not instance.slug:
        instance.slug = f"{instance.ref_code}-{instance.id}"
        instance.save(update_fields=["slug"])
