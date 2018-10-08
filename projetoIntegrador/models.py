from django.db import models



# Create your models here.

class PalestranteInstrutor(models.Model):

    TIPO_CHOICES = (
        ("palestrante", "Palestrante"),
        ("instrutor", "Instrutor"),
    )

    nome_palestrante_instrutor = models.CharField(max_length=100, null=False)
    mini_curriculo = models.TextField(max_length=300, null=False)
    foto_palestrante = models.ImageField(upload_to='images')
    tipo = models.CharField(max_length=15, choices=TIPO_CHOICES)

    class Meta:
        verbose_name_plural= "palestrantes"

    def __str__(self):
        return self.nome_palestrante_instrutor

class Evento(models.Model):
    nome_evento = models.CharField(max_length=150, null=False)
    descricao_evento = models.TextField(max_length=1500, null=False)
    edicao = models.CharField(max_length=5, null=False)
    local_evento = models.CharField(max_length=50, null=False)
    data_evento = models.DateField(null=False, verbose_name="Data do Evento")


    class Meta:
        verbose_name_plural = "eventos"

    def __str__(self):
        return self.nome_evento


class Avaliacao(models.Model):
    enunciado = models.TextField(max_length=300, null=False)
    qtd_respostas = models.IntegerField(null=False)
    evento = models.ForeignKey(Evento, on_delete=False)

    def __str__(self):
        return self.enunciado

class Questoes(models.Model):
    enunciado_questao = models.TextField(max_length=300)
    id_avaliacao = models.ForeignKey(Avaliacao, on_delete=False)

    def __str__(self):
        return self.enunciado_questao

class Alternativas(models.Model):
    descricao_alternativa = models.TextField(max_length=300, null=False)
    resposta = models.BooleanField()
    id_questao = models.ForeignKey(Questoes, on_delete=False)


    def __str__(self):
        return self.descricao_alternativa

class PalestraOficina(models.Model):
    TIPO_PO_CHOICES = (
        ("palestra", "Palestra"),
        ("oficina", "Oficina"),
    )
    nome_palestra =models.CharField(max_length=100, null=False)
    descricao = models.TextField(max_length=300, null=False)
    data_po = models.DateField(null=False, verbose_name="Data")
    hora_po = models.TimeField(null=False)
    duracao = models.TimeField(null=False)
    tipo = models.CharField(max_length=10, null=False, choices=TIPO_PO_CHOICES)
    id_evento = models.ForeignKey(Evento, on_delete=False)
    id_palestrante_instrutor = models.ForeignKey(PalestranteInstrutor, on_delete=False)

    def __str__(self):
        return self.nome_palestra
    class Meta:
        verbose_name_plural = "palestras_oficinas"


class Pessoa(models.Model):
    nome_pessoa = models.CharField(max_length=100, null=False)
    telefone = models.CharField(max_length=30, null=False)
    email = models.EmailField(max_length=100, null=False)
    cpf = models.CharField(max_length=16, null=False)
    def __str__(self):
        return self.nome_pessoa

class Matricula(models.Model):
    data_matricula = models.DateField(null=False, verbose_name="Data da Matricula")
    id_palestra_oficina = models.ForeignKey(PalestraOficina, on_delete=False)
    id_pessoa = models.ForeignKey(Pessoa, on_delete=False)
    def __str__(self):

        return self.data_matricula

class Sugestoes(models.Model):
    sugetao = models.TextField(max_length=300)
    pessoa_sugestoes = models.ManyToManyField(Pessoa)

    def __str__(self):
        return self.sugetao