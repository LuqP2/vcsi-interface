from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox, QCheckBox
from PyQt5.QtCore import Qt
from vcsi_wrapper import VcsiWrapper
import sys
import os

class VcsiGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.vcsi = VcsiWrapper()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("VCSI Interface - Gerador de Contact Sheets")
        self.setGeometry(300, 300, 600, 400)

        layout = QVBoxLayout()

        # Video file
        video_layout = QHBoxLayout()
        video_layout.addWidget(QLabel("Arquivo de Vídeo:"))
        self.video_entry = QLineEdit()
        video_layout.addWidget(self.video_entry)
        video_btn = QPushButton("Selecionar")
        video_btn.clicked.connect(self.select_video)
        video_layout.addWidget(video_btn)
        layout.addLayout(video_layout)

        # Output file
        output_layout = QHBoxLayout()
        output_layout.addWidget(QLabel("Arquivo de Saída:"))
        self.output_entry = QLineEdit()
        output_layout.addWidget(self.output_entry)
        output_btn = QPushButton("Selecionar")
        output_btn.clicked.connect(self.select_output)
        output_layout.addWidget(output_btn)
        layout.addLayout(output_layout)

        # Width
        width_layout = QHBoxLayout()
        width_layout.addWidget(QLabel("Largura:"))
        self.width_entry = QLineEdit("1500")
        width_layout.addWidget(self.width_entry)
        layout.addLayout(width_layout)

        # Grid
        grid_layout = QHBoxLayout()
        grid_layout.addWidget(QLabel("Grade (ex: 4x4):"))
        self.grid_entry = QLineEdit("4x4")
        grid_layout.addWidget(self.grid_entry)
        layout.addLayout(grid_layout)

        # Timestamp
        self.timestamp_cb = QCheckBox("Mostrar Timestamp")
        layout.addWidget(self.timestamp_cb)

        # Background color
        bg_layout = QHBoxLayout()
        bg_layout.addWidget(QLabel("Cor de Fundo (hex):"))
        self.bg_entry = QLineEdit("000000")
        bg_layout.addWidget(self.bg_entry)
        layout.addLayout(bg_layout)

        # Font color
        font_layout = QHBoxLayout()
        font_layout.addWidget(QLabel("Cor da Fonte (hex):"))
        self.font_entry = QLineEdit("ffffff")
        font_layout.addWidget(self.font_entry)
        layout.addLayout(font_layout)

        # Generate button
        generate_btn = QPushButton("Gerar Contact Sheet")
        generate_btn.clicked.connect(self.generate)
        layout.addWidget(generate_btn)

        self.setLayout(layout)

    def select_video(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Selecionar Vídeo", "", "Video files (*.mp4 *.avi *.mkv *.mov)")
        if file_path:
            self.video_entry.setText(file_path)

    def select_output(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Salvar Contact Sheet", "", "Image files (*.jpg *.png)")
        if file_path:
            self.output_entry.setText(file_path)

    def generate(self):
        video = self.video_entry.text()
        output = self.output_entry.text()
        width = int(self.width_entry.text()) if self.width_entry.text().isdigit() else 1500
        grid = self.grid_entry.text()
        timestamp = self.timestamp_cb.isChecked()
        bg_color = self.bg_entry.text()
        font_color = self.font_entry.text()

        if not video or not os.path.exists(video):
            QMessageBox.warning(self, "Erro", "Selecione um arquivo de vídeo válido.")
            return
        if not output:
            QMessageBox.warning(self, "Erro", "Selecione o arquivo de saída.")
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
            QMessageBox.information(self, "Sucesso", "Contact sheet gerado com sucesso!")
        else:
            QMessageBox.critical(self, "Erro", "Falha ao gerar o contact sheet. Verifique se vcsi e ffmpeg estão instalados.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VcsiGUI()
    ex.show()
    sys.exit(app.exec_())