#! /usr/bin/env python
from __future__ import print_function, division
import cv2
import numpy as np


def arg_parser(args=None):
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("in_file", help="Path to input file")
    parser.add_argument("-o", "--out-file", help="Path to output file", default="out.jpg")
    parser.add_argument("-p", "--pixels-per-frame", help="Number of pixels to use for each frame", default=3, type=int)
    parser.add_argument("-s", "--sweep", help="How to scan accross the video", default="centre")
    return parser


def average(in_file, out_file="out.jpg"):
    # loading the video
    vidcap = cv2.VideoCapture(in_file)
    print("Frames:", vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    success, img = vidcap.read()
    print("shape:", img.shape)

    # establish a while loop for reading all the video frames
    frames = 0
    # accumulator in double precision
    avg = np.zeros_like(img.shape[:1])
    while success:
        avg = avg + cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        frames += 1
        success, img = vidcap.read()

    print ("Frames:", frames)
    return avg / frames


def append_pixel(in_file, out_file="out.jpg", pixels_per_frame=3, sweep="centre"):
    # loading the video
    vidcap = cv2.VideoCapture(in_file)
    frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    print("Frames:", frames)
    success, img = vidcap.read()
    print("shape:", img.shape)
    out_shape = list(img.shape)
    out_shape[1] = frames * pixels_per_frame
    print ("out_shape", out_shape)
    width = img.shape[1]

    if sweep == "centre":
        get_left_in_pixel = get_centre
    elif sweep == "left":
        get_left_in_pixel = sweep_left
    elif sweep == "right":
        get_left_in_pixel = sweep_right
    # establish a while loop for reading all the video frames
    current_frame = 0
    # accumulator in double precision
    output = np.zeros(out_shape, dtype=np.float64)
    while success:
        in_start = get_left_in_pixel(width, frames, current_frame, pixels_per_frame)
        out_start = pixels_per_frame * (frames - current_frame - 1)
        inslice = img[:, in_start:in_start + pixels_per_frame, :]
        output[:, out_start:out_start + pixels_per_frame, :] =  inslice
        current_frame += 1
        success, img = vidcap.read()

    return output


def get_centre(width, frames, current_frame, pixels_per_frame):
    return width // 2


def sweep_left(width, frames, current_frame, pixels_per_frame):
    return current_frame * (width - pixels_per_frame) // frames


def sweep_right(width, frames, current_frame, pixels_per_frame):
    return width - current_frame * (width - pixels_per_frame) // frames - pixels_per_frame


if __name__ == "__main__":
    args = arg_parser().parse_args()
    result = append_pixel(**vars(args))
    cv2.imwrite(args.out_file, result)
    print(result)
