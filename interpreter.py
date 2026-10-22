
import re

# ===============================
#        SYNTAX PHRASES
# ===============================

DECLARATION_PHRASE = "apparently due to unfortunate circumstances"
REASSIGNMENT_PHRASE = "after reconsidering every terrible decision"
OUTPUT_PHRASE = "has unfortunately become relevant"
INPUT_PHRASE = "against all better judgment, "

# ==============================
#        VARIABLE STORAGE
# ==============================

VARIABLES = {}


# ==============================
#        VALUE CONVERSION
# ==============================

def parse_value(value):
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value


# ===============================
#      ADVANCED ARITHMETIC
# ===============================

def parse_expression(expression):
    expression = expression.strip()

    tokens = re.findall(
        r'\d+(?:\.\d+)?|[A-Za-z_]\w*|\*\*|[()+\-*/]',
        expression
    )

    compact = re.sub(r'\s+', '', expression)

    if not tokens or "".join(tokens) != compact:
        raise ValueError("INVALID EXPRESSION. CHECK YOUR SYMBOLS.")

    # Preserve plain values and ordinary text.
    if not any(op in expression for op in ("+", "-", "*", "/", "(", ")")):
        return parse_value(expression)

    index = 0

    def peek():
        return tokens[index] if index < len(tokens) else None

    def consume():
        nonlocal index

        token = peek()

        if token is None:
            raise ValueError("EXPRESSION ENDED PREMATURELY.")

        index += 1
        return token

    def primary():
        token = consume()

        if token == "(":
            value = expression_parser()

            if peek() != ")":
                raise ValueError("MISSING CLOSING PARENTHESIS.")

            consume()
            return value

        if token.replace(".", "", 1).isdigit():
            return float(token) if "." in token else int(token)

        if re.fullmatch(r'[A-Za-z_]\w*', token):
            if token not in VARIABLES:
                raise ValueError(f"VARIABLE '{token}' DOES NOT EXIST.")

            value = VARIABLES[token]

            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise ValueError(f"'{token}' IS NOT A NUMBER.")

            return value

        raise ValueError(f"INVALID OPERAND: {token}")

    def power():
        value = primary()

        if peek() == "**":
            consume()
            value = value ** unary()

        return value

    def unary():
        if peek() == "+":
            consume()
            return unary()

        if peek() == "-":
            consume()
            return -unary()

        return power()

    def term():
        value = unary()

        while peek() in ("*", "/"):
            operator = consume()
            right = unary()

            if operator == "*":
                value *= right
            else:
                if right == 0:
                    raise ValueError(
                        "DIVISION BY ZERO. ABSOLUTELY NOT."
                    )

                value /= right

        return value

    def expression_parser():
        value = term()

        while peek() in ("+", "-"):
            operator = consume()
            right = term()

            if operator == "+":
                value += right
            else:
                value -= right

        return value

    result = expression_parser()

    if index != len(tokens):
        raise ValueError(f"UNEXPECTED TOKEN: {tokens[index]}")

    if isinstance(result, float) and result.is_integer():
        result = int(result)

    return result


# ===============================
#          SYNTAX INDEX
# ===============================

def syntax_index(user_input):
    if user_input.strip().lower() not in ("help", "help()"):
        return None

    print()
    print("=" * 52)
    print("       VIRAMIND : SYNTAX GRAVEYARD")
    print("=" * 52)

    print("""
[ 01 ] VARIABLE DECLARATION
      apparently due to unfortunate circumstances

      Example:
      apparently due to unfortunate circumstances age is 13

[ 02 ] VARIABLE REASSIGNMENT
      after reconsidering every terrible decision

      Example:
      after reconsidering every terrible decision age is now 14

[ 03 ] VARIABLE OUTPUT
      has unfortunately become relevant

      Example:
      age has unfortunately become relevant

[ 04 ] USER INPUT
      against all better judgment,

      Example:
      against all better judgment, name is requested with "Your name?"

[ 05 ] HELP
      help

      Displays this syntax index.
""")

    print("=" * 52)
    print("STATUS: THE LANGUAGE IS STILL UNDER CONSTRUCTION.")
    print("FEATURES: FEWER THAN THE ERRORS YOU WILL DISCOVER.")
    print("=" * 52)
    print()

    return "."


# ===============================
#        VALUE DECLARATION
# ===============================

def parse_declaration(user_input):
    if not user_input.startswith(DECLARATION_PHRASE):
        return None

    user_input = user_input[len(DECLARATION_PHRASE):].strip()

    if " is " not in user_input:
        return "COMMON_SENSE_ERROR: USER HAS NO COMMON SENSE LEFT ABOUT DECLARATION."

    variable_name, expression = user_input.split(" is ", 1)
    variable_name = variable_name.strip()

    if not re.fullmatch(r'[A-Za-z_]\w*', variable_name):
        return "DECLARATION ERROR: THAT IS NOT A VALID VARIABLE NAME."

    try:
        value = parse_expression(expression)
    except (ValueError, OverflowError, ZeroDivisionError) as error:
        return f"ARITHMETIC_ERROR: {error}"

    VARIABLES[variable_name] = value

    return f"Cute, you declared {variable_name} as {value}."


# ================================
#        VALUE REASSIGNMENT
# ================================

def parse_reassignment(user_input):
    if not user_input.startswith(REASSIGNMENT_PHRASE):
        return None

    user_input = user_input[len(REASSIGNMENT_PHRASE):].strip()

    if " is now " not in user_input:
        return "REASSIGNMENT HAS FAILED. EVEN THE VARIABLE IS CONFUSED."

    variable_name, expression = user_input.split(" is now ", 1)
    variable_name = variable_name.strip()

    if variable_name not in VARIABLES:
        return "VARIABLE HASN'T BEEN MADE AND NOW YOU EXPECT ME TO MAKE ONE?"

    try:
        value = parse_expression(expression)
    except (ValueError, OverflowError, ZeroDivisionError) as error:
        return f"ARITHMETIC_ERROR: {error}"

    VARIABLES[variable_name] = value

    return f"Fine. {variable_name} is now {value}."


# ==========================
#        VALUE OUTPUT
# ==========================

def parse_output(user_input):
    if not user_input.endswith(OUTPUT_PHRASE):
        return None

    variable_name = user_input[:-len(OUTPUT_PHRASE)].strip()

    if variable_name in VARIABLES:
        return VARIABLES[variable_name]

    return "ERROR: VARIABLE DOES NOT EXIST."


# =========================
#        VALUE INPUT
# =========================

def parse_input(user_input):
    if not user_input.startswith(INPUT_PHRASE):
        return None

    user_input = user_input[len(INPUT_PHRASE):].strip()

    if " is requested with " not in user_input:
        return "ERROR: INPUT SYNTAX IS INCOMPLETE."

    variable_name, question = user_input.split(" is requested with ", 1)
    variable_name = variable_name.strip()
    question = question.strip()

    if not re.fullmatch(r'[A-Za-z_]\w*', variable_name):
        return "ERROR: YOU FORGOT TO NAME YOUR VARIABLE PROPERLY."

    if len(question) < 2 or question[0] != '"' or question[-1] != '"':
        return 'ERROR: PUT YOUR QUESTION INSIDE DOUBLE QUOTES.'

    question = question[1:-1]

    if not question:
        return "ERROR: YOUR QUESTION IS EMPTY. IMPRESSIVE."

    value = input(question + " ")

    try:
        VARIABLES[variable_name] = parse_expression(value)
    except (ValueError, OverflowError, ZeroDivisionError) as error:
        return f"INPUT_ARITHMETIC_ERROR: {error}"

    return "."


# =========================
#        MAIN PARSER
# =========================

def parse(user_input):
    result = parse_declaration(user_input)
    if result is not None:
        return result

    result = parse_reassignment(user_input)
    if result is not None:
        return result

    result = parse_output(user_input)
    if result is not None:
        return result

    result = parse_input(user_input)
    if result is not None:
        return result

    result = syntax_index(user_input)
    if result is not None:
        return result

    try:
        return parse_expression(user_input)
    except (ValueError, OverflowError, ZeroDivisionError) as error:
        return f"VIRAMIND ERROR: {error}"
