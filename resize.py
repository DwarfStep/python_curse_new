import cv2 as cv

def resizing(img_res, new_wigth=None, new_height =None):
    h, w = img_res.shape[:2]

    if new_wigth is None and new_height is None:
        return img_res

    if new_wigth is None :
        ratio = new_wigth / h
        dimension = (int(w * ratio), new_height)

    else:
        ratio = new_wigth / w
        dimension = (new_wigth, int(h * ratio))

    return cv.resize(img_res, dimension)