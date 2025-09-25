import tkinter as tk
from tkinter import messagebox
import ollama

MODEL = "phi3"

def generate_commit_title(hint: str) -> str:
    prompt = f"""Buatkan judul commit Git dari ide berikut:

"{hint}"

Aturan:
- subject ≤ 60 karakter
- gunakan imperative mood (misalnya "Add", "Fix", "Refactor")
- balas hanya SATU baris judul commit

Contoh:
- Fix an ID not found Issue
- Add Error Message for fail login
- Add Try Catch for login
"""
    resp = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    return resp["message"]["content"].strip()

def on_generate():
    hint = entry.get("1.0", tk.END).strip()
    if not hint:
        messagebox.showwarning("Warning", "Masukkan ide commit dulu!")
        return

    try:
        title = generate_commit_title(hint)
        output_var.set(title)
    except Exception as e:
        messagebox.showerror("Error", f"Gagal generate commit: {e}")

def on_copy():
    result = output_var.get()
    if result:
        root.clipboard_clear()
        root.clipboard_append(result)
        root.update()
        messagebox.showinfo("Copied", "Judul commit berhasil dicopy!")

# === GUI ===
root = tk.Tk()
root.title("Commit Title Generator Ver. 1.1")

# input box
tk.Label(root, text="Masukkan ide commit:").pack(anchor="w", padx=10, pady=(10, 0))
entry = tk.Text(root, height=4, width=60)
entry.pack(padx=10, pady=5)

# tombol
tk.Button(root, text="Generate Judul Commit", command=on_generate).pack(pady=5)

# output
tk.Label(root, text="Hasil judul commit:").pack(anchor="w", padx=10, pady=(10, 0))
output_var = tk.StringVar()
output_entry = tk.Entry(root, textvariable=output_var, width=60, state="readonly")
output_entry.pack(padx=10, pady=5)

# tombol copy
tk.Button(root, text="Copy ke Clipboard", command=on_copy).pack(pady=(0, 10))

root.mainloop()
