from scipy.io import loadmat
import os

# loads utk face images/labels from .mat file and returns python lists
def load_data(mat_path):
    d = loadmat(mat_path)
    return d["images"], d["genders"][0], d["ages"][0], d["ethnicities"][0], d["img_size"][0, 0]

# makes directory, catching exceptions
def mk_dir(dir):
    try:
        os.mkdir( dir )
    except OSError:
        pass
