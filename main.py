from lexer import Lexer, TokenType


def print_tokens(tokens):
    """Выводит токены в читаемом формате"""
    print("\n" + "=" * 50)
    print("ТОКЕНЫ:")
    print("=" * 50)

    for token in tokens:
        print(f"{token}")

    print("=" * 50)
    print(f"Всего токенов: {len(tokens)}")
    print("=" * 50)


def analyze_expression(expression):
    """Анализирует выражение и выводит результат"""
    print(f"\nАнализ выражения: '{expression}'")
    print("-" * 50)

    lexer = Lexer(expression)
    tokens = lexer.tokenize()

    # Группируем по типам для статистики
    types_count = {}
    for token in tokens:
        if token.type in types_count:
            types_count[token.type] += 1
        else:
            types_count[token.type] = 1

    print("Статистика по типам токенов:")
    for token_type, count in types_count.items():
        print(f"  {token_type.value}: {count}")

    print_tokens(tokens)
    return tokens


def main():
    print("ЛАБОРАТОРНАЯ РАБОТА: ЛЕКСЕР (LEXER/SCANNER)")
    print("Курс: Формальные языки и конечные автоматы")
    print("=" * 70)

    # Тест 1: Простое арифметическое выражение
    expr1 = "3 + 4 * 2"
    analyze_expression(expr1)

    # Тест 2: Выражение с тригонометрическими функциями
    expr2 = "sin(pi/2) + cos(0)"
    analyze_expression(expr2)

    # Тест 3: Выражение с числами с плавающей точкой
    expr3 = "3.14 * 2.5 ^ 2"
    analyze_expression(expr3)

    # Тест 4: Сложное выражение
    expr4 = "sin(pi * 0.5) + cos(pi) - 3.14"
    analyze_expression(expr4)

    # Тест 5: Выражение с константами
    expr5 = "2 * pi * e"
    analyze_expression(expr5)

    # Интерактивный режим
    print("\n" + "=" * 70)
    print("ИНТЕРАКТИВНЫЙ РЕЖИМ (введите 'exit' для выхода)")
    print("=" * 70)

    while True:
        try:
            expr = input("\nВведите выражение > ")
            if expr.lower() == 'exit':
                break

            if expr.strip():
                analyze_expression(expr)
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Ошибка: {e}")

    print("\nРабота завершена.")


if __name__ == "__main__":
    main()