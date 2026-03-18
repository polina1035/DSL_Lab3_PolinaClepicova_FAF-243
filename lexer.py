from enum import Enum


# Типы токенов
class TokenType(Enum):
    # Специальные
    EOF = 'EOF'
    ILLEGAL = 'ILLEGAL'

    # Числа
    INT = 'INT'
    FLOAT = 'FLOAT'

    # Операторы
    PLUS = 'PLUS'  # +
    MINUS = 'MINUS'  # -
    MULTIPLY = 'MULTIPLY'  # *
    DIVIDE = 'DIVIDE'  # /
    POWER = 'POWER'  # ^
    ASSIGN = 'ASSIGN'  # =

    # Разделители
    LPAREN = 'LPAREN'  # (
    RPAREN = 'RPAREN'  # )
    COMMA = 'COMMA'  # ,

    # Тригонометрические функции
    SIN = 'SIN'
    COS = 'COS'

    # Константы
    PI = 'PI'
    E = 'E'

    # Идентификаторы
    IDENT = 'IDENT'


# Класс токена
class Token:
    def __init__(self, type_, literal, line=1, column=0):
        self.type = type_
        self.literal = literal
        self.line = line
        self.column = column

    def __str__(self):
        return f"Token({self.type.value}, '{self.literal}', line={self.line}, col={self.column})"


# Основной класс лексера
class Lexer:
    def __init__(self, input_text):
        self.input = input_text
        self.position = 0  # текущая позиция
        self.next_position = 0  # следующая позиция
        self.ch = ''  # текущий символ
        self.line = 1
        self.column = 0

        # Ключевые слова
        self.keywords = {
            'sin': TokenType.SIN,
            'cos': TokenType.COS,
            'pi': TokenType.PI,
            'e': TokenType.E
        }

        self.read_char()

    def read_char(self):
        """Читает следующий символ"""
        if self.next_position >= len(self.input):
            self.ch = '\0'  # EOF
        else:
            self.ch = self.input[self.next_position]
            if self.ch == '\n':
                self.line += 1
                self.column = 0
            else:
                self.column += 1

        self.position = self.next_position
        self.next_position += 1

    def peek_char(self):
        """Смотрит следующий символ без перемещения"""
        if self.next_position >= len(self.input):
            return '\0'
        return self.input[self.next_position]

    def skip_whitespace(self):
        """Пропускает пробелы"""
        while self.ch in ' \t\n\r':
            self.read_char()

    def read_number(self):
        """Читает число (целое или с плавающей точкой)"""
        position = self.position
        is_float = False

        # Читаем целую часть
        while self.ch.isdigit():
            self.read_char()

        # Проверяем на десятичную точку
        if self.ch == '.' and self.peek_char().isdigit():
            is_float = True
            self.read_char()  # проглатываем точку

            # Читаем дробную часть
            while self.ch.isdigit():
                self.read_char()

        literal = self.input[position:self.position]

        if is_float:
            return Token(TokenType.FLOAT, literal, self.line, self.column - len(literal))
        else:
            return Token(TokenType.INT, literal, self.line, self.column - len(literal))

    def read_identifier(self):
        """Читает идентификатор или ключевое слово"""
        position = self.position

        while self.ch.isalpha() or self.ch == '_':
            self.read_char()

        literal = self.input[position:self.position]

        # Проверяем, является ли это ключевым словом
        token_type = self.keywords.get(literal, TokenType.IDENT)

        return Token(token_type, literal, self.line, self.column - len(literal))

    def next_token(self):
        """Возвращает следующий токен"""
        self.skip_whitespace()

        token = None
        column = self.column

        if self.ch == '\0':
            token = Token(TokenType.EOF, '', self.line, column)

        elif self.ch == '+':
            token = Token(TokenType.PLUS, '+', self.line, column)
            self.read_char()

        elif self.ch == '-':
            token = Token(TokenType.MINUS, '-', self.line, column)
            self.read_char()

        elif self.ch == '*':
            token = Token(TokenType.MULTIPLY, '*', self.line, column)
            self.read_char()

        elif self.ch == '/':
            token = Token(TokenType.DIVIDE, '/', self.line, column)
            self.read_char()

        elif self.ch == '^':
            token = Token(TokenType.POWER, '^', self.line, column)
            self.read_char()

        elif self.ch == '=':
            token = Token(TokenType.ASSIGN, '=', self.line, column)
            self.read_char()

        elif self.ch == '(':
            token = Token(TokenType.LPAREN, '(', self.line, column)
            self.read_char()

        elif self.ch == ')':
            token = Token(TokenType.RPAREN, ')', self.line, column)
            self.read_char()

        elif self.ch == ',':
            token = Token(TokenType.COMMA, ',', self.line, column)
            self.read_char()

        else:
            if self.ch.isdigit():
                token = self.read_number()
            elif self.ch.isalpha() or self.ch == '_':
                token = self.read_identifier()
            else:
                token = Token(TokenType.ILLEGAL, self.ch, self.line, column)
                self.read_char()

        return token

    def tokenize(self):
        """Токенизирует весь ввод"""
        tokens = []
        token = self.next_token()

        while token.type != TokenType.EOF:
            tokens.append(token)
            token = self.next_token()

        tokens.append(token)  # добавляем EOF
        return tokens