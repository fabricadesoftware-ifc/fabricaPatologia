from django.db import models



class ImagensModel(models.Model):
    descricao_imagem = models.CharField(max_length=150)
    imagem = models.ImageField(upload_to='imagens', null=True, blank=True)



    def __str__(self):
        return self.descricao_imagem