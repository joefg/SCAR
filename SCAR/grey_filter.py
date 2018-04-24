"""
grey_filter.py

A simple grayscale filter, using SCAR's filter system.
"""

import logging
import numpy as np
import cv2

import SCAR.Controls.control as control

class GrayFilter(control.Control):
    """
    GrayFilter

    a simple demonstration of an overridden control method.
    """

    def apply_control(self):
        """
        apply_control - overridden method for applying a control
        """
        self.image_out = cv2.cvtColor(self.base_image, cv2.COLOR_BGR2GRAY)

        return self.image_out
