import sys
from pathlib import Path

# Adiciona o diretório raiz ao sys.path para permitir a importação de repo_reader
sys.path.append(str(Path(__file__).resolve().parent.parent))

from repo_reader import repo_reader_file  # Agora importe a função normalmente

def test_repo_reader_file():
    # Executa a função e obtém o resultado
    metrics_list = repo_reader_file()

    # Dados esperados com base no novo output fornecido
    expected_output = [
        {
            'filename': 'test.txt',
            'file_type': 'txt',
            'lines_of_code': 0,
            'complexity': 0,
            'authors': ['Álvaro', 'Mariana Sousa'],
            'number_of_changes': 2,
            'lines_added_by_author': {'Álvaro': 1, 'Mariana Sousa': 2}
        },
        {
            'filename': 'file1.md',
            'file_type': 'md',
            'lines_of_code': 0,
            'complexity': 0,
            'authors': ['Álvaro', 'Mariana Sousa'],
            'number_of_changes': 2,
            'lines_added_by_author': {'Álvaro': 29, 'Mariana Sousa': 0}
        },
        {
            'filename': 'file2.txt',
            'file_type': 'txt',
            'lines_of_code': 0,
            'complexity': 0,
            'authors': ['Álvaro'],
            'number_of_changes': 1,
            'lines_added_by_author': {'Álvaro': 12}
        },
        {
            'filename': 'file3.py',
            'file_type': 'py',
            'lines_of_code': 221,
            'complexity': 50,
            'authors': ['Álvaro'],
            'number_of_changes': 1,
            'lines_added_by_author': {'Álvaro': 310}
        },
        {
            'filename': 'file4.c',
            'file_type': 'c',
            'lines_of_code': 946,
            'complexity': 226,
            'authors': ['Álvaro'],
            'number_of_changes': 1,
            'lines_added_by_author': {'Álvaro': 1110}
        },
        {
            'filename': 'file.md',
            'file_type': 'md',
            'lines_of_code': 0,
            'complexity': 0,
            'authors': ['Álvaro', 'Mariana Sousa'],
            'number_of_changes': 2,
            'lines_added_by_author': {'Álvaro': 1, 'Mariana Sousa': 4}
        },
        {
            'filename': 'file5.txt',
            'file_type': 'txt',
            'lines_of_code': 0,
            'complexity': 0,
            'authors': ['Mariana Sousa'],
            'number_of_changes': 1,
            'lines_added_by_author': {'Mariana Sousa': 10}
        },
        {
            'filename': '.DS_Store',
            'file_type': 'DS_Store',
            'lines_of_code': 0,
            'complexity': 0,
            'authors': ['Álvaro'],
            'number_of_changes': 1,
            'lines_added_by_author': {'Álvaro': 0}
        },
        {
            'filename': 'repo_reader.py',
            'file_type': 'py',
            'lines_of_code': 82,
            'complexity': 17,
            'authors': ['Álvaro'],
            'number_of_changes': 1,
            'lines_added_by_author': {'Álvaro': 121}
        }
    ]
    
    # Verifica se o resultado tem o mesmo número de arquivos que o esperado
    assert len(metrics_list) == len(expected_output), "O número de arquivos processados não corresponde ao esperado."

    # Itera sobre cada arquivo esperado e compara com o resultado real
    for expected, actual in zip(expected_output, metrics_list):
        assert actual['filename'] == expected['filename']
        assert actual['file_type'] == expected['file_type']
        assert actual['lines_of_code'] == expected['lines_of_code']
        assert actual['complexity'] == expected['complexity']
        assert set(actual['authors']) == set(expected['authors'])
        assert actual['number_of_changes'] == expected['number_of_changes']
        assert actual['lines_added_by_author'] == expected['lines_added_by_author']
