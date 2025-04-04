from django.db import models

ESPECIALIDADE_CHOICES = (
    ("Pedriatra", "Pediatra"),
    ("Médico geral", "Médico geral"),
    ("Ginecologista", "Ginecologista")
)

STATUS_MEDICO = {
    ('agendado', 'agendado'),
    ('realizado', 'realizado'),
    ('cancelado', 'cancelado')
}

class Medico(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    especialidade = models.CharField(max_length=255, choices=ESPECIALIDADE_CHOICES)
    crm = models.CharField(max_length=255, unique=True, null=False, blank=False)
    email = models.EmailField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    paciente = models.CharField(max_length=255, null=False, blank=False)
    data = models.DateTimeField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=STATUS_MEDICO)

    def __str__(self):
        return self.paciente