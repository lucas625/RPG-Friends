from django.db import models

class Habilidade(models.Model):
    nome = models.CharField(max_length=100, primary_key=True)
    imagem = models.ImageField(upload_to='habilidades/', null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    levelR = models.DecimalField(null=False, blank=False, max_digits=3, decimal_places=0)

    class Meta:
            verbose_name = 'Habilidade'
            verbose_name_plural = 'Habilidades'
            ordering = ('levelR', 'nome',)

    def __str__(self):
        return self.nome


class Classe(models.Model):
    nome = models.CharField(max_length=100, primary_key=True)
    imagem = models.ImageField(upload_to='classes/', null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    levelR = models.DecimalField(null=False, blank=False, max_digits=3, decimal_places=0)
    habilidades = models.ManyToManyField(Habilidade, blank=True)

    class Meta:
        verbose_name = 'Classe'
        verbose_name_plural = 'Classes'
        ordering = ('levelR', 'nome',)

    def __str__(self):
        return self.nome


class Monstro(models.Model):
    nome = models.CharField(max_length=100, primary_key=True)
    imagem = models.ImageField(upload_to='monstros/', null=False, blank=False)
    level = models.DecimalField(max_digits=3, decimal_places=0, null=False, blank=False)
    vida = models.DecimalField(max_digits=15, decimal_places=0, null=False, blank=False)
    mana = models.DecimalField(max_digits=15, decimal_places=0, null=False, blank=False)
    defesa = models.DecimalField(max_digits=10, decimal_places=0, null=False, blank=False)
    resistencia = models.DecimalField(max_digits=10, decimal_places=0, null=False, blank=False)
    ataque = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)
    exp = models.DecimalField(max_digits=10, decimal_places=0, null=False, blank=False)
    alinhamento = models.CharField(max_length=100, null=False, blank=False)
    classe = models.ForeignKey(Classe, on_delete=models.SET_NULL, null=True, blank=True)
    habilidades = models.ManyToManyField(Habilidade, blank=True)

    class Meta:
        verbose_name = 'Monstro'
        verbose_name_plural = 'Monstros' #avisa ao django que tem o plural
        ordering = ('level', 'nome',)

    def __str__(self):
        return self.nome


class Mapa(models.Model):
    nome = models.CharField(max_length=100, primary_key=True)
    imagem = models.ImageField(upload_to='mapas/', null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    monstros = models.ManyToManyField(Monstro, blank=True)

    class Meta:
        verbose_name = 'Mapa'
        verbose_name_plural = 'Mapas'
        ordering = ('nome',)

    def __str__(self):
        return self.nome


class Raca(models.Model):
    nome = models.CharField(max_length=100, primary_key=True)
    imagem = models.ImageField(upload_to='raças/', null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    classes = models.ManyToManyField(Classe, blank=True)
    habilidades = models.ManyToManyField(Habilidade, blank=True)

    class Meta:
        verbose_name = 'Raça'
        verbose_name_plural = 'Raças'
        ordering = ('nome',)

    def __str__(self):
        return self.nome
