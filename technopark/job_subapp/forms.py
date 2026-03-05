from django.forms import ModelForm
from . models import Company,Job

class CompanyForm(ModelForm):
    class Meta:
        model=Company
        fields='__all__'
class JobForm(ModelForm):
    class Meta:
        model=Job
        fields='__all__'