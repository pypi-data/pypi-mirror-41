
from __future__ import absolute_import
from __future__ import print_function

import logging
logger = logging.getLogger(__name__)

import sys
import os
import re
import numpy as np
from imageio import imread


def _absPath(myPath):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    import sys

    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
        logger.DEBUG("found MEIPASS: %s "%os.path.join(base_path, os.path.basename(myPath)))

        return os.path.join(base_path, os.path.basename(myPath))
    except Exception:
        base_path = os.path.abspath(os.path.dirname(__file__))
        return os.path.join(base_path, myPath)

def _arrayFromImage(fName):
    """converts png image to float32 array
    returns an array of shape [h,w,3]
    """
    img = np.asarray(imread(fName))

    if len(img.shape)<3:
        raise TypeError("image %s appears not to be a 2d rgb image"%fName)

    return 1./255*img[:,:,:3]


def loadcolormaps():
    cmaps = {}

    try:
        basePath = sys._MEIPASS
    except:
        basePath = _absPath("../colormaps/")

    reg = re.compile("cmap_(.*)\.png")
    for fName in os.listdir(basePath):
        match = reg.match(fName)
        if match:
            try:
                cmaps[match.group(1)] = _arrayFromImage(os.path.join(basePath,fName))[0,:,:]
            except Exception as e:
                print(e)
                print("could not load %s"%fName)

    return cmaps


if __name__ == '__main__':
    from time import time

    t = time()
    
    d =  loadcolormaps()

    print("time to load cmaps: %s s"%(time()-t))

    print(len(d))
