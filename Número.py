def numero_por_extenso(valor):
    # Dicionários para mapear números em extenso
    unidades = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
    especiais = {
        10: "dez",
        11: "onze",
        12: "doze",
        13: "treze",
        14: "quatorze",
        15: "quinze",
        16: "dezesseis",
        17: "dezessete",
        18: "dezoito",
        19: "dezenove"
    }
    
    # Função auxiliar para converter números até 999
    def converte_grupo(num):
        if num == 0:
            return ""
        elif num < 10:
            return unidades[num]
        elif num < 20:
            return especiais[num]
        elif num < 100:
            return dezenas[num // 10] + (" e " + converte_grupo(num % 10) if num % 10 != 0 else "")
        else:
            return unidades[num // 100] + " cento" + (" e " + converte_grupo(num % 100) if num % 100 != 0 else "")
    
    # Função principal para converter números até bilhões
    def converte_numero(num):
        if num == 0:
            return "zero"
        
        grupos = []
        milhares = ["", " mil", " milhão", " bilhão"]
        for i in range(4):
            grupo = num % 1000
            if grupo != 0:
                extenso = converte_grupo(grupo)
                if i == 1 and extenso == "um":
                    extenso = "mil"
                else:
                    extenso += milhares[i]
                grupos.append(extenso)
            num //= 1000
        
        return " ".join(reversed(grupos))
    
    return converte_numero(valor)


# Função principal para tratar o valor monetário
def valor_monetario_extenso():
    # Entrada do usuário
    entrada = input("Digite o valor em dinheiro (exemplo: R$ 1.003,95): ").strip()
    
    # Remover o símbolo 'R$' e separar reais e centavos
    valor = entrada.replace("R$", "").replace(".", "").replace(",", ".")
    reais, centavos = map(int, valor.split("."))
    
    # Converter reais e centavos para extenso
    extenso_reais = numero_por_extenso(reais)
    extenso_centavos = numero_por_extenso(centavos)
    
    # Montar a frase final
    resultado = ""
    if reais > 0:
        resultado += extenso_reais + " real" + ("s" if reais > 1 else "")
    if centavos > 0:
        resultado += " e " if reais > 0 else ""
        resultado += extenso_centavos + " centavo" + ("s" if centavos > 1 else "")
    
    return resultado


# Execução do programa
if __name__ == "__main__":
    print(valor_monetario_extenso())