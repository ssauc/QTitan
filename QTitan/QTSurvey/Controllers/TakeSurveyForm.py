from django import forms
from ..models import CompletedSurvey

class TakeSurveyForm(forms.Form):
    def __init__(self, surveyFields, *args, **kwargs):
        super(TakeSurveyForm, self).__init__(*args, **kwargs)

        for i in range(len(surveyFields)):
            self.fields[str(i)] = forms.CharField(
                                                label = '',
                                                help_text = '',
                                                required = True,
                                                widget = forms.HiddenInput(
                                                            attrs = {'value': surveyFields[i].value,
                                                                     'type': 'text',
                                                                     'id': str(i),
                                                                     'orderPosition': str(i + 1)}))
