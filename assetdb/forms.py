from __future__ import absolute_import
import datetime
from datetime import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Fieldset
from datetimewidget.widgets import DateTimeWidget

from crispy_forms.layout import Layout, ButtonHolder, Submit, Div, HTML, Field
    
from . import models	

class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket


class AssetForm(forms.ModelForm):
    class Meta:
        model = models.Asset
        widgets = {
            #Use localization
            'purchase_date': DateTimeWidget(attrs={'class':"datetimeinput"}, usel10n = True)
        }

    def __init__(self, *args, **kwargs):
        super(AssetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Creating a New Asset',
                Div(
                    'model', 'model_details','colour','assigned_to','program', 'notes',
                    css_class='col-md-6'
                ),
                Div(
                    'purchase_date',
                    Field('purchase_price', css_class="hl-num-fields"),
                    'bought_from','warranty_info','status',
                    ButtonHolder(
                    Submit('submit', 'Submit')
                    ),
                    css_class='col-md-6'
                    )
                ),
            )
        