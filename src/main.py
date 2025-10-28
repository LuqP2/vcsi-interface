from vcsi_wrapper import VcsiWrapper
import os

def main():
    vcsi = VcsiWrapper()

    print("VCSI Interface - Gerador de Contact Sheets")
    print("==========================================")

    video_file = input("Caminho do arquivo de vídeo: ").strip()
    if not video_file or not os.path.exists(video_file):
        print("Arquivo de vídeo inválido.")
        return

    output_file = input("Caminho do arquivo de saída (ex: output.jpg): ").strip()
    if not output_file:
        print("Arquivo de saída inválido.")
        return

    grid = input("Grade (ex: 4x4): ").strip() or '4x4'
    width = input("Largura (ex: 1500): ").strip()
    width = int(width) if width.isdigit() else 1500

    show_timestamp = input("Mostrar timestamp? (s/n): ").strip().lower() == 's'

    bg_color = input("Cor de fundo (hex, ex: 000000): ").strip() or '000000'
    font_color = input("Cor da fonte (hex, ex: ffffff): ").strip() or 'ffffff'

    vcsi.set_video_file(video_file)
    vcsi.set_output_path(output_file)
    vcsi.set_grid(grid)
    vcsi.set_width(width)
    vcsi.set_background_color(bg_color)
    vcsi.set_metadata_font_color(font_color)
    if show_timestamp:
        vcsi.enable_timestamp()

    print("Gerando contact sheet...")
    success = vcsi.create_contact_sheet()
    if success:
        print("Sucesso! Contact sheet gerado em:", output_file)
    else:
        print("Erro ao gerar o contact sheet. Verifique se vcsi e ffmpeg estão instalados.")

if __name__ == '__main__':
    main()