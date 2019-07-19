from anthill.platform.api.rest.handlers.detail import DetailMixin
from anthill.platform.api.rest.handlers.edit import (
    CreatingMixin, UpdatingMixin, DeletionMixin, ModelFormHandler)
from anthill.platform.api.rest.handlers.list import ListHandler
from promo.models import PromoCode
from .forms import ChangePromoCodeForm


class PromoCodeHandler(CreatingMixin, UpdatingMixin, DeletionMixin, DetailMixin,
                       ModelFormHandler):
    """
    Multiple operations with promo code items:
        fetching, creating, updating and deleting.
    """
    model = PromoCode

    def get_form_class(self):
        """Return the form class to use in this handler."""
        if self.request.method in ('GET',):  # Detail
            form_class = super().get_form_class()
        else:
            form_class = ChangePromoCodeForm

        if self.request.method in ('PUT',):  # Updating
            # Patching form meta
            setattr(form_class.Meta, 'all_fields_optional', True)
            setattr(form_class.Meta, 'assign_required', False)
        return form_class


class PromoCodeListHandler(ListHandler):
    """Get list of promo codes."""
    model = PromoCode
