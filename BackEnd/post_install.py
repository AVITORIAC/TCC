import os

def replace_force_str():
    """
        Esta função percorre todos os arquivos com extensão .py e em seguida, lê o conteúdo de cada arquivo, 
        substitui todas as ocorrências da string 'force_text' por 'force_str' e escreve o novo conteúdo de volta no arquivo.
        É muito importante pois assim atualiza a venv e evita erros na hora de rodar o servidor da API
    """
    for dirpath, dirnames, filenames in os.walk('.'):
        for filename in [f for f in filenames if f.endswith(".py")]:
            filepath = os.path.join(dirpath, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            new_content = content.replace('force_str', 'force_str')
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Updated {filepath}")

if __name__ == "__main__":
    replace_force_str()
