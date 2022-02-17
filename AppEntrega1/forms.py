from django.forms import Form, ImageField

class AvatarFormulario(Form):
    imagen = ImageField(required=True)