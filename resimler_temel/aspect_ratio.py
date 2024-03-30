import cv2

def resize_with_aspect_ratio(img, width=None ,height=None, inter= cv2.INTER_AREA):

    dimension = None
    (h,w)= img.shape[:2]

    if width is None and height is None:
        return img
    
    if width is None:
        r= height/float(h)
        dimension=(int(r*w),height)
    
    else :
        r=width/float(w)
        dimension=(width,int(r*h))
    
    return cv2.resize(img,dimension,interpolation=inter)

img=cv2.imread("klon.jpg")
img2=resize_with_aspect_ratio(img,width=None ,height=600, inter= cv2.INTER_AREA)

cv2.imshow("orginal",img)
cv2.imshow("resized",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

