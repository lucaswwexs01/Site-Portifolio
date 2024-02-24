from django.db import models
from django.core.mail import send_mail
from django.conf import settings

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # chama o método save original

        # cria o corpo da mensagem com todas as informações do formulário
        message_body = f"Nome: {self.name}\nEmail: {self.email}\nAssunto: {self.subject}\nMensagem: {self.message}"

        # envia o email
        send_mail(
            f"Novo contato de {self.email} - {self.subject}",  # adiciona o email e o assunto no assunto do email
            message_body,
            settings.EMAIL_HOST_USER,
            ['lucaswwexs@gmail.com'], 
        )
