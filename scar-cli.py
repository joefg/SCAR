"""
scar_cli.py

this contains a ui for the SCAR package.
written to demonstrate something.
"""

import cv2
import logging

import SCAR.Harness.harness as SCARHarness

# our example filters
import SCAR.face_detect as face
import SCAR.grey_filter as grey
import SCAR.canny as canny
import SCAR.otsu_filter as otsu
import SCAR.gauss_filter as gauss

# MAIN METHOD

if __name__ == '__main__':
    print("""
  /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$$
 /$$__  $$ /$$__  $$ /$$__  $$| $$__  $$
| $$  \__/| $$  \__/| $$  \ $$| $$  \ $$
|  $$$$$$ | $$      | $$$$$$$$| $$$$$$$/
 \____  $$| $$      | $$__  $$| $$__  $$
 /$$  \ $$| $$    $$| $$  | $$| $$  \ $$
|  $$$$$$/|  $$$$$$/| $$  | $$| $$  | $$
 \______/  \______/ |__/  |__/|__/  |__/

| STACKED | CONTROL | AUGMENTED | REALITY 
    """)

    # initialising the logger
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s [%(levelname)s] %(message)s')

    # initialising the webcam
    try:
        video_capture = cv2.VideoCapture(0)
        logging.info("Added webcam.")
    except cv2.error as ce:
        logging.error("Could not open webcam. Exiting.")
        exit(1)

    # creating our harness
    harness = SCARHarness.Harness()

    # setting our base image, at first, to be blank
    harness.set_base_image(
        video_capture.read()[1]
    )

    # creating the facejack filter and adding it to our harness
    #facefilter = face.FaceDetect()
    #harness.add_control(facefilter)

    # adding a grayscale filter
    grayfilter = grey.GrayFilter()
    harness.add_control(grayfilter)

    # adding a Canny edge detector filter
    cannyfilter = canny.CannyFilter()
    harness.add_control(cannyfilter)

    # adding a Otsu thresholding filter
    #otsufilter = otsu.OtsuFilter()
    #harness.add_control(otsufilter)

    # adding a gaussian blue filter
    #gaussfilter = gauss.GaussFilter()
    #harness.add_control(gaussfilter)

    # loop for getting the image from the webcam and displaying it
    logging.info("Activating main loop-- 'q' to exit loop.")
    frame_count = 0

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # set the current frame to be the frame in the harness
        harness.set_base_image(frame)

        # Display the resulting frame
        cv2.imshow('SCAR Output', harness.get_current_image())

        frame_count += 1

        logging.info("Frame count: {0}".format(
            frame_count
        ))

        # loop breakpoint
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    video_capture.release()
    logging.info("Capture released.")

    # Destroy windows.
    cv2.destroyAllWindows()
    logging.info("Windows destroyed.")
