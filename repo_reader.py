# - This file only works if you have the pydriller library installed.
# - File has to be in pl7/DEV/<folder_name>/repo_reader.py
from pydriller import Repository
from collections import defaultdict
import os

def repo_reader_commit():
    
    current_directory = os.getcwd()
    repo_path = '/Users/alvaroterroso/Desktop/test_repo'

    file_metrics = defaultdict(lambda: {
        'lines_of_code': 0,
        'complexity': 0,
        'authors': set(),
        'number_of_changes': 0,
        'file_type': '',
        'lines_added_by_author': defaultdict(int)
    })
    
    # Percorre todos os commits no repositório
    for commit in Repository(repo_path).traverse_commits():
        for mod in commit.modified_files:
            # Nome do arquivo
            filename = mod.filename

            # Atualiza o número de autores
            author_name = commit.author.name
            file_metrics[filename]['authors'].add(author_name)
            
            # Incrementa o número de mudanças
            file_metrics[filename]['number_of_changes'] += 1
            
            # Atualiza o número de linhas de código e complexidade
            if mod.nloc is not None:
                file_metrics[filename]['lines_of_code'] = mod.nloc
            if mod.complexity is not None:
                file_metrics[filename]['complexity'] = mod.complexity

            # Define o tipo de arquivo (extensão)
            file_metrics[filename]['file_type'] = filename.split('.')[-1]

            # Incrementa o total de linhas adicionadas pelo autor atual
            if mod.added is not None:
                file_metrics[filename]['lines_added_by_author'][author_name] += mod.added

    # Exibe as métricas de cada arquivo
    for filename, metrics in file_metrics.items():
        print(f"Arquivo: {filename}")
        print(f"Tipo de Arquivo: {metrics['file_type']}")
        print(f"Linhas de Código (LOC): {metrics['lines_of_code']}")
        print(f"Complexidade: {metrics['complexity']}")
        print(f"Número de Autores: {len(metrics['authors'])}")
        print(f"Número de Mudanças: {metrics['number_of_changes']}")
        print("Linhas de Código Adicionadas por Autor:")
        for author, lines_added in metrics['lines_added_by_author'].items():
            print(f"  {author}: {lines_added} linhas")
        print('-' * 40)
    
    return file_metrics

#repo_reader_commit()

def repo_reader_file():
    
    current_directory = os.getcwd()
    repo_path = '/Users/alvaroterroso/Desktop/test_repo'

    # Lista que armazenará as métricas de cada arquivo como dicionários
    file_metrics_dict = defaultdict(lambda: {
        'filename': '',
        'file_type': '',
        'lines_of_code': 0,
        'complexity': 0,
        'authors': set(),
        'number_of_changes': 0,
        'lines_added_by_author': defaultdict(int)
    })
    
    # Percorre todos os commits no repositório
    for commit in Repository(repo_path).traverse_commits():
        for mod in commit.modified_files:
            filename = mod.filename
            author_name = commit.author.name

            # Atualiza as informações do arquivo
            file_metrics_dict[filename]['filename'] = filename
            file_metrics_dict[filename]['file_type'] = filename.split('.')[-1]
            file_metrics_dict[filename]['authors'].add(author_name)
            file_metrics_dict[filename]['number_of_changes'] += 1
            if mod.nloc is not None:
                file_metrics_dict[filename]['lines_of_code'] = mod.nloc
            if mod.complexity is not None:
                file_metrics_dict[filename]['complexity'] = mod.complexity

            # Incrementa o total de linhas adicionadas pelo autor atual
            if mod.added_lines is not None:
                file_metrics_dict[filename]['lines_added_by_author'][author_name] += mod.added_lines

    # Converte o dicionário para uma lista de dicionários, formatando o conjunto de autores como uma lista
    file_metrics_list = []
    for filename, metrics in file_metrics_dict.items():
        metrics['authors'] = list(metrics['authors'])  # Converte o conjunto de autores para uma lista
        file_metrics_list.append(metrics)
        
    # Exibe as métricas de cada arquivo
    for metrics in file_metrics_list:
        print(f"Arquivo: {metrics['filename']}")
        print(f"Tipo de Arquivo: {metrics['file_type']}")
        print(f"Linhas de Código (LOC): {metrics['lines_of_code']}")
        print(f"Complexidade: {metrics['complexity']}")
        print(f"Número de Autores: {len(metrics['authors'])}")
        print(f"Número de Mudanças: {metrics['number_of_changes']}")
        print("Linhas de Código Adicionadas por Autor:")
        for author, lines_added in metrics['lines_added_by_author'].items():
            print(f"  {author}: {lines_added} linhas")
        print('-' * 40)
    
    return file_metrics_list

repo_reader_file()