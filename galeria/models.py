from django.db import models

class Fotografia(models.Model):
    OPCOES_CATEGORIA = [("NEBULOSA","Nebulosas"),
                   ("ESTRELA","Estrelas"),
                   ("GALÁXIA","Galáxias"),
                   ("PLANETA","Planetas")]

    nome = models.CharField(max_length = 100,null=False,blank=False)
    legenda = models.CharField(max_length = 100,null=False,blank=False)
    categoria = models.CharField(max_length = 100,choices=OPCOES_CATEGORIA,null=False,blank=False,default='')
    descricao = models.TextField(null=False,blank=False)
    foto = models.CharField(max_length = 100,null=False,blank=False)

    def __str__(self):
        return f"Fotografia [nome={self.nome}]"