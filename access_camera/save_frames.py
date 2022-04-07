import cv2, os, time

out_dir="./frames"
show_image=False
save_frames=True
capture_dalay=0.5
frame_count=0

# Create folder to save frames
if not os.path.exists(path=out_dir):
    os.mkdir(path=out_dir)

for f in os.listdir(out_dir):
    os.remove(os.path.join(out_dir, f))

# Open camera (on linux /dev/video0)
cap = cv2.VideoCapture(0)

# Check if camera is already in use
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # we just want to save a few frames, not all of them
    time.sleep(capture_dalay)

    # Just to keep track how many frames are already processed
    frame_count+=1

    # Get actual data from the camera sensor
    ret, frame = cap.read()
    # Just in case you want to use the image in grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Something went wrong :c
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Save the frame in the given location 
    if save_frames:
        cv2.imwrite(os.path.join(out_dir, str(frame_count) + ".png"), frame)

    # Show image in Window, if enabled
    if show_image:
        # I just wanted some text on it, okay?!
        font = cv2.FONT_HERSHEY_SIMPLEX
        text_size = cv2.getTextSize("Frame: " + str(frame_count), font, 0.5, 1)
        cv2.putText(frame, "Frame: " + str(frame_count), (10, 20), font, 0.5, (0, 255, 0), 1)
        # Show image
        cv2.imshow('frame', frame)

    # Break if the "q" key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Just say that youdon't want to use the camera anymore
cap.release()
cv2.destroyAllWindows()