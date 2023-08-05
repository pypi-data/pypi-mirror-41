from django.db import models

from .constants import TYPES


def clone_model(original_model):
    """
    Create a copy of a Django mode
    :param original_model: models.Model
    :return: models.Model
    """
    # Create a local copy of the model to avoid references errors
    model = original_model.__class__.objects._all().get(pk=original_model.id)

    # This block of codes forces Django to clone to model and the simple fields
    # CharField, TextField etc...
    destination_model = model
    destination_model.pk = None
    destination_model.type = TYPES.PUBLISHED
    destination_model.save(broadcast_draft=False)

    # Search for the ManyToManyField and copy it's content into the model
    all_model_fields = original_model._meta.get_fields()
    for field in all_model_fields:
        if isinstance(field, models.ManyToManyField):
            # Select the through model
            through = field.remote_field.through

            filter_params = {
                original_model._meta.model_name: original_model,
            }
            all_link_models = through.objects.filter(**filter_params)

            for link_model in all_link_models:
                link_model.pk = None
                setattr(link_model, original_model._meta.model_name, destination_model)
                link_model.save()

    destination_model.save(broadcast_draft=False)
    return destination_model
