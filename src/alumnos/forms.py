from django.forms import ModelForm
#from django.core.exceptions import ValidationError

from .models import Alumno

class AlumnoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for x in self.fields.keys():
            self.fields[x].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['curso'].widget.attrs.update({
                'class': 'form-select'
            })
        self.fields['status'].widget.attrs.update({
                'class': 'form-select'
            })

    class Meta:
        model = Alumno
        fields = ['first_name', 'last_name', 'curso', 'status', 'birthday']

class InscriptosForm(ModelForm):
    class Meta:
        model = Alumno
        fields = ['first_name', 'last_name', 'curso']

#    first_name = forms.CharField()
#    last_name = forms.CharField()
#    birthday = forms.DateTimeField()

#    def save(self, commit=False):
#        first_name = self.cleaned_data['first_name']
#        last_name = self.cleaned_data['last_name']
#        birthday = self.cleaned_data['birthday']
#        alumno = Alumno(first_name=first_name, last_name=last_name, 
#                        birthday=birthday)
#        if commit:
#            alumno.save()
#        return alumno

#    def clean_first_name(self):
#        data = self.cleaned_data['first_name']
#        if len (data) < 5:
#            raise ValidationError("El nombre es corto.")
#        return data
