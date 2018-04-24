"""
control.py

this is the code that contains a demo control object,
which can be extended to be a "filter".

"""

import numpy as np
import cv2
import logging

class Control:


    def __init__(self) -> None:
        """
        Constructor.

        Requires an image to be put in.

        """
        try:
            super().__init__()
            self.base_image = None
            self.image_out = None
        except cv2.error as CVError:
            logging.error("ERROR: could not create Control object.")

    def __str__(self) -> str:
        """
        toString method-- for debugging, really.

        :return:
        """
        return super().__str__()

    def set_image(self, image) -> None:
        """
        This sets an image to use.
        :param image:
        :return:
        """
        self.base_image = image
        self.image_out = self.apply_control()

    def apply_control(self) -> None:
        """
        apply_control method

        this is what is overridden when you create your own control.
        :return:

        """
        self.image_out = self.base_image
        return self.image_out