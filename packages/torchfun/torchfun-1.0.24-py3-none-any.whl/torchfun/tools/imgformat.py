import os,shutil
from glob import glob
from tqdm import tqdm
from sys import argv
import argparse

parser = argparse.ArgumentParser(description='Image Format Transformer')
parser.add_argument('files', metavar='FILE_PATTERN', type=str, nargs='+',
                        help='files to be transformed')
parser.add_argument('-t','--type',dest='type', type=str, default=None, help='output image type')
parser.add_argument('-d','--dir',dest='dir', type=str, default=None, help='dir to store output images, default: same dir as the input image.')

def imgformat():
    import imageio
    opt=parser.parse_args(argv[1:])
    if not opt.type:
        print('please specify output type by -t or --type possible values: png,jpg,eps,bmp,gif...')
        return 0
    else:
        opt.type = opt.type.lower()

    more_files = []
    files = []
    for fpath in opt.files:
        if '*' in fpath:
            more_files.extend(glob(fpath))
        else:
            files.append(fpath)
    all_fpaths = list(set(more_files+files))
    filenumbers = len(all_fpaths)
    for i,imgpath in enumerate(all_fpaths):
        srcdir = os.path.dirname(imgpath)
        srcname = os.path.basename(imgpath)
        srctag = '.'.join(srcname.split('.')[:-1])
        srctype = srcname.split('.')[-1].lower()
        destdir = opt.dir or srcdir
        destpath = os.path.join(destdir,srctag+'.'+opt.type)
        if opt.type == srctype:
            if os.path.abspath(srcdir) != os.path.abspath(destdir): 
                shutil.copy(imgpath,destpath)
                print(i,'/',filenumbers,imgpath,'copy->',destpath)
            else:
                print(i,'/',filenumbers,'skipping',imgpath)
        else:
            print(i,'/',filenumbers,imgpath,'->',destpath)
            imageio.imsave(destpath,imageio.imread(imgpath))
    print('finished.')
    return 0

def main():
    return imgformat()

if __name__ == '__main__':
  main()