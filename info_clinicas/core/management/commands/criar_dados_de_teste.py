from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError

from info_clinicas.clinicas.models import Clinica
from info_clinicas.especialidade.models import Especialidade


class Command(BaseCommand):
    help = 'Comando que popula o banco com dados de teste'

    def criar_admin(self):
        User = get_user_model()

        User.objects.create_superuser('admin', 'admin@madmin.com', 'admin')

        self.stdout.write(
            self.style.SUCCESS(f'usuário admin criado com sucesso! admin:admin')
        )

    def criar_especialidades(self):
        lista = ['Acupuntura', 'Alergia e Imunologia', 'Anestesiologia', 'Angiologia', 'Cancerologia', 'Cardiologia',
                 'Cirurgia Cardiovascular', 'Cirurgia da Mão', 'Cirurgia de Cabeça e Pescoço',
                 'Cirurgia do Aparelho Digestivo', 'Cirurgia Geral', 'Cirurgia Pediátrica', 'Cirurgia Plástica',
                 'Cirurgia Torácica', 'Cirurgia Vascular', 'Clínica Médica', 'Coloproctologia', 'Dermatologia',
                 'Endocrinologia e Metabologia', 'Endoscopia', 'Gastroenterologia', 'Genética Médica', 'Geriatria',
                 'Ginecologia e Obstetrícia', 'Hematologia e Hemoterapia', 'Homeopatia', 'Infectologia',
                 'Mastologia', 'Medicina de Família e Comunidade', 'Medicina do Trabalho', 'Medicina de Tráfego',
                 'Medicina Esportiva', 'Medicina Física e Reabilitação', 'Medicina Intensiva',
                 'Medicina Legal e Perícia Médica', 'Medicina Nuclear', 'Medicina Preventiva e Social', 'Nefrologia',
                 'Neurocirurgia', 'Neurologia', 'Nutrologia', 'Oftalmologia', 'Ortopedia e Traumatologia',
                 'Otorrinolaringologia', 'Patologia', 'Patologia Clínica/Medicina Laboratorial', 'Pediatria',
                 'Pneumologia', 'Psiquiatria', 'Radiologia e Diagnóstico por Imagem', 'Radioterapia', 'Reumatologia',
                 'Urologia']

        for i in lista:
            especialidade = Especialidade(nome_especialidade=i)
            especialidade.save()

        self.stdout.write(
            self.style.SUCCESS(f'Especialidades criadas com sucesso!')
        )

    def criar_clinica(self):
        nome = 'Clinica Teste'
        cnpj = '0000000000'
        site = 'clinicateste.com'
        endereco = 'Rua x, 47'
        cidade = 'São Paulo'
        estado = 'SP'
        telefone = '(11) 2222-4433'
        responsavel = 'Fulaninho'

        nova_clinica = Clinica(
            nome=nome,
            cnpj=cnpj,
            site=site,
            endereco=endereco,
            cidade=cidade,
            estado=estado,
            telefone=telefone,
            responsavel=responsavel,
        )

        try:
            clinica_teste = Clinica.objects.get(nome=nome)
        except Clinica.DoesNotExist:
            clinica_teste = None

        if clinica_teste:
            raise CommandError(f'Clinica já cadastrada. ID: {clinica_teste.id}')

        nova_clinica.save()

        self.stdout.write(
            self.style.SUCCESS(f'{nova_clinica.nome} criada com sucesso! ID: {nova_clinica.id}')
        )
    def criar_medicos(self):
        # pegar primeira clinica cadastrada
        self.stdout.write(
            self.style.SUCCESS(f'medicos criados com sucesso!')
        )

    def criar_pacientes(self):
        # pegar primeira clinica cadastrada
        self.stdout.write(
            self.style.SUCCESS(f'pacientes criados com sucesso!')
        )

    def criar_disponibilidades(self):
        self.stdout.write(
            self.style.SUCCESS(f'disponibilidades criadas com sucesso!')
        )

    def criar_agendamentos(self):
        self.stdout.write(
            self.style.SUCCESS(f'agendamentos criados com sucesso!')
        )

    def handle(self, *args, **options):
        self.criar_admin()
        self.criar_especialidades()
        self.criar_clinica()
        self.criar_medicos()
        self.criar_pacientes()
        self.criar_disponibilidades()
        self.criar_agendamentos()
