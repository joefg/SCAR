"""
canny.py

A Canny Edge Detector filter for SCAR-like architectures.
"""

import logging
import numpy as np
import cv2

import SCAR.Controls.control as control

class CannyFilter(control.Control):
    """
    CannyFilter

    Another demonstration of the SCAR architecture.
    """

    def apply_control(self):

        self.image_out = cv2.Canny(self.base_image, 100, 100)

        return self.image_out
