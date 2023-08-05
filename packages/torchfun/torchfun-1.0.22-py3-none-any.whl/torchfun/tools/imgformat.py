import os
from glob import glob
from tqdm import tqdm
from sys import argv
import argparse

parser = argparse.ArgumentParser(description='Image Format Transformer')
parser.add_argument('files', metavar='N', type=str, nargs='+',
                        help='files to be transformed')
parser.add_argument('--type',dest='type', type=str, default=None, help='output image type')

def imgformat():
    import imageio
    opt=parser.parse_args(argv[1:])
    print(opt.files,opt.type)
    return 0

#    files = glob(os.path.join(folder_path,'*.png'))
#    for fp in tqdm(files):
#        fparts = fp.split('.')
#        fparts[-1]='eps'
#        target = '.'.join(fparts)
#        img = img = imageio.imread(fname)


def main():
    return imgformat()

if __name__ == '__main__':
  main()