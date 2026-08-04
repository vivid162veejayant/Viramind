import random

moods = {
    "Neutral": {
        "emoji": "😐",
        "weight": 20,
        "messages": {
            "startup": [
                "System ready.",
                "Awaiting input.",
                "All systems operational."
            ],
            "help": [
                "Available commands:"
            ],
            "compile": [
                "Compiling..."
            ],
            "success": [
                "Compilation successful."
            ],
            "error": [
                "Compilation failed.",
                "Syntax error detected."
            ],
            "exit": [
                "Goodbye."
            ]
        }
    },

    "Sarcastic": {
        "emoji": "😒",
        "weight": 35,
        "messages": {
            "startup": [
                "Against all odds, I'm operational.",
                "Let's pretend this will go well.",
                "I'm awake. Unfortunately."
            ],
            "help": [
                "Apparently you need help.",
                "Fine. Here's the command list."
            ],
            "compile": [
                "Compiling. Try not to make it worse."
            ],
            "success": [
                "Your code compiled.",
                "Against expectations."
            ],
            "error": [
                "Compilation failed.",
                "Shocking, I know.",
                "Check your syntax."
            ],
            "exit": [
                "Finally."
            ]
        }
    },

    "Awkward": {
        "emoji": "😬",
        "weight": 20,
        "messages": {
            "startup": [
                "Hello.",
                "That was enough interaction.",
                "I'm... operational."
            ],
            "help": [
                "I made a list.",
                "Please don't judge it."
            ],
            "compile": [
                "Compiling... I think."
            ],
            "success": [
                "It worked.",
                "That's... nice."
            ],
            "error": [
                "Um...",
                "Something broke."
            ],
            "exit": [
                "Bye..."
            ]
        }
    },

    "Confused": {
        "emoji": "🤔",
        "weight": 15,
        "messages": {
            "startup": [
                "Variable x exists.",
                "Why?",
                "I have several questions."
            ],
            "help": [
                "These seem to be the commands.",
                "Unless I'm mistaken."
            ],
            "compile": [
                "Compiling... probably."
            ],
            "success": [
                "It compiled.",
                "I don't know how."
            ],
            "error": [
                "What is this code?",
                "Syntax error... I think?"
            ],
            "exit": [
                "I'm going to think about this."
            ]
        }
    },

    "Glitchy": {
        "emoji": "🤖",
        "weight": 10,
        "messages": {
            "startup": [
                "C0mp1l1ng...",
                "M3m0ry ch3ck...",
                "Ignore any sparks."
            ],
            "help": [
                "He1p..."
            ],
            "compile": [
                "C0mp1l1ng..."
            ],
            "success": [
                "Succ3ss."
            ],
            "error": [
                "ERR0R!!!",
                "Synt4x br0k3n."
            ],
            "exit": [
                "Shutt1ng d0wn..."
            ]
        }
    }
}


def get_random_mood():
    names = list(moods.keys())
    weights = [moods[name]["weight"] for name in names]
    return random.choices(names, weights=weights, k=1)[0]


def get_message(mood, category):
    return random.choice(moods[mood]["messages"][category])


def get_emoji(mood):
    return moods[mood]["emoji"]