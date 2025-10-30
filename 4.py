def dfa_transition(current_state, symbol):
    # Таблица переходов: state -> {symbol: next_state}
    transitions = {
        0: {'A': 1, 'B': 1, 'C': 1},
        1: {'A': 1, 'B': 0, 'C': 2},
        2: {'A': 1, 'B': 3, 'C': 3},
        3: {'A': 2, 'B': 2, 'C': 3}
    }
    
    if current_state not in transitions:
        raise ValueError(f"Неизвестное состояние: {current_state}")
    if symbol not in transitions[current_state]:
        raise ValueError(f"Неизвестный символ: {symbol}")
    
    return transitions[current_state][symbol]

def dfa_accepts(string):
    current_state = 0  # начальное состояние
    path = [0]  # сохраняем путь состояний
    
    for char in string:
        current_state = dfa_transition(current_state, char)
        path.append(current_state)
    
    # Конечное состояние — 2
    accepted = (current_state == 2)
    return accepted, path

# Тестируем строки
test_strings = ["ABABA", "CBABB", "BBAABA", "BCABCA"]

for s in test_strings:
    accepted, path = dfa_accepts(s)
    print(f"Строка '{s}':")
    print(f"  Цепочка состояний: {' → '.join(map(str, path))}")
    print(f"  Статус: {'Есть в языке' if accepted else 'Нет в языке'}\n")
