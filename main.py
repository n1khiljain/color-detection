import cv2
from PIL import Image
from util import get_limits

cap = cv2.VideoCapture(0)

YELLOW = [0, 255, 255]
BLUE = [255, 0, 0]
RED = [0, 0, 255]
GREEN = [0, 255, 0]

def detect_color(color):
    lower_limit, upper_limit = get_limits(color=color)
    while True:
        ret, frame = cap.read()

        frame =cv2.flip(frame, 1) # flips frame horizontally

        hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsv_image, lower_limit, upper_limit) # generates a mask of all the pixels in the frame that are within the range of the color

        #drawing a bounding box around object
        mask_image = Image.fromarray(mask)

        bbox = mask_image.getbbox() # gets bounding box of object. bbox is a tuple of (left, top, right, bottom)

        if bbox is not None:
            x1, y1, x2, y2 = bbox

            cv2.rectangle(frame, (x1, y1), (x2, y2), color=color, thickness=5)

        cv2.imshow('frame', frame) # shows new window with frame
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()

    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_color(color=BLUE)
