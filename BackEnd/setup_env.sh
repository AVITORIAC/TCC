# passo a passo para rodar a api

# Criar a venv (pode ser tanto python como py)
python -m venv .venv

# Ativar a venv
.venv\Scripts\activate

# criar arquivo de configurações e adicionar as configurações necessárias nele
cd C:\caminho\para\seu\diretorio
type nul > .env

# Instalar os requisitos
pip install -r requirements.txt

# Executar o script de pós instalação (configuração do ambiente)
python post_install.py

# criar migrações
python manage.py makemigrations

# aplicar migrações
python manage.py migrate

# criar superusuário
python manage.py createsuperuser

# rodar servidor da API
python manage.py runserver
