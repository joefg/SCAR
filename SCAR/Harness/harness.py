"""
harness.py

this holds the harness class, which contains a list of controls to
modify an image.

"""

import logging

class Harness:


    def __init__(self) -> None:
        """
        Constructor.

        """
        super().__init__()
        self.controls = []
        self.base_image = None
        self.current_image = self.base_image
        logging.info("Harness created.")

    def __str__(self) -> str:
        """
        ToString.
        :return:
        """
        return super().__str__() + "Harness."

    def add_control(self, control):
        """
        Method to add a control to the list.

        :param control:
        :return:
        """
        if len(self.controls) == 0:
            # if there are no controls, we create the first.
            control.set_image(self.base_image)
            self.controls.append(control)
            logging.info("Added first control.")
        else:
            # set the current top image to be derived from the output of the control underneath it.
            control.set_image(self.controls[-1].apply_control())
            self.controls.append(control)
            logging.info("Added control.")

        # base case: the current top image is the top control's output
        self.current_image = self.controls[-1].apply_control()
        logging.info("Set current top image.")

    def set_base_image(self, image):
        """
        Method to set the base image.
        :param image:
        :return:
        """
        # set base image
        self.base_image = image

        # set images in the filters to be derived from the base images of previous layers
        if len(self.controls) > 0:
            # set first image to be the base image
            self.controls[0].set_image(self.base_image)

            # set the rest of the controls to use the output from precious controls
            for i in range(1, len(self.controls)):
                self.controls[i].set_image(self.controls[i-1].apply_control())

            logging.info("Base images set for filters.")

        self.current_image = self.get_current_image()
        logging.info("Images updated.")

    def get_current_image(self):
        """
        Method to get the image post filtering.
        :return:
        """
        if len(self.controls) > 1:
            return self.controls[-1].apply_control()
        else:
            return self.base_image
