import tkinter as tk
from tkinter import ttk  # Importar ttk explícitamente
from tkinter import messagebox
import ipaddress

class IPCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de IPs")

        # Crear pestañas para IPv4 e IPv6
        self.tab_control = ttk.Notebook(root)  # Usar ttk.Notebook

        self.tab_ipv4 = tk.Frame(self.tab_control)
        self.tab_ipv6 = tk.Frame(self.tab_control)

        self.tab_control.add(self.tab_ipv4, text="IPv4")
        self.tab_control.add(self.tab_ipv6, text="IPv6")

        self.tab_control.pack(expand=1, fill="both")

        # Interfaz para IPv4
        self.label_ipv4 = tk.Label(self.tab_ipv4, text="Introduce una dirección IPv4 y máscara (ej. 192.168.1.1/24):")
        self.label_ipv4.pack(pady=10)

        self.entry_ipv4 = tk.Entry(self.tab_ipv4, width=30)
        self.entry_ipv4.pack(pady=10)

        self.button_calculate_ipv4 = tk.Button(self.tab_ipv4, text="Calcular", command=self.calculate_ipv4)
        self.button_calculate_ipv4.pack(pady=10)

        self.result_ipv4 = tk.Label(self.tab_ipv4, text="")
        self.result_ipv4.pack(pady=10)

        # Interfaz para IPv6
        self.label_ipv6 = tk.Label(self.tab_ipv6, text="Introduce una dirección IPv6 y prefijo (ej. 2001:db8::/32):")
        self.label_ipv6.pack(pady=10)

        self.entry_ipv6 = tk.Entry(self.tab_ipv6, width=30)
        self.entry_ipv6.pack(pady=10)

        self.button_calculate_ipv6 = tk.Button(self.tab_ipv6, text="Calcular", command=self.calculate_ipv6)
        self.button_calculate_ipv6.pack(pady=10)

        self.result_ipv6 = tk.Label(self.tab_ipv6, text="")
        self.result_ipv6.pack(pady=10)

    def calculate_ipv4(self):
        try:
            ip_network = ipaddress.IPv4Network(self.entry_ipv4.get(), strict=False)
            result = f"Dirección de red: {ip_network.network_address}\n"
            result += f"Máscara de red: {ip_network.netmask}\n"
            result += f"Dirección de broadcast: {ip_network.broadcast_address}\n"
            result += f"Número de hosts: {ip_network.num_addresses - 2}\n"
            self.result_ipv4.config(text=result)
        except ValueError as e:
            messagebox.showerror("Error", f"Entrada inválida: {e}")

    def calculate_ipv6(self):
        try:
            ip_network = ipaddress.IPv6Network(self.entry_ipv6.get(), strict=False)
            result = f"Dirección de red: {ip_network.network_address}\n"
            result += f"Prefijo de red: /{ip_network.prefixlen}\n"
            result += f"Número de hosts: {ip_network.num_addresses}\n"
            self.result_ipv6.config(text=result)
        except ValueError as e:
            messagebox.showerror("Error", f"Entrada inválida: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = IPCalculatorApp(root)
    root.mainloop()