import pyautogui
import cv2
import numpy as np

# resolution
resolution = (1920, 1080)

# video codec
codec = cv2.VideoWriter_fourcc(*"mp4v")

# output file name
filename = "Recording.mp4"

# frame rate
fps = 12.0

# creating a VideoWriter object
out = cv2.VideoWriter(filename, codec, fps, resolution)

# create empty window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

# Resize this window
cv2.resizeWindow("Live", 480, 270)

# start recording
while True:
    # take screenshot
    img = pyautogui.screenshot()

    # convert screenshot to numpy array
    frame = np.array(img)

    # Resize frame to 4K resolution if necessary
    frame = cv2.resize(frame, resolution)

    # Convert it from RGB to BGR
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # write to the output file
    out.write(frame)

    # display recording screen
    cv2.imshow('Live', frame)

    # stop recording when we press q
    if cv2.waitKey(1) == ord('q'):
        break

# release the video writer
out.release()

# Destroy all windows
cv2.destroyAllWindows()
