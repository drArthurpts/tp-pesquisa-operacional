from django.core.management.base import BaseCommand

from tpPesquisaOperacionalApp import Abrigo
import pandas as pd

class Command(BaseCommand):
    help = 'Importa abrigos de um arquivo CSV'

    def add_arguments(self, parser):
        parser.add_argument('arquivo_csv', type=str, help='O caminho do arquivo CSV')

    def handle(self, *args, **kwargs):
        arquivo_csv = kwargs['arquivo_csv']
        dados = pd.read_csv(arquivo_csv)
        for _, linha in dados.iterrows():
            Abrigo.objects.get_or_create(
                nome=linha['nome'],
                endereco=linha['endereco'],
                # Adicione mais campos conforme necessário
            )
        self.stdout.write(self.style.SUCCESS('Importação concluída com sucesso'))