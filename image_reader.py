import cv2

if __name__ == '__main__':
    camera_ind = 0
    cam = cv2.VideoCapture(camera_ind)
    ret, frame = cam.read()
    if not ret:
        print("Failed to read from camera")
    else:
        filename = "Test.jpg"
        cv2.imwrite(filename, frame) 

