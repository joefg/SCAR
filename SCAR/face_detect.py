"""
face_detect.py

implementation of a control in a SCAR harness- aimed at detecting faces.

"""

import cv2
import logging

import SCAR.Controls.control as control

class FaceDetect(control.Control):
    """
    FaceDetect

    Supposed to detect a face and draw a box around it.
    """

    def apply_control(self):

        # set our face cascade
        face_cascade = cv2.CascadeClassifier('SCAR/haarcascade_frontalface_default.xml')

        # get locations of faces
        faces = face_cascade.detectMultiScale(
            cv2.cvtColor(self.base_image, cv2.COLOR_BGR2GRAY),
            scaleFactor = 1.1,
            minNeighbors = 5,
            minSize = (30, 30),
        )

        self.image_out = self.base_image

        # draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(self.image_out, (x, y), (x + w, y + h), (0, 0, 255), 2)

        logging.info("FaceDetect: {0} faces detected.".format(
            len(faces)
        ))

        return self.image_out
