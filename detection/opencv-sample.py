import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
mouth_cascade = cv2.CascadeClassifier('cascades/haarcascade_mcs_mouth.xml')
# mouth_cascade = cv2.CascadeClassifier('cascades/Mouth.xml')

# img = cv2.imread('snapshots/post-nauka.jpg')
# img = cv2.imread('snapshots/news1.jpg')
img = cv2.imread('snapshots/news2.jpg')
# img = cv2.imread('snapshots/news3.png')
# img = cv2.imread('snapshots/portret.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('img in gray', gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.05,
    minNeighbors=5
    # minSize=(30, 30),
    # flags=cv2.cv.CV_HAAR_SCALE_IMAGE
)
# print(faces)
# print(type(faces))

if isinstance(faces, tuple) or faces.shape[0] == 0:
    print('No faces found')
    exit(1)

if faces.shape[0] > 1:
    print('Too many faces!! Found {0} faces'.format(faces.shape[0]))
    exit(1)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    roi_gray_face = gray[y:y+h, x:x+w]
    # roi_color = img[y:y + h, x:x + w]
    mouths = mouth_cascade.detectMultiScale(
        roi_gray_face,
        scaleFactor=1.5,
        minNeighbors=10
    )

    cv2.imshow('face', roi_gray_face)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

# print("Found {0} mouths!".format(len(mouths)))

    print(mouths)
    # print(type(mouths))

    if isinstance(mouths, tuple) or mouths.shape[0] == 0:
        print('No mouths found')
        exit(1)

    if mouths.shape[0] > 1:
        print('Too many mouths!! Found {0} mouths'.format(mouths.shape[0]))
        exit(1)

    for (x_m, y_m, w_m, h_m) in mouths:
        cv2.rectangle(img, (x_m, y_m), (x_m + w_m, y_m + h_m), (255, 0, 0), 2)
        roi_gray_mouth = roi_gray_face[y_m:y_m+h_m, x_m:x_m+w_m]

        cv2.imwrite('out/img1.jpg', roi_gray_mouth)
        # roi_color = img[y:y + h, x:x + w]

        cv2.imshow('mouth', roi_gray_mouth)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# cv2.imshow('the whole image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

