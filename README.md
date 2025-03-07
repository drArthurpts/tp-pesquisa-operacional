
# Trabalho Prático da Disciplina de Pesquisa Operacional 
Neste trabalho iremos usar um problema do mundo real como exemplo e aplicar a
modelagem matemática, a fim de chegar em uma solução mais adequada dentre as diversas
alternativas, ou seja, obter a solução mais otimizada.

O objetivo principal deste projeto de pesquisa operacional é desenvolver
um modelo de otimização que maximize a alocação de desabrigados em abrigos disponíveis em
toda a cidade de Porto Alegre. Queremos garantir que o maior número possível de desabrigados
seja acomodado de maneira eficiente e eficaz, levando em consideração as capacidades dos
abrigos e a localização dos desabrigados.

## Como executar o projeto Django

Para executar o projeto Django, siga as etapas abaixo:

1. Certifique-se de ter o Python instalado em sua máquina. Você pode baixar a versão mais recente do Python em [python.org](https://www.python.org/downloads/).

2. Clone o repositório do projeto para o seu ambiente local:

    ```bash
    git clone https://github.com/seu-usuario/tp-pesquisa-operacional.git
    ```

3. Acesse o diretório do projeto:

    ```bash
    cd tp-pesquisa-operacional
    ```

4. Crie um ambiente virtual para isolar as dependências do projeto:

    ```bash
    python -m venv env
    ```

5. Ative o ambiente virtual:

    - No Windows:

      ```bash
      env\Scripts\activate
      ```

    - No macOS e Linux:

      ```bash
      source env/bin/activate
      ```

6. Instale as dependências do projeto:

    ```bash
    pip install -r requirements.txt
    ```

7. Execute as migrações do banco de dados:

    ```bash
    python manage.py migrate
    ```

8. Inicie o servidor de desenvolvimento:

    ```bash
    python manage.py runserver
    ```

9. Agora você pode acessar o projeto Django em seu navegador através do endereço `http://localhost:8000/`.

Lembre-se de substituir `seu-usuario` pelo seu nome de usuário do GitHub no comando de clone do passo 2.

