"""
gauss_filter.py

a simple gaussian blur filter for SCAR
"""

import logging
import numpy as np
import cv2

import SCAR.Controls.control as control

class GaussFilter(control.Control):
    """
    GaussFilter

    a simple Gaussian blur filter control
    """

    def apply_control(self):

        self.image_out = cv2.GaussianBlur(self.base_image, (25, 25), 0)

        return self.image_out
