def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    return linhas

def formatar_conjunto(conjunto):
    #Formata o conjunto para exibição.
    return '{' + ', '.join(map(str, set(conjunto))) + '}'

def uniao(conjunto1, conjunto2):
    #Calcula a união dos dois conjuntos e retorna o resultado.
    resultado = set(conjunto1).union(set(conjunto2))
    return resultado

def interseccao(conjunto1, conjunto2):
    #Calcula a interseção dos dois conjuntos e retorna o resultado.
    resultado = set(conjunto1).intersection(set(conjunto2))
    return resultado

def diferenca(conjunto1, conjunto2):
    #Calcula a diferença dos dois conjuntos e retorna o resultado.
    resultado = set(conjunto1).difference(set(conjunto2))
    return resultado

def produto_cartesiano(conjunto1, conjunto2):
    #Calcula o produto cartesiano dos dois conjuntos e retorna o resultado.
    resultado = {(x, y) for x in conjunto1 for y in conjunto2}
    return resultado

def processar_arquivo(nome_arquivo):
    #Processa o arquivo de entrada e executa as operações definidas.
    linhas = ler_arquivo(nome_arquivo)
    num_operacoes = int(linhas[0].strip())
    index = 1
    resultados = []

    for _ in range(num_operacoes):
        operacao = linhas[index].strip()
        conjunto1 = linhas[index + 1].strip().split(', ')
        conjunto2 = linhas[index + 2].strip().split(', ')
        index += 3

        if operacao == 'U':
            resultado = uniao(conjunto1, conjunto2)
            operacao_str = 'União'
        elif operacao == 'I':
            resultado = interseccao(conjunto1, conjunto2)
            operacao_str = 'Interseção'
        elif operacao == 'D':
            resultado = diferenca(conjunto1, conjunto2)
            operacao_str = 'Diferença'
        elif operacao == 'C':
            resultado = produto_cartesiano(conjunto1, conjunto2)
            operacao_str = 'Produto Cartesiano'
        else:
            raise ValueError(f'Operação desconhecida: {operacao}')

        resultado_formatado = formatar_conjunto(resultado)
        conjunto1_formatado = formatar_conjunto(conjunto1)
        conjunto2_formatado = formatar_conjunto(conjunto2)

        if operacao == 'C':
            resultado_str = f'{operacao_str}: conjunto 1 {conjunto1_formatado}, conjunto 2 {conjunto2_formatado}. Resultado: {{{", ".join(f"({a}, {b})" for a, b in resultado)}}}'
        else:
            resultado_str = f'{operacao_str}: conjunto 1 {conjunto1_formatado}, conjunto 2 {conjunto2_formatado}. Resultado: {resultado_formatado}'
        
        resultados.append(resultado_str)

    return resultados

def main():
    nome_arquivo = 'teste3.txt'  # Substitue pelo nome do arquivo que vc deseja abrir, dentre os disponíveis na pasta
    resultados = processar_arquivo(nome_arquivo)

    for resultado in resultados:
        print(resultado)

if __name__ == '__main__':
    main()
