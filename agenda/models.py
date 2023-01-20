from django.db import models
from datetime import date, time
from django.utils import timezone
from django.core.exceptions import ValidationError
#from smart_selects.db_fields import ChainedForeignKey
#from smart_selects.db_fields import ChainedManyToManyField

class Especialidade(models.Model):
    especialidade = models.CharField(max_length=100)
    
    def __str__(self):
        return self.especialidade

class Cadastrar(models.Model):
    nome = models.CharField(max_length=200)
    crm = models.CharField(max_length=50,unique=True)
    email = models.EmailField(blank=False, max_length=50)
    telefone = models.CharField(max_length=14)
    especialidade = models.ForeignKey(Especialidade,on_delete=models.DO_NOTHING)
    

    def __str__(self):
        return self.nome

def validarData(value):
    hoje = timezone.now().date()
    if value < hoje :
        raise(ValidationError("Data ultrapassada, insira uma data maior ou igual a de hoje"))

class AgendaM(models.Model):
    medico = models.ForeignKey(Cadastrar,on_delete=models.DO_NOTHING)
    data = models.DateField(null=False, validators=[validarData])    
    

class Cliente(models.Model):
    NIVEL = (('F', 'F'),('M', 'M'))
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=30, )
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=14)
    sexo = models.CharField(max_length=1,choices=NIVEL, blank=False, null=False, default='M')


    def __str__(self):
        return self.nome

"""def horarioc(self):
    self.datah = data.Consulta()
    self.horac = horario.Consulta()
    self.nomeM = nome.Cadastrar()
    if self.datah == self.datah:
        if self.horac == hora.Consulta():
            if self.nomeM == nomeM:
               raise(ValidationError("Hora já foi escolhida, escolha outra"))
"""            

class Consulta(models.Model):
    Horarios = (
        ("1", "08:00 ás 09:00"),
        ("2", "09:00 ás 10:00"),
        ("3", "10:00 ás 11:00"),
        ("4", "14:00 ás 15:00"),
        ("5", "15:00 ás 16:00"),
        ("6", "16:00 ás 17:00"),
    )
    
    nomeC = models.CharField('Nome Cliente:',max_length=100)
    especialidade_medica = models.ForeignKey(Especialidade,on_delete=models.DO_NOTHING)
    medico = models.ForeignKey(Cadastrar, on_delete=models.DO_NOTHING) 
    ''',chained_field="especial",
    chained_model_field="especial",show_all=False,auto_choose=True,sort=True'''
    data = models.DateField(null=False, validators=[validarData])
    hora  = models.CharField(max_length=20 , choices=Horarios)
    

    def __str__(self):
        return self.nomeC