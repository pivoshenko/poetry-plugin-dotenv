Output ../assets/demo.gif

Set FontSize 26
Set Width 1920
Set Height 1080
Set BorderRadius 10
Set TypingSpeed 0.5
Set Theme "Catppuccin Mocha"
Set WindowBar Colorful
Set Shell "zsh"

# ================================================================
# Intro
# ================================================================

Type "echo 'Welcome to poetry-plugin-dotenv!'"
Enter
Sleep 5s
Ctrl+L

Type "ls -a"
Enter
Sleep 5s
Ctrl+L

Type "bat -p main.py"
Enter
Sleep 5s
Ctrl+L

# ================================================================
# TOML Configuration - default
# ================================================================

Hide
Type "cp configs/pyproject.toml pyproject.toml"
Enter
Ctrl+L
Show

Type "bat -p -r 0:10 pyproject.toml"
Enter
Sleep 5s

Type "bat -p .env"
Enter
Sleep 5s

Type "poetry run -vvv python main.py"
Enter
Sleep 7s
Ctrl+L

# ================================================================
# TOML Configuration - custom location
# ================================================================

Hide
Type "cp configs/pyproject_location.toml pyproject.toml"
Enter
Ctrl+L
Show

Type "bat -p -r 0:10 pyproject.toml"
Enter
Sleep 5s

Type "bat -p .env.dev"
Enter
Sleep 5s

Type "poetry run -vvv python main.py"
Enter
Sleep 7s
Ctrl+L

# ================================================================
# TOML Configuration - ignore
# ================================================================

Hide
Type "cp configs/pyproject_ignore.toml pyproject.toml"
Enter
Ctrl+L
Show

Type "bat -p -r 0:10 pyproject.toml"
Enter
Sleep 5s

Type "poetry run -vvv python main.py"
Enter
Sleep 7s
Ctrl+L

# ================================================================
# OS Configuration - custom location
# ================================================================

Hide
Type "cp configs/pyproject.toml pyproject.toml"
Enter
Ctrl+L
Show

Type "bat -p .env.prod"
Enter
Sleep 5s

Type "export POETRY_PLUGIN_DOTENV_LOCATION=.env.prod && poetry run -vvv python main.py"
Enter
Sleep 7s
Ctrl+L

# ================================================================
# OS Configuration - ignore
# ================================================================

Type "export POETRY_PLUGIN_DOTENV_IGNORE=true && poetry run -vvv python main.py"
Enter
Sleep 7s
Ctrl+L

Ctrl+D
