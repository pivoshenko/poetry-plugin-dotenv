Output demo.gif

Set FontSize 24
Set Width 1920
Set Height 1080
Set BorderRadius 10
Set TypingSpeed 0.5
Set Theme "OneDark"
Set Shell "zsh"

Type "echo 'Welcome to poetry-plugin-dotenv!'"
Enter
Sleep 10s
Ctrl+L

Type "ls -a"
Enter
Sleep 10s
Ctrl+L

Type "bat -p --paging=never main.py"
Enter
Sleep 10s
Ctrl+L

Type "bat -p --paging=never .env"
Enter
Sleep 10s

Type "poetry run -vvv python main.py"
Enter
Sleep 10s
Ctrl+L

Type "bat -p --paging=never .env.dev"
Enter
Sleep 10s

Type "export POETRY_DOTENV_LOCATION=.env.dev && poetry run -vvv python main.py"
Enter
Sleep 10s
Ctrl+L

Type "export POETRY_DONT_LOAD_DOTENV=1 && poetry run -vvv python main.py"
Enter
Sleep 10s
Ctrl+L

Ctrl+D
