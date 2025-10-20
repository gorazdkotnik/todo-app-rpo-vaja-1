from todo_app import TodoApp

if __name__ == "__main__":
    print(greet_user("User"))
    app = TodoApp()
    app.menu()


def greet_user(name):
    return f"Hello, {name}! Welcome to the Todo Application!"
