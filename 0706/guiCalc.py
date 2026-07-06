import tkinter as tk
from tkinter import ttk


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('GUI Calculator')
        self.resizable(False, False)
        self.geometry('300x380')
        self._create_widgets()
        self._bind_keys()

    def _create_widgets(self):
        self.display_var = tk.StringVar()
        entry = ttk.Entry(self, textvariable=self.display_var, font=('Segoe UI', 18), justify='right')
        entry.pack(fill='x', padx=10, pady=10)
        entry.focus_set()

        btns = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '±', '+'),
        ]

        frame = ttk.Frame(self)
        frame.pack(expand=True, fill='both', padx=10, pady=5)

        for r, row in enumerate(btns):
            for c, ch in enumerate(row):
                b = ttk.Button(frame, text=ch, command=lambda v=ch: self._on_button(v))
                b.grid(row=r, column=c, sticky='nsew', padx=2, pady=2)

        for i in range(4):
            frame.columnconfigure(i, weight=1)
        for i in range(4):
            frame.rowconfigure(i, weight=1)

        bottom = ttk.Frame(self)
        bottom.pack(fill='x', padx=10, pady=5)

        eq = ttk.Button(bottom, text='=', command=self._calculate)
        eq.pack(side='left', expand=True, fill='x', padx=(0,5))
        clear = ttk.Button(bottom, text='C', command=self._clear)
        clear.pack(side='left', expand=True, fill='x', padx=5)
        back = ttk.Button(bottom, text='⌫', command=self._backspace)
        back.pack(side='left', expand=True, fill='x', padx=(5,0))

    def _on_button(self, v):
        if v == '±':
            self._toggle_sign()
            return
        self.display_var.set(self.display_var.get() + v)

    def _toggle_sign(self):
        s = self.display_var.get()
        if not s:
            return
        try:
            if s.startswith('-'):
                self.display_var.set(s[1:])
            else:
                self.display_var.set('-' + s)
        except Exception:
            pass

    def _clear(self):
        self.display_var.set('')

    def _backspace(self):
        self.display_var.set(self.display_var.get()[:-1])

    def _calculate(self):
        expr = self.display_var.get()
        if not expr:
            return
        try:
            # safe eval: allow only digits, operators, parentheses, dot
            safe = ''.join(ch for ch in expr if ch in '0123456789+-*/().')
            result = eval(safe, {'__builtins__': None}, {})
            self.display_var.set(str(result))
        except Exception:
            self.display_var.set('Error')

    def _bind_keys(self):
        for key in '0123456789+-*/().':
            self.bind(key, lambda e, k=key: self._on_button(k))
        self.bind('<Return>', lambda e: self._calculate())
        self.bind('=', lambda e: self._calculate())
        self.bind('<BackSpace>', lambda e: self._backspace())
        self.bind('<Delete>', lambda e: self._clear())
        self.bind('<Escape>', lambda e: self._clear())
        # plus/minus with 'p' or 'm'
        self.bind('p', lambda e: self._toggle_sign())
        self.bind('m', lambda e: self._toggle_sign())


if __name__ == '__main__':
    app = Calculator()
    app.mainloop()
