from anthill.platform.api.rest.handlers.detail import DetailMixin
from anthill.platform.api.rest.handlers.edit import (
    CreatingMixin, UpdatingMixin, DeletionMixin, ModelFormHandler)
from anthill.platform.api.rest.handlers.list import ListHandler
from promo.models import PromoCode
from .forms import EditPromoCodeForm


class PromoCodeHandler(CreatingMixin, UpdatingMixin, DeletionMixin, DetailMixin,
                       ModelFormHandler):
    """Multiple operations with promo code items."""
    model = PromoCode

    def get_form_class(self):
        """Return the form class to use in this handler."""
        if self.request.method in ('PUT', 'POST'):
            self.form_class = EditPromoCodeForm
        form_class = super().get_form_class()
        return form_class


class PromoCodeListHandler(ListHandler):
    """Get list of promo codes."""
    model = PromoCode


class UsePromoCode(ModelFormHandler):
    """Use promo code."""
    model = PromoCode

    async def put(self, *args, **kwargs):
        # noinspection PyAttributeOutsideInit
        self.object = await self.get_object()
        await self.object.use()

    async def post(self, *args, **kwargs):
        await self.put(*args, **kwargs)
