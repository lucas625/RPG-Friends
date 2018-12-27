from django.db import models

class Monstro(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    imagem = models.ImageField(upload_to='monstros/', null=False, blank=False)
    level = models.DecimalField(max_digits=3, decimal_places=0, null=False, blank=False)
    vida = models.DecimalField(max_digits=15, decimal_places=0, null=False, blank=False)
    mana = models.DecimalField(max_digits=15, decimal_places=0, null=False, blank=False)
    defesa = models.DecimalField(max_digits=10, decimal_places=0, null=False, blank=False)
    resistencia = models.DecimalField(max_digits=10, decimal_places=0, null=False, blank=False)
    ataque = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)
    exp = models.DecimalField(max_digits=10, decimal_places=0, null=False, blank=False)
    alinhamento = models.CharField(max_length=100, null=False, blank=False)
    classe = models.CharField(max_length=100, null=False, blank=False)
    class Meta:
        verbose_name = 'Monstro'
        verbose_name_plural = 'Monstros' #avisa ao django que tem o plural

    def __str__(self):
        return self.nome
