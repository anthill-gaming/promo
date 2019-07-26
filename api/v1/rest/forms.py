from anthill.framework.forms.orm import (
    ModelForm, ModelUpdateForm, ModelCreateForm, ModelSearchForm)
from promo.models import PromoCode


class EditPromoCodeForm(ModelForm):
    class Meta:
        model = PromoCode
        exclude = ['key']
