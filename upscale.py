import argparse
import sys
from pathlib import Path

from realesrgan import Realesrgan

def main():
    MODELS = {'realesrgan',
            'realesrgan-anime',
            'realesrgan-anime-video'
    }
    INFILES = Path.cwd() / 'infiles'
    OUTFILES = Path.cwd() / 'outfiles'

    parser = argparse.ArgumentParser(
        epilog = "Use -l or --list to view available upscaling models."
    )
    parser.add_argument('-m', '--model', required=True)
    parser.add_argument('-i', '--infile', required=True)
    parser.add_argument('-o', '--outfile', required=True)
    parser.add_argument('-l', '--list', action='store_true')

    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
        return
    
    if args.list:
        print("upscaler-suite supported models:")
        for model in sorted(MODELS):
            print(model)
        return
    
    if args.model not in MODELS:
        raise Exception(
        "Unrecognized model.\n"
        "Use 'python upscale.py -l' or 'python upscale.py --list' to see available models."
        )
    
    infile = INFILES / Path(args.infile)
    outfile = OUTFILES / Path(args.outfile)
    if not infile.is_file():
        raise Exception("infile does not exist, or is a directory.\n"
                        "Tried looking for:\n\n"
                        f"{infile}\n"
                        "Infile should be in 'upscaler-suite/infiles' or its subdirectories.")
    
    model = {
        'realesrgan': 'realesrgan-x4plus',
        'realesrgan-anime': 'realesrgan-x4plus-anime',
        'realesrgan-anime-video': 'realesr-animevideov3'
    }.get(model)

    match infile.suffix:
        case 'pdf': 
            match outfile.suffix:
                case 'pdf':
                    pdf_to_pdf()
                case _:
                    raise Exception("pdf files can only be upscaled into pdf files.")
    while True:
        raise NotImplementedError
    
def pdf_to_pdf():
    raise NotImplementedError
if __name__ == '__main__':
    main()