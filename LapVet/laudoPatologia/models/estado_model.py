# coding=utf-8
from django.db import models


class EstadoModel(models.Model):
    STATE_CHOICES = (
		('Acre', 'Acre'), ('Alagoas', 'Alagoas'), ('Amapá', 'Amapá'),
		('Amazonas', 'Amazonas'), ('Bahia', 'Bahia'), ('Ceará', 'Ceará'),
		('Distrito Federal', 'Distrito Federal'), ('Espírito Santo', 'Espírito Santo'),
		('Goiás', 'Goiás'), ('Maranhão', 'Maranhão'), ('Mato Grosso', 'Mato Grosso'),
		('Mato Grosso do Sul', 'Mato Grosso do Sul'), ('Minas Gerais', 'Minas Gerais'),
		('Pará', 'Pará'), ('Paraíba', 'Paraíba'), ('Paraná', 'Paraná'),
		('Pernambuco', 'Pernambuco'), ('Piauí', 'Piauí'), ('Rio de Janeiro', 'Rio de Janeiro'),
		('Rio Grande do Norte', 'Rio Grande do Norte'), ('Rio Grande do Sul', 'Rio Grande do Sul'),
		('Rondônia', 'Rondônia'), ('Roraima', 'Roraima'), ('Santa Catarina', 'Santa Catarina'),
		('São Paulo', 'São Paulo'), ('Sergipe', 'Sergipe'), ('Tocantins', 'Tocantins')
	)
    nome_estado = models.CharField(max_length=100, choices=STATE_CHOICES)

    def __unicode__(self):
        return self.nome_estado

    def __str__(self):
        return self.nome_estado

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"
