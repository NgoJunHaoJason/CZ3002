'''
Demo for face detection and gender recognition using computer's webcam
'''
import argparse
import cv2
import mxnet as mx
import numpy as np
import os

from camera import Camera
from face_detection import LFFD
from gender_classification import SSRNet
from violation_handling import Notifier


def parse_args():
    '''
    Parse arguments for this program
    '''
    parser = argparse.ArgumentParser(
        prog='camera',
        description='detect face and recognise gender using image from camera'
    )

    parser.add_argument(
        '--debug',
        action='store_true',
        help='whether to run in debug mode'
    )

    parser.add_argument(
        '--camera_id',
        type=str,
        default='0',
        help='id of the camera',
    )

    parser.add_argument(
        '--toilet_gender',
        type=int,
        default='0',
        help='the gender of the toilet being monitored by the camera (0 for female, 1 for male)',
    )

    parser.add_argument(
        '--toilet_location',
        type=str,
        default='N3-01-01',
        help='location of the toilet being monitored by the camera',
    )

    parser.add_argument(
        '--notification_interval',
        type=int,
        default=5,
        help='time interval (in seconds) between each notification',
    )

    parser.add_argument(
        '--lffd_symbol_file_path',
        type=str,
        default='face_detection/model/symbol_10_560_25L_8scales_v1_deploy.json',
        help='path to symbol file of face detection model',
    )

    parser.add_argument(
        '--lffd_model_file_path',
        type=str,
        default='face_detection/model/train_10_560_25L_8scales_v1_iter_1400000.params',
        help='path to model params of face detection model',
    )

    parser.add_argument(
        '--ssrnet_prefix',
        type=str,
        default='gender_recognition/ssr2_imdb_gender/model',
        help='prefix (path) for gender recognition model',
    )

    parser.add_argument(
        '--ssrnet_epoch_num',
        type=int,
        default=0,
        help='epoch at which gender recognition model was saved',
    )

    return parser.parse_args()


def main(args):
    '''
    The main program
    '''   
    context = mx.cpu()
    
    face_detector = LFFD(
        symbol_file_path=args.lffd_symbol_file_path,
        model_file_path=args.lffd_model_file_path,
    )

    gender_classifier = SSRNet(
        prefix=args.ssrnet_prefix,
        epoch=args.ssrnet_epoch_num,
    )

    notifier = Notifier()

    camera = Camera(
        args.toilet_gender,
        args.toilet_location,
        args.notification_interval,
        face_detector,
        gender_classifier,
        notifier,
    )
    camera.run(debug=args.debug)


if __name__ == '__main__':
    args = parse_args()

    if not os.path.exists(args.lffd_symbol_file_path):
        print('The symbol file does not exist!')
        exit(1)
    
    if not os.path.exists(args.lffd_model_file_path):
        print('The model file does not exist!')
        exit(1)
    
    main(args)
    print('\ncamera stopped')
