#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 16:56:50 2021

WARNING: For educational purpose only. No warranty on the legality of it. 
         Use at your own risk.

Requirements: moviepy, pytube
@author: ikespand
"""

import os
import tempfile
import shutil
from moviepy import editor
from pytube import YouTube

def download_mp3_from_youtube(url:str, output_file_path:str=os.getcwd())-> str:
    """
    Download YouTube audio as MP3.

    Parameters
    ----------
    url : str
        URL of the video from YouTube.
    output_file_path : str, optional
        Location where mp3 is desired. The default is os.getcwd().

    Returns
    -------
    str
        Full path of saved mp3.

    """
    # Create a temporary dir to dump mp4 from YouTube
    tmp_dirpath = tempfile.mkdtemp()    
    
    # Fetch stream from YouTube
    yt = YouTube(url) 
    streams = yt.streams.filter(only_audio=True).all()
    #print("Available streams for audio -->")
    #[print (stream)for stream in streams]
    # Download to `tmp_dirpath`
    temp_file_path = streams[0].download(output_path=tmp_dirpath)
    song_name = os.path.basename(temp_file_path).split(".")[0]
    output_file_name = os.path.join(output_file_path,song_name + ".mp3")
    
    # Convert it to MP3 and save it to `tmp_dirpath`
    clip = editor.AudioFileClip(temp_file_path)
    clip.write_audiofile(output_file_name)

    #Delete the temporary dir
    shutil.rmtree(tmp_dirpath)
    return output_file_name
 #%%
if __name__ == "__main__":
    url = r"https://www.youtube.com/watch?v=M7F2KOQvzDc"
    output_file_name = download_mp3_from_youtube(url)
