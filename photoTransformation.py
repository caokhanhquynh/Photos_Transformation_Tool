import cv2
import random

def getRedComponent(img):
    if len(img[0][0]) != 3:
        print("Attempting to return the red component from a non RGB image")
        print("Returning an empty matrix")
        return []
    else:
        imageHeight = len(img)
        imageWidth = len(img[0])
        R = [] #Red component matrix
        for i in range(imageHeight):
            row = []
            for j in range (imageWidth):
                pixel = img[i][j]
                row.append(pixel[0])
            R.append(row)
        return R

def getGreenComponent(img):
    if len(img[0][0]) != 3:
        print("Attempting to return the green component from a non RGB image")
        print("Returning an empty matrix")
        return []
    else:
        imageHeight = len(img)
        imageWidth = len(img[0])
        G = [] #Green component matrix
        for i in range(imageHeight):
            row = []
            for j in range (imageWidth):
                pixel = img[i][j]
                row.append(pixel[1])
            G.append(row)
        return G

def getBlueComponent(img):
    if len(img[0][0]) != 3:
        print("Attempting to return the blue component from a non RGB image")
        print("Returning an empty matrix")
        return []
    else:
        imageHeight = len(img)
        imageWidth = len(img[0])
        B = [] #Blue component matrix
        for i in range(imageHeight):
            row = []
            for j in range (imageWidth):
                pixel = img[i][j]
                row.append(pixel[2])
            B.append(row)
    return B

def updateImage(img, R, G, B):
    for i in range(len(img)):
        for j in range(len(img[0])):
            pixel = [R[i][j], G[i][j], B[i][j]]
            img[i][j] = pixel  

#invert image
def invertMatrixUpsideDown(M):
    L = []
    for i in range (len(M)-1, -1, -1):
        L.append (M[i])
    return L

def invertImageUpsideDown(myImage):
    R = getRedComponent(myImage)
    G = getGreenComponent(myImage)
    B = getBlueComponent(myImage)
    R = invertMatrixUpsideDown(R)
    G = invertMatrixUpsideDown(G)
    B = invertMatrixUpsideDown(B)
    updateImage(myImage, R, G, B)
    #Display the inverted image
    cv2.imshow("Inverted Image", myImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #Save the inverted image in the computer hard drive
    cv2.imwrite("pic_inverted.jpg", myImage)

#reduce quality  
def reduceQuality(img):
    w = len(img[0]) // 10
    h = len(img) // 10
    N = [[0 for x in range(w)] for y in range(h)]
    
    for i in range(h):
        for j in range(w):
            N[i][j] = img[i * 10][j * 10]
    return N

def reduceImageQuality(myImage):
    R = getRedComponent(myImage)
    G = getGreenComponent(myImage)
    B = getBlueComponent(myImage)
    R = reduceQuality(R)
    G = reduceQuality(G)
    B = reduceQuality(B)
    
    for i in range(len(myImage) - 9):
        for j in range(len(myImage[0]) - 9):
            pixel = [B[i//10][j//10], G[i//10][j//10], R[i//10][j//10]]
            myImage[i][j] = pixel
    
    cv2.imshow("Quality Reduced Image", myImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    cv2.imwrite("picQualityReduced.jpg", myImage)
    
def distortRBG(img):
    N = [[0 for x in range(len(img[0]))] for y in range(len(img))]
    for i in range(len(img)):
        distort_num = random.randint(-5,5)
        for j in range(len(img[0])):
            if (i + distort_num > len(img) or i + distort_num < len(img) or j + distort_num > len(img[0]) or j + distort_num < len(img[0])):
                distort_num = 0
            N[i][j] = img[i + distort_num][j + distort_num]
    return N

def distortImage(myImage):
    R = getRedComponent(myImage)
    G = getGreenComponent(myImage)
    B = getBlueComponent(myImage)
    R = distortRBG(R)
    G = distortRBG(G)
    B = distortRBG(B)
    
    for i in range(len(myImage)):
        for j in range(len(myImage[0])):
            pixel = [B[i][j], G[i][j], R[i][j]]
            myImage[i][j] = pixel
    
    cv2.imshow("Distort Image", myImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    cv2.imwrite("picDistorted.jpg", myImage)

#Main Program
#Read image
myImage = cv2.imread("cat.jpg")

#Display image
cv2.imshow("Original Image", myImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Invert image upside down
# invertImageUpsideDown(myImage)

# #Reduce image's quality
# reduceImageQuality(myImage)

#Distort image
distortImage(myImage)