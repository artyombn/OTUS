from django import forms
from .models import Animal, Food


class AnimalForm(forms.ModelForm):

    name = forms.CharField(
        label="Имя животного",
        initial="default animal",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Input Animal name",
                "class": "form-control",
            }
        ),
    )
    food = forms.ModelMultipleChoiceField(
        queryset=Food.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple(),
    )

    class Meta:
        model = Animal
        fields = "__all__"
        # fields = ("name",) # можно указать только те поля, которые нужны
        exclude = ("age",)
