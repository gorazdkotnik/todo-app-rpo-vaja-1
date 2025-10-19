import os

TASKS_FILE = "tasks.txt"


class Task:
    """Predstavlja posamezno opravilo."""

    def __init__(self, description, done=False):
        self.description = description
        self.done = done

    def mark_done(self):
        self.done = True

    def __str__(self):
        status = "✅" if self.done else "❌"
        return f"{status} {self.description}"


class TodoList:
    """Upravlja seznam opravil."""

    def __init__(self, file_path=TASKS_FILE):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.file_path):
            return []
        tasks = []
        with open(self.file_path, "r", encoding="utf-8") as f:
            for line in f:
                description, done = line.strip().split("|")
                tasks.append(Task(description, done == "1"))
        return tasks

    def save_tasks(self):
        with open(self.file_path, "w", encoding="utf-8") as f:
            for task in self.tasks:
                f.write(f"{task.description}|{1 if task.done else 0}\n")

    def add_task(self, description):
        new_task = Task(description)
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"➕ Dodano opravilo: {description}")

    def remove_task(self, index):
        try:
            removed = self.tasks.pop(index - 1)
            self.save_tasks()
            print(f"❌ Opravljeno '{removed.description}' je odstranjeno.")
        except IndexError:
            print("⚠️ Napačna številka opravila.")

    def mark_done(self, index):
        try:
            self.tasks[index - 1].mark_done()
            self.save_tasks()
            print(
                f"✅ Opravilo '{self.tasks[index - 1].description}' označeno kot dokončano!"
            )
        except IndexError:
            print("⚠️ Napačna številka opravila.")

    def show_tasks(self):
        if not self.tasks:
            print("📭 Ni opravil.")
            return
        print("\n📋 Seznam opravil:")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")
        print()


class TodoApp:
    """Uporabniški vmesnik aplikacije (CLI)."""

    def __init__(self):
        self.todo_list = TodoList()

    def menu(self):
        while True:
            print("\n=== To-Do List ===")
            print("1. Prikaži opravila")
            print("2. Dodaj opravilo")
            print("3. Označi opravilo kot končano")
            print("4. Odstrani opravilo")
            print("5. Izhod")

            choice = input("Izberi možnost (1–5): ").strip()

            if choice == "1":
                self.todo_list.show_tasks()
            elif choice == "2":
                desc = input("Vnesi opis opravila: ").strip()
                self.todo_list.add_task(desc)
            elif choice == "3":
                self.todo_list.show_tasks()
                try:
                    num = int(input("Številka opravila: "))
                    self.todo_list.mark_done(num)
                except ValueError:
                    print("⚠️ Vnesi veljavno številko.")
            elif choice == "4":
                self.todo_list.show_tasks()
                try:
                    num = int(input("Številka opravila: "))
                    self.todo_list.remove_task(num)
                except ValueError:
                    print("⚠️ Vnesi veljavno številko.")
            elif choice == "5":
                print("👋 Izhod iz aplikacije. Lep dan!")
                break
            else:
                print("⚠️ Neveljavna izbira.")
