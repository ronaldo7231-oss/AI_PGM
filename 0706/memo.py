import tkinter as tk
from tkinter import filedialog, messagebox

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Notepad")
        self.root.geometry("800x600")

        self.file_path = None

        # ---------------- Text Area ----------------
        self.text = tk.Text(root, wrap="word", undo=True, font=("Consolas", 12))
        self.text.pack(expand=True, fill="both")

        # 스크롤바
        scrollbar = tk.Scrollbar(self.text)
        scrollbar.pack(side="right", fill="y")
        self.text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.text.yview)

        # ---------------- Menu ----------------
        self.menu = tk.Menu(root)
        root.config(menu=self.menu)

        file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)

        edit_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Undo", command=self.text.edit_undo)
        edit_menu.add_command(label="Redo", command=self.text.edit_redo)
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", command=lambda: self.text.event_generate("<<Cut>>"))
        edit_menu.add_command(label="Copy", command=lambda: self.text.event_generate("<<Copy>>"))
        edit_menu.add_command(label="Paste", command=lambda: self.text.event_generate("<<Paste>>"))
        edit_menu.add_command(label="Select All", command=self.select_all)

        # ---------------- Status Bar ----------------
        self.status = tk.StringVar()
        self.status.set("Characters: 0")

        self.status_bar = tk.Label(root, textvariable=self.status, anchor="w")
        self.status_bar.pack(side="bottom", fill="x")

        # 글자수 업데이트
        self.text.bind("<KeyRelease>", self.update_status)

        # 단축키
        self.bind_shortcuts()

    # ---------------- 기능 ----------------
    def new_file(self):
        self.text.delete(1.0, tk.END)
        self.file_path = None

    def open_file(self):
        file = filedialog.askopenfilename()
        if file:
            with open(file, "r", encoding="utf-8") as f:
                content = f.read()
            self.text.delete(1.0, tk.END)
            self.text.insert(tk.END, content)
            self.file_path = file

    def save_file(self):
        if self.file_path:
            with open(self.file_path, "w", encoding="utf-8") as f:
                f.write(self.text.get(1.0, tk.END))
        else:
            self.save_as()

    def save_as(self):
        file = filedialog.asksaveasfilename(defaultextension=".txt")
        if file:
            with open(file, "w", encoding="utf-8") as f:
                f.write(self.text.get(1.0, tk.END))
            self.file_path = file

    def select_all(self):
        self.text.tag_add("sel", "1.0", "end")

    def update_status(self, event=None):
        text_length = len(self.text.get(1.0, tk.END)) - 1
        self.status.set(f"Characters: {text_length}")

    def bind_shortcuts(self):
        self.root.bind("<Control-n>", lambda e: self.new_file())
        self.root.bind("<Control-o>", lambda e: self.open_file())
        self.root.bind("<Control-s>", lambda e: self.save_file())
        self.root.bind("<Control-a>", lambda e: self.select_all())

# ---------------- 실행 ----------------
root = tk.Tk()
app = Notepad(root)
root.mainloop()