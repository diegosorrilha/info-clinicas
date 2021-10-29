from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError

from info_clinicas.agendamento.models import Agendamento
from info_clinicas.clinicas.models import Clinica
from info_clinicas.especialidade.models import Especialidade
from info_clinicas.medicos.models import Medicos, Disponibilidade
from info_clinicas.pacientes.models import Paciente


class Command(BaseCommand):
    help = 'Comando que popula o banco com dados de teste'

    def criar_admin(self):
        User = get_user_model()
        try:
            user_admin = User.objects.get(username='admin')
        except User.DoesNotExist:
            user_admin = None

        if user_admin:
            self.stdout.write(
                self.style.ERROR(f'Usuário: {user_admin.username} já cadastrado. ID: {user_admin.id}')
            )

        else:
            User.objects.create_superuser('admin', 'admin@madmin.com', 'admin')

            self.stdout.write(
                self.style.SUCCESS(f'Usuário: admin criado com sucesso! admin:admin')
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
            try:
                especialidade_teste = Especialidade.objects.get(nome_especialidade=i)
            except Especialidade.DoesNotExist:
                especialidade_teste = None

            if especialidade_teste:
                self.stdout.write(
                    self.style.ERROR(f'Especialidade: "{especialidade_teste.nome_especialidade}" já cadastrada. '
                                     f'ID: {especialidade_teste.id}'
                                     )
                )
                continue

            especialidade = Especialidade(nome_especialidade=i)
            especialidade.save()

            self.stdout.write(
                self.style.SUCCESS(f'Especialidade: "{especialidade.nome_especialidade}" cadastrada com sucesso. '
                                   f'ID: {especialidade.id}'
                                   )
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
            self.stdout.write(
                self.style.ERROR(f'Clinica: "{clinica_teste.nome}" já cadastrada. ID: {clinica_teste.id}')
            )

        else:
            nova_clinica.save()

            self.stdout.write(
                self.style.SUCCESS(f'Clínica: "{nova_clinica.nome}" criada com sucesso! ID: {nova_clinica.id}')
            )

    def criar_medicos(self):
        clinica_teste = Clinica.objects.get(nome='Clinica Teste')

        medicos = [
            {
                'nome_completo': 'Dr Alfredo',
                'sexo': 'Masculino',
                'cpf': '11122233344',
                'email': 'alfredo@gmail.com',
                'data_nascimento': '',
                'telefone': '5511988887744',
                'endereco': 'Rua das flores, 47',
                'bairro': 'Jardim da saudade',
                'cidade': 'São Paulo',
                'pais': 'Brasil',
                'CEP': '07456-000',
                'CRM': '1234567',
            },
            {
                'nome_completo': 'Dr Bernardo',
                'sexo': 'Masculino',
                'cpf': '11122233344',
                'email': 'bernardo@gmail.com',
                'data_nascimento': '',
                'telefone': '5511988887744',
                'endereco': 'Rua da justiça, 74',
                'bairro': 'Jardim Europa',
                'cidade': 'São Bernardo do Campo',
                'pais': 'Brasil',
                'CEP': '07456-000',
                'CRM': '1234567',
            },
        ]

        for m in medicos:
            try:
                medico_teste = Medicos.objects.get(nome_completo=m['nome_completo'])
            except Medicos.DoesNotExist:
                medico_teste = None

            if medico_teste:
                self.stdout.write(
                    self.style.ERROR(f'Médico: "{medico_teste.nome_completo}" já cadastrado. ID: {medico_teste.id}')
                )
                continue

            medico = Medicos(
                nome_completo=m['nome_completo'],
                sexo=m['sexo'],
                cpf=m['cpf'],
                email=m['email'],
                data_nascimento='1980-10-01',
                telefone=m['telefone'],
                endereco=m['endereco'],
                bairro=m['bairro'],
                cidade=m['cidade'],
                pais=m['pais'],
                CEP=m['CEP'],
                CRM=m['CRM'],
                clinica=clinica_teste
            )

            medico.save()

            self.stdout.write(
                self.style.SUCCESS(f'Médico: "{medico.nome_completo}" criado com sucesso! ID: {medico.id}')
            )

    def criar_pacientes(self):
        clinica_teste = Clinica.objects.get(nome='Clinica Teste')

        pacientes = [
            {
                'nome_completo': 'João Roberto da Silva',
                'sexo': 'Masculino',
                'data_nascimento': '1985-01-01',
                'telefone': '5511985554477',
                'endereço': 'Rua Noel Rosa, 13',
                'cidade': 'Guarulhos',
                'estado': 'São Paulo',
                'email': 'joaozim@gmail.com',
            },
            {
                'nome_completo': 'Ana Cristina Soares',
                'sexo': 'Feminino',
                'data_nascimento': '1988-09-15',
                'telefone': '5511985557788',
                'endereço': 'Rua Huberto Porto, 55',
                'cidade': 'Guarulhos',
                'estado': 'São Paulo',
                'email': 'acristina@gmail.com',
            },

        ]

        for p in pacientes:
            try:
                paciente_teste = Paciente.objects.get(nome_completo=p['nome_completo'])
            except Paciente.DoesNotExist:
                paciente_teste = None

            if paciente_teste:
                self.stdout.write(
                    self.style.ERROR(f'Paciente: "{paciente_teste.nome_completo}" já cadastrado. ID: {paciente_teste.id}')
                )
                continue

            paciente = Paciente(
                nome_completo=p['nome_completo'],
                sexo=p['sexo'],
                data_nascimento='1980-10-01',
                telefone=p['telefone'],
                endereço=p['endereço'],
                cidade=p['cidade'],
                estado=p['estado'],
                email=p['email'],
                clinica=clinica_teste
            )

            paciente.save()

            self.stdout.write(
                self.style.SUCCESS(f'Paciente: "{paciente.nome_completo}" criado com sucesso! ID: {paciente.id}')
            )

    def criar_disponibilidades(self):
        '''
            class Disponibilidade(models.Model):

            disponivel = models.BooleanField(default=True)
            medico = models.ForeignKey(Medicos, on_delete=models.PROTECT)
            data = models.DateField(verbose_name="Data disponível", auto_now=False, auto_now_add=False)
            hora = models.TimeField(verbose_name="Horário disponível", auto_now=False, auto_now_add=False)
            clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE, blank=True, null=False)
        '''
        clinica_teste = Clinica.objects.get(nome='Clinica Teste')
        medico_1_teste = Medicos.objects.get(nome_completo='Dr Alfredo')
        medico_2_teste = Medicos.objects.get(nome_completo='Dr Bernardo')

        disp_medico1 = Disponibilidade(
            disponivel=True,
            medico=medico_1_teste,
            data='2021-12-24',
            hora='12:30',
            clinica=clinica_teste
        )

        disp_medico1.save()

        self.stdout.write(
            self.style.SUCCESS(f'Disponibilidade: "{disp_medico1.data} - {disp_medico1.medico.nome_completo}" criada com sucesso! ID: {disp_medico1.id}')
        )

        disp_medico1 = Disponibilidade(
            disponivel=False,
            medico=medico_1_teste,
            data='2021-12-25',
            hora='12:30',
            clinica=clinica_teste
        )

        disp_medico1.save()

        self.stdout.write(
            self.style.SUCCESS(f'Disponibilidade: "{disp_medico1.data} - {disp_medico1.medico.nome_completo}" criada com sucesso! ID: {disp_medico1.id}')
        )

        disp_medico2 = Disponibilidade(
            disponivel=True,
            medico=medico_2_teste,
            data='2021-12-24',
            hora='12:30',
            clinica=clinica_teste
        )

        disp_medico2.save()

        self.stdout.write(
            self.style.SUCCESS(f'Disponibilidade: "{disp_medico2.data} - {disp_medico2.medico.nome_completo}" criada com sucesso! ID: {disp_medico2.id}')
        )

        disp_medico2 = Disponibilidade(
            disponivel=False,
            medico=medico_2_teste,
            data='2021-12-25',
            hora='12:30',
            clinica=clinica_teste
        )

        disp_medico2.save()

        self.stdout.write(
            self.style.SUCCESS(f'Disponibilidade: "{disp_medico2.data} - {disp_medico2.medico.nome_completo}" criada com sucesso! ID: {disp_medico2.id}')
        )

    def criar_agendamentos(self):
        clinica_teste = Clinica.objects.get(nome='Clinica Teste')

        medicos_pacientes = [
            {
                'medico': Medicos.objects.get(nome_completo='Dr Alfredo'),
                'paciente': Paciente.objects.get(nome_completo='João Roberto da Silva')
            },
            {
                'medico': Medicos.objects.get(nome_completo='Dr Bernardo'),
                'paciente': Paciente.objects.get(nome_completo='Ana Cristina Soares')
            },
        ]

        for m_p in medicos_pacientes:
            disponibilidade = Disponibilidade.objects.get(medico=m_p['medico'], disponivel=False)

            agendamento = Agendamento(
                status='Agendado',
                agendado_para=disponibilidade,
                medico=m_p['medico'],
                paciente=m_p['paciente'],
                clinica=clinica_teste,
            )

            agendamento.save()

            self.stdout.write(
                self.style.SUCCESS(f'Agendamento: "{agendamento.agendado_para} - {agendamento.medico.nome_completo} - {agendamento.paciente.nome_completo}" criado com sucesso! ID: {agendamento.id}')
            )

    def handle(self, *args, **options):
        self.criar_admin()
        self.criar_especialidades()
        self.criar_clinica()
        self.criar_medicos()
        self.criar_pacientes()
        self.criar_disponibilidades()
        self.criar_agendamentos()
