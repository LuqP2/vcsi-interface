# vcsi-interface

![Build Status](https://github.com/yourusername/vcsi-interface/actions/workflows/testing.yml/badge.svg)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](http://opensource.org/licenses/MIT)

## Overview

The `vcsi-interface` project provides a simple and functional command-line interface for creating video contact sheets using the `vcsi` functionality. It leverages `uv` for command-line interactions and `ffmpeg` for video processing.

## Features

- Create video contact sheets from various video formats.
- Customize output parameters such as grid size, width, and background color.
- Support for metadata display and timestamping on contact sheets.

## Installation

To install the `vcsi-interface`, you need to have Python and `uv` installed. You can install the project using the following command:

```
uv tool install vcsi-interface
```

### Dependencies

Make sure to install the following dependencies:

- `uv`
- `ffmpeg`

You can install `ffmpeg` using your package manager. For example, on Ubuntu:

```
sudo apt-get install ffmpeg
```

## Usage

To create a video contact sheet, run the following command:

```
uv run src/main.py <video_file> [options]
```

### Example

```
uv run src/main.py bbb_sunflower_2160p_60fps_normal.mp4 -w 830 -g 4x4 --background-color 000000
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.