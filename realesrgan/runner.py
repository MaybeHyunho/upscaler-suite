import subprocess
from pathlib import Path

class Realesrgan():
    def __init__(self, model, infile, outfile):
        self.model = model
        self.infile = infile
        self.outfile = outfile
        exepath = Path.cwd() / 'realesrgan' / 'realesrgan-ncnn-vulkan.exe'
        subprocess.call([str(exepath), 
                       '-i', str(infile),
                       '-o', str(outfile), 
                       '-n', str(model)])
        