"""
otsu_filter.py

implementation of Otsu Thresholding in a SCAR control harness.
"""

import cv2
import logging

import SCAR.Controls.control as control

class OtsuFilter(control.Control):
    """
    OtsuFilter

    Performs Otsu binarisation as a filter.
    """

    def apply_control(self):

        ret, th = cv2.threshold(self.base_image,
                                           0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        self.image_out = th

        return self.image_out
