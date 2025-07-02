import tkinter as tk
from tkinter import messagebox

estudiantes = []

# Funciones
def agregar_estudiante():
    if len(estudiantes) >= 3:
        messagebox.showwarning("Límite alcanzado", "Ya se han registrado 3 estudiantes.")
        return

    nombre = entry_nombre.get().strip()
    edad = entry_edad.get().strip()
    nota = entry_nota.get().strip()

    try:
        if not nombre:
            messagebox.showerror("Error", "El nombre no puede estar vacío.")
            return
        edad = int(edad)
        if edad <= 0:
            messagebox.showerror("Error", "La edad debe ser mayor que 0.")
            return
        nota = float(nota)
        if not (0 <= nota <= 5):
            messagebox.showerror("Error", "La nota debe estar entre 0 y 5.")
            return
        estudiantes.append([nombre, edad, nota])
        messagebox.showinfo("Éxito", f"Estudiante {nombre} registrado.")
        entry_nombre.delete(0, tk.END)
        entry_edad.delete(0, tk.END)
        entry_nota.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Edad y nota deben ser numéricos.")

def mostrar_estudiantes():
    texto_resultado.delete("1.0", tk.END)
    if not estudiantes:
        texto_resultado.insert(tk.END, "No hay estudiantes registrados.\n")
    else:
        for i, est in enumerate(estudiantes, 1):
            texto_resultado.insert(tk.END, f"{i}. {est[0]} - Edad: {est[1]} años - Nota: {est[2]:.2f}\n")

def mostrar_promedio():
    texto_resultado.delete("1.0", tk.END)
    if not estudiantes:
        texto_resultado.insert(tk.END, "No hay estudiantes registrados.\n")
    else:
        promedio = sum(est[2] for est in estudiantes) / len(estudiantes)
        texto_resultado.insert(tk.END, f"Promedio de notas: {promedio:.2f}\n")

def mostrar_mayores():
    texto_resultado.delete("1.0", tk.END)
    mayores = [est for est in estudiantes if est[1] >= 18]
    if mayores:
        for i, est in enumerate(mayores, 1):
            texto_resultado.insert(tk.END, f"{i}. {est[0]} - {est[1]} años\n")
    else:
        texto_resultado.insert(tk.END, "No hay estudiantes mayores de edad.\n")

def mostrar_aprobados():
    texto_resultado.delete("1.0", tk.END)
    aprobados = [est for est in estudiantes if est[2] >= 3.0]
    if aprobados:
        for i, est in enumerate(aprobados, 1):
            texto_resultado.insert(tk.END, f"{i}. {est[0]} - Nota: {est[2]:.2f}\n")
    else:
        texto_resultado.insert(tk.END, "Ningún estudiante aprobó.\n")

def mostrar_mejor():
    texto_resultado.delete("1.0", tk.END)
    if not estudiantes:
        texto_resultado.insert(tk.END, "No hay estudiantes registrados.\n")
    else:
        mejor = max(estudiantes, key=lambda est: est[2])
        texto_resultado.insert(tk.END, f"Mejor estudiante: {mejor[0]} - Nota: {mejor[2]:.2f}\n")

# Interfaz
ventana = tk.Tk()
ventana.title("Gestión de Estudiantes")
ventana.geometry("500x600")

# Entradas
tk.Label(ventana, text="Nombre:").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Edad:").pack()
entry_edad = tk.Entry(ventana)
entry_edad.pack()

tk.Label(ventana, text="Nota Final:").pack()
entry_nota = tk.Entry(ventana)
entry_nota.pack()

tk.Button(ventana, text="Agregar Estudiante", command=agregar_estudiante).pack(pady=5)

# Botones de acciones
tk.Button(ventana, text="Ver Estudiantes", command=mostrar_estudiantes).pack(pady=2)
tk.Button(ventana, text="Promedio de Notas", command=mostrar_promedio).pack(pady=2)
tk.Button(ventana, text="Estudiantes Mayores", command=mostrar_mayores).pack(pady=2)
tk.Button(ventana, text="Estudiantes Aprobados", command=mostrar_aprobados).pack(pady=2)
tk.Button(ventana, text="Mejor Estudiante", command=mostrar_mejor).pack(pady=2)

# Área de resultados
tk.Label(ventana, text="Resultados:").pack(pady=5)
texto_resultado = tk.Text(ventana, height=15, width=60)
texto_resultado.pack()

ventana.mainloop()
