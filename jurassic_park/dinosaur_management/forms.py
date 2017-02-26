from django import forms
from .models import Dinossauro, Alimentacao, Especie, Genero, Subordem, Ordem

class DinoForm(forms.ModelForm):
    escondido = forms.CharField(widget=forms.HiddenInput(), initial='dinossauro')
    class Meta:
        model = Dinossauro
        fields = ['nome_br', 'custo_individual', 'quantidade', 'imagem', 'f_alimentacao', 'f_especie',
                  'f_genero', 'f_subordem', 'f_ordem']
        labels = {
            'nome_br': 'Nome ',
            'f_alimentacao': 'Alimentação ',
            'f_especie': 'Espécie',
            'f_genero': 'Gênero ',
            'f_subordem': 'Subordem',
            'f_ordem': 'Ordem',
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.Meta.fields:
                self.fields[field].widget.attrs.update({
                        'class': 'u-full-widget',
                    })

class AlimentacaoForm(forms.ModelForm):
    escondido = forms.CharField(widget=forms.HiddenInput(), initial='alimentação')
    class Meta:
        model = Alimentacao
        fields = ['tipo']

class EspecieForm(forms.ModelForm):
    escondido = forms.CharField(widget=forms.HiddenInput(), initial='espécie')
    class Meta:
        model = Especie
        fields = ['nome', 'descricao', 'f_genero']

class GeneroForm(forms.ModelForm):
    escondido = forms.CharField(widget=forms.HiddenInput(), initial='gênero')
    class Meta:
        model = Genero
        fields = ['nome', 'descricao']


class SubordemForm(forms.ModelForm):
    escondido = forms.CharField(widget=forms.HiddenInput(), initial='subordem')
    class Meta:
        model = Subordem
        fields = ['nome', 'descricao']


class OrdemForm(forms.ModelForm):
    escondido = forms.CharField(widget=forms.HiddenInput(), initial='ordem')
    class Meta:
        model = Ordem
        fields = ['nome', 'descricao']

