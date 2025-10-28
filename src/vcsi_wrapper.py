import subprocess
import os

class VcsiWrapper:
    def __init__(self):
        self.video_file = None
        self.output_path = None
        self.width = 1500
        self.grid = '4x4'
        self.show_timestamp = False
        self.background_color = '000000'
        self.metadata_font_color = 'ffffff'

    def set_video_file(self, video_file):
        self.video_file = video_file

    def set_output_path(self, output_path):
        self.output_path = output_path

    def set_width(self, width):
        self.width = width

    def set_grid(self, grid):
        self.grid = grid

    def enable_timestamp(self):
        self.show_timestamp = True

    def set_background_color(self, color):
        self.background_color = color

    def set_metadata_font_color(self, color):
        self.metadata_font_color = color

    def create_contact_sheet(self):
        if not self.video_file or not self.output_path:
            raise ValueError("Video file and output path must be set.")

        command = ['vcsi', self.video_file, '-o', self.output_path, '-w', str(self.width), '-g', self.grid, '--background-color', self.background_color, '--metadata-font-color', self.metadata_font_color]

        if self.show_timestamp:
            command.append('-t')

        try:
            subprocess.run(command, check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error running vcsi: {e}")
            return False