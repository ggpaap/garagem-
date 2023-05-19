from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    site = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Acessorio(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nome

class Cor(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Cor"
        verbose_name_plural = "Cor"

class Modelo(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Veiculo(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria,on_delete=models.PROTECT)
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT)
    ano = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return self .preco.modelo.marca.ano.cor

# Create your models here.
