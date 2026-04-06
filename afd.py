import json

def load_afd(filename):
    print(f"Carregando AFD a partir do arquivo '{filename}'...")
    with open(filename, "r") as f:
        data = json.load(f)

    states = data["states"]
    alphabet = data["alphabet"]
    start_state = data["start_state"]
    end_states = set(data["end_states"])
    transitions = {}

    for state, rules in data["transitions"].items():
        for symbol, next_state in rules.items():
            if state not in states:
                raise ValueError(f"Estado inválido no arquivo: '{state}'")
            if next_state not in states:
                raise ValueError(f"Próximo estado inválido no arquivo: '{next_state}'")
            if symbol not in alphabet:
                raise ValueError(f"Símbolo inválido no arquivo: '{symbol}'")
            transitions[(state, symbol)] = next_state

    print("[INFO] AFD carregado com sucesso!")
    return states, alphabet, start_state, end_states, transitions


def run_afd(transitions, start_state, end_states, alphabet, word):
    current_state = start_state

    for symbol in word:
        if symbol not in alphabet:
            print(f"[ERRO] Símbolo '{symbol}' não pertence ao alfabeto")
            return False

        next_state = transitions.get((current_state, symbol))
        if not next_state:
            print(f"[ERRO] Transição indefinida para ({current_state}, '{symbol}')")
            return False

        current_state = next_state

    return current_state in end_states


def main():
    try:
        states, alphabet, start_state, end_states, transitions = load_afd("afd.json")
    except FileNotFoundError:
        print("[FALHA] Arquivo 'afd.json' não encontrado")
        return
    except json.JSONDecodeError:
        print("[FALHA] Erro ao ler JSON. Verifique a formatação do arquivo")
        return
    except ValueError as ex:
        print(f"[FALHA] {ex}")
        return

    while True:
        word = input("\nInforme uma palavra para validação (ou 'sair'): ").strip()
        if word.lower() == "sair":
            print("Encerrando execução...")
            break
        if not word:
            print("[AVISO] Nenhuma palavra informada")
            continue

        is_accepted = run_afd(transitions, start_state, end_states, alphabet, word)
        print("[RESULTADO] Palavra aceita" if is_accepted else "[RESULTADO] Palavra rejeitada")


if __name__ == "__main__":
    main()