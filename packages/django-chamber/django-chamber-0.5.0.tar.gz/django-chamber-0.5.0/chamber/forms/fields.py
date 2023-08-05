from django import forms
from django.utils.translation import ugettext


class DecimalField(forms.DecimalField):

    def __init__(self, *args, **kwargs):
        self.step = kwargs.pop('step', 'any')
        self.min = kwargs.pop('min', None)
        self.max = kwargs.pop('max', None)
        super().__init__(*args, **kwargs)

    def widget_attrs(self, widget):
        attrs = super().widget_attrs(widget)
        attrs['step'] = self.step
        if self.min is not None:
            attrs['min'] = self.min
        if self.max is not None:
            attrs['max'] = self.max
        return attrs


class PriceNumberInput(forms.NumberInput):

    def __init__(self, currency, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.placeholder = currency


class PriceField(DecimalField):

    widget = PriceNumberInput

    def __init__(self, *args, **kwargs):
        currency = kwargs.pop('currency', ugettext('CZK'))
        kwargs.setdefault('max_digits', 10)
        kwargs.setdefault('decimal_places', 2)
        if 'widget' not in kwargs:
            kwargs['widget'] = PriceNumberInput(currency)
        super().__init__(*args, **kwargs)
