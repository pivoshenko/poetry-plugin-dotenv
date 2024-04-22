Output ../assets/demo.gif

Set FontSize 26
Set Width 1920
Set Height 1080
Set Margin 20
Set BorderRadius 10
Set TypingSpeed 0.5
Set Theme "Catppuccin Mocha"
Set WindowBar Colorful
Set Shell "zsh"

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

Type "bat -p pyproject.toml"
Enter
Sleep 5s
Ctrl+L

Type "bat -p .env.dev"
Enter
Sleep 5s

Type "poetry run -vvv python main.py"
Enter
Sleep 5s
Ctrl+L

Ctrl+D
