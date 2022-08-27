# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 12:38:12 2022

Converts HEIC format given by iPhone to JPEG/PNG.

@author: PC
"""

from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()


def convert_heic_to(heic_path:str, desired_format:str="png", desired_format_full_name:str = None):   
    """
    Saves the heic file into the desired format, tested with png on windows so far.

    Parameters
    ----------
    heic_path : str 
        Complete path of heic file..
    desired_format : str, optional
        Desired output format. The default is "png".
    desired_format_full_name : str, optional
        If you want to save output at other place then provide complete path + name incl. extension. The default is None.

    Returns
    -------
    None.

    """
    if desired_format_full_name is None:
        new_format_fname = heic_path.split(".")[0]+ "." + desired_format
    else:
        new_format_fname = desired_format_full_name
    
    print("Processing >> `{}` \nAnd saving it as `{}`".format(heic_path, new_format_fname))

    image = Image.open(heic_path)
    image.save(new_format_fname, format = desired_format)
    return new_format_fname
# %%
if __name__ == "__main__":
    desired_format = "png"
    heic_path = r"C:\Users\PC\Documents\SpouceVisaDocuments\IMG_0684.HEIC"
    convert_heic_to(heic_path)
