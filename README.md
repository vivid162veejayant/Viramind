# ☕ Viramind

### 💀 A developer-hostile programming language.

Viramind is an experimental programming language built in Python. It combines custom phrase-based syntax, variable storage, arithmetic evaluation, and a personality system designed to make programming feel like negotiating with a compiler that has questionable priorities.

**The goal:** Build a functional programming language with its own syntax, behavior, and a distinctly developer-hostile personality.

---

## 🚦 Project Status

- **Stage:** Early-stage prototype
- **Implementation language:** Python 🐍
- **Type:** Experimental programming language
- **AI dependency:** None
- **Development:** Active

Viramind started as a basic input loop that recognized the `exit` command. It has since evolved into a prototype with custom syntax, variables, and arithmetic expression evaluation.

## ⚙️ Current Features

### 📝 1. Custom Syntax

Viramind uses phrase-based instructions instead of relying entirely on conventional programming keywords.

| Purpose      | Syntax phrase                                 |
| ------------ | --------------------------------------------- |
| Declaration  | `apparently due to unfortunate circumstances` |
| Reassignment | `after reconsidering every terrible decision` |
| Output       | `has unfortunately become relevant`           |
| Input        | `against all better judgment,`                |

These phrases are part of Viramind's identity. Even a simple instruction has to sound like it regrets being written.

### 📦 2. Variables

Viramind maintains variable storage so values can be assigned and reused in expressions.

For example, a variable containing `10` can be referenced in a later calculation.

### 🧮 3. Arithmetic Evaluation

The current expression evaluator supports:

- Addition: `+`
- Subtraction: `-`
- Multiplication: `*`
- Division: `/`
- Exponentiation: `**`
- Parentheses for grouping
- Unary positive and negative operators

**Example:**

```text
x = 10
x ** 2
```

Expected result:

```text
100
```

### ⌨️ 4. Input and Output

Viramind has custom syntax for receiving input and displaying output, allowing users to interact with the language through its own instructions.

### 🎭 5. Personality System

Viramind includes a startup sequence, mood selection, and personality-dependent messages.

The long-term goal is to make its personality part of the language's behavior rather than merely a collection of messages printed by the main program.

## 🛠️ How Viramind Was Built

Viramind's development has progressed through several stages:

1. Created a basic program with input handling and exit recognition.
2. Organized the project into separate Python modules.
3. Added custom syntax phrases for declarations, reassignment, input, and output.
4. Implemented variable storage and value conversion.
5. Added arithmetic expression parsing and evaluation.
6. Integrated the language logic with the startup sequence and personality system.

Each stage moves Viramind closer to becoming a usable programming language rather than a simple command loop.

## 🗺️ Planned Development

These are future goals, not completed features.

- [ ] Improve syntax validation and error messages.
- [ ] Expand the language's syntax and supported operations.
- [ ] Develop more robust execution and runtime behavior.
- [ ] Add the planned randomized compilation behavior and ridiculous compiler excuses.
- [ ] Improve testing and documentation.
- [ ] Explore a future implementation in C.

The intended compiler personality may sometimes cooperate and sometimes refuse for reasons that are technically irrelevant and emotionally important to the compiler.

## 🧠 Design Philosophy

> Programming should work. The language just doesn't have to be pleasant about it.

Viramind is a learning project exploring language design, expression parsing, variable handling, modular Python development, and the gradual evolution of a small prototype into a more complete language.

## ⚠️ Current Limitations

Viramind is an early-stage prototype, not a production-ready programming language.

Its feature set, error handling, and runtime behavior are still evolving. Planned features should not be considered implemented until they are built and tested.

## 📜 License

**License:** To be decided.

See the repository's `LICENSE` file once a license has been selected.

## 👨‍💻 Development

Viramind is being developed incrementally. Features are added, tested, and refined as the project evolves.

Contributions, suggestions, and constructive feedback are welcome, subject to the project's eventual license terms.

---

**Viramind:** Your code may be correct. The compiler's willingness to acknowledge that is another matter. ☕💀

