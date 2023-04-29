from decimal import Decimal

from django.shortcuts import get_object_or_404

from dropsride.currency.models import Currency


def is_model_instance_changed(instance):
    """
    Check if a model instance has changed by comparing its current state to the
    original state (as it was when it was first loaded from the database).

    Args:
        instance: a model instance

    Returns:
        True if any fields have changed, False otherwise
    """
    if instance.id:
        # Get the original instance from the database
        model_class = instance.__class__
        original_instance = model_class.objects.get(pk=instance.pk)

        # Compare the fields of the original instance to the current instance
        for field_name in instance._meta.fields:
            if getattr(instance, field_name.name) != getattr(
                original_instance, field_name.name
            ):
                return True

        return False

    # New instance, assume all fields are dirty
    return True


def is_uuid_model_instance_changed(instance):
    """
    Check if a model instance has changed by comparing its current state to the
    original state (as it was when it was first loaded from the database).

    Args:
        instance: a model instance

    Returns:
        True if any fields have changed, False otherwise
    """
    if instance.uuid:
        # Get the original instance from the database
        model_class = instance.__class__
        original_instance = model_class.objects.get(uuid=instance.uuid)

        # Compare the fields of the original instance to the current instance
        for field_name in instance._meta.fields:
            if getattr(instance, field_name.name) != getattr(
                original_instance, field_name.name
            ):
                return True

        return False

    # New instance, assume all fields are dirty
    return True


def convert_to_dollar(amount):
    amount = Decimal(amount)
    usd = get_object_or_404(Currency, code="USD")
    return Decimal(usd.price / amount)
