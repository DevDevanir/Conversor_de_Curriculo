# Este arquivo define os formulários Django para o nosso aplicativo.

from django import forms

class UploadFileForm(forms.Form):
    # Campo para o upload do arquivo HTML
    html_file = forms.FileField(
        label='Selecione o arquivo HTML',
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file', 'accept': '.html'})
    )
    
    # Campo para o nome do arquivo de saída (sem extensão)
    output_filename = forms.CharField(
        label='Nome do arquivo de saída (sem extensão)',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: meu_curriculo'})
    )
    
    # Opções para o formato de saída
    OUTPUT_FORMAT_CHOICES = [
        ('pdf', 'PDF'),
        ('png', 'PNG'),
        ('jpeg', 'JPEG'),
    ]
    output_format = forms.ChoiceField(
        label='Formato de Saída',
        choices=OUTPUT_FORMAT_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}), # Usar RadioSelect para botões
        initial='pdf' # Valor padrão
    )