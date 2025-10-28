import tkinter as tk
from tkinter import filedialog, messagebox
from vcsi_wrapper import VcsiWrapper

class VcsiGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("VCSI Interface - Gerador de Contact Sheets")
        self.vcsi = VcsiWrapper()

        # Video file
        tk.Label(root, text="Arquivo de Vídeo:").grid(row=0, column=0, sticky='w')
        self.video_entry = tk.Entry(root, width=50)
        self.video_entry.grid(row=0, column=1)
        tk.Button(root, text="Selecionar", command=self.select_video).grid(row=0, column=2)

        # Output file
        tk.Label(root, text="Arquivo de Saída:").grid(row=1, column=0, sticky='w')
        self.output_entry = tk.Entry(root, width=50)
        self.output_entry.grid(row=1, column=1)
        tk.Button(root, text="Selecionar", command=self.select_output).grid(row=1, column=2)

        # Width
        tk.Label(root, text="Largura:").grid(row=2, column=0, sticky='w')
        self.width_entry = tk.Entry(root)
        self.width_entry.insert(0, "1500")
        self.width_entry.grid(row=2, column=1, sticky='w')

        # Grid
        tk.Label(root, text="Grade (ex: 4x4):").grid(row=3, column=0, sticky='w')
        self.grid_entry = tk.Entry(root)
        self.grid_entry.insert(0, "4x4")
        self.grid_entry.grid(row=3, column=1, sticky='w')

        # Timestamp
        self.timestamp_var = tk.BooleanVar()
        tk.Checkbutton(root, text="Mostrar Timestamp", variable=self.timestamp_var).grid(row=4, column=0, columnspan=2, sticky='w')

        # Background color
        tk.Label(root, text="Cor de Fundo (hex):").grid(row=5, column=0, sticky='w')
        self.bg_color_entry = tk.Entry(root)
        self.bg_color_entry.insert(0, "000000")
        self.bg_color_entry.grid(row=5, column=1, sticky='w')

        # Metadata font color
        tk.Label(root, text="Cor da Fonte (hex):").grid(row=6, column=0, sticky='w')
        self.font_color_entry = tk.Entry(root)
        self.font_color_entry.insert(0, "ffffff")
        self.font_color_entry.grid(row=6, column=1, sticky='w')

        # Generate button
        tk.Button(root, text="Gerar Contact Sheet", command=self.generate).grid(row=7, column=0, columnspan=3)

    def select_video(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi *.mkv *.mov")])
        if file_path:
            self.video_entry.delete(0, tk.END)
            self.video_entry.insert(0, file_path)

    def select_output(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("Image files", "*.jpg *.png")])
        if file_path:
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, file_path)

    def generate(self):
        video = self.video_entry.get()
        output = self.output_entry.get()
        width = int(self.width_entry.get())
        grid = self.grid_entry.get()
        timestamp = self.timestamp_var.get()
        bg_color = self.bg_color_entry.get()
        font_color = self.font_color_entry.get()

        if not video or not output:
            messagebox.showerror("Erro", "Selecione o vídeo e o arquivo de saída.")
            return

        self.vcsi.set_video_file(video)
        self.vcsi.set_output_path(output)
        self.vcsi.set_width(width)
        self.vcsi.set_grid(grid)
        self.vcsi.set_background_color(bg_color)
        self.vcsi.set_metadata_font_color(font_color)
        if timestamp:
            self.vcsi.enable_timestamp()

        success = self.vcsi.create_contact_sheet()
        if success:
            messagebox.showinfo("Sucesso", "Contact sheet gerado com sucesso!")
        else:
            messagebox.showerror("Erro", "Falha ao gerar o contact sheet. Verifique se vcsi e ffmpeg estão instalados.")

if __name__ == '__main__':
    root = tk.Tk()
    app = VcsiGUI(root)
    root.mainloop()