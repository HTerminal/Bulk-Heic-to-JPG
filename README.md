# Bulk-Heic-to-JPG
Convert your Iphone HEIC images to JPG in bulk
# Convert HEIC Images to JPG with ImageMagick

This guide provides step-by-step instructions on how to use Python and ImageMagick to convert `.heic` images to `.jpg` format.

## Requirements

1. **Python 3.x** - Make sure you have Python installed. You can download it from [here](https://www.python.org/downloads/).
2. **ImageMagick** - Download and install ImageMagick, ensuring the `convert` feature is enabled. You can download it from [here](https://imagemagick.org/script/download.php).
    - During installation, check the box for "Install legacy utilities (e.g., convert)" to enable the `convert` command.

## Installation

1. **Install ImageMagick**:
    - Download the installer from [ImageMagick's official page](https://imagemagick.org/script/download.php).
    - Run the installer, selecting the `convert` feature as mentioned above.
    - Note the installation path (default is usually `C:\Program Files\ImageMagick-[version]`).

2. **Install Python Libraries**:
    - This script does not require additional libraries, as it uses only built-in modules.

## Script Usage

1. **Update the Script with Your Paths**:
    - Set the `heicImg` path to the directory containing your `.heic` images.
    - Set the `imageMagickPath` to the installation path of ImageMagick.

2. **Run the Script**:
    - Save the code below into a Python file, e.g., `heic_to_jpg.py`.
    - Open a terminal or command prompt and navigate to the file location.
    - Run the script with `python heic_to_jpg.py`.

```python
import glob, os, subprocess

# Specify the directory containing .heic images
heicImg = glob.glob(r"C:\Users\Hitesh\Desktop\Print\img\*.heic")

# Specify the ImageMagick installation path
imageMagickPath = "C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI"

print(heicImg)
print('=====start heic2jpg=====')

for heicName in heicImg:
    input = heicName
    dirname = os.path.dirname(input)
    basename_without_ext = os.path.splitext(os.path.basename(input))[0]
    output = os.path.join(dirname, basename_without_ext + ".jpg")
    
    print('=====')
    print("input: " + input)
    print("output: " + output)
    print('=====Run ImageMagick=====')
    print('Command')
    print(os.path.join(imageMagickPath, "magick convert") + " " + input + " " + output)
    
    # Run the conversion command
    subprocess.run([os.path.join(imageMagickPath, "magick"), "convert", input, output])

print('=====finished=====')
