from utils import input_number

BYTE_SIZE = 8


def download_time(file_size, internet_speed):
    """
    Estima em minutos o tempo que levará para baixar determinado arquivo
    """
    megabytes = to_megabytes(internet_speed)
    seconds = file_size / megabytes
    return to_minutes(seconds)


def to_megabytes(megabits):
    """Converte megabits em megabytes"""
    return megabits / BYTE_SIZE


def to_minutes(seconds):
    """Converte segundos em minutos"""
    return seconds / 60


def main():
    """
    18. Faça um programa que peça o tamanho de um arquivo para download
    (em MB) e a velocidade de um link de Internet (em Mbps), calcule e
    informe o tempo aproximado de download do arquivo usando este link
    (em minutos).
    """
    file_size = input_number('Informe o tamanho do arquivo (MB): ')
    link_speed = input_number('Informe a velocidade do link (Mbps): ')
    minutes = download_time(file_size, link_speed)
    print(f'O tempo estimado para download é de {minutes:.1f} minutos.')



if __name__ == '__main__':
    main()
