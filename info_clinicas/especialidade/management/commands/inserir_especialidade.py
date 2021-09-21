from django.core.management.base import BaseCommand, CommandError

from info_clinicas.especialidade.models import Especialidade


class Command(BaseCommand):
    help = 'Comando que insere a base de especialidade default'

    def handle(self, *args, **options):

        cria = Especialidade(nome_especialidade='Acupuntura')
        cria.save()

    lista = ['Alergia e Imunologia', 'Anestesiologia', 'Angiologia', 'Cancerologia', 'Cardiologia', 'Cirurgia Cardiovascular', 'Cirurgia da Mão', 'Cirurgia de Cabeça e Pescoço', 'Cirurgia do Aparelho Digestivo', 'Cirurgia Geral', 'Cirurgia Pediátrica', 'Cirurgia Plástica', 'Cirurgia Torácica', 'Cirurgia Vascular', 'Clínica Médica', 'Coloproctologia', 'Dermatologia', 'Endocrinologia e Metabologia', 'Endoscopia', 'Gastroenterologia', 'Genética Médica', 'Geriatria', 'Ginecologia e Obstetrícia', 'Hematologia e Hemoterapia', 'Homeopatia', 'Infectologia',
             'Mastologia', 'Medicina de Família e Comunidade', 'Medicina do Trabalho', 'Medicina de Tráfego', 'Medicina Esportiva', 'Medicina Física e Reabilitação', 'Medicina Intensiva', 'Medicina Legal e Perícia Médica', 'Medicina Nuclear', 'Medicina Preventiva e Social', 'Nefrologia', 'Neurocirurgia', 'Neurologia', 'Nutrologia', 'Oftalmologia', 'Ortopedia e Traumatologia', 'Otorrinolaringologia', 'Patologia', 'Patologia Clínica/Medicina Laboratorial', 'Pediatria', 'Pneumologia', 'Psiquiatria', 'Radiologia e Diagnóstico por Imagem', 'Radioterapia', 'Reumatologia', 'Urologia']

    for i in lista:
        especialidade = Especialidade(nome_especialidade=i)
        especialidade.save()
