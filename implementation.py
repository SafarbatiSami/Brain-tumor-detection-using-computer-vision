#############################################- Image Processing software v1.0 -#########################################################################
# THIS SOFTWARE WAS MADE BY TWO IMPLIED 'SIGNAL AND IMAGE PROCESSING' STUDENTS OF UNIVERSITY OF CLERMONT AUVERGNE, SAMI SAFARBATI AND ILHAME BELARREM .#
#                                                                                                                                                      #
#                                                                                                                                                      #
#                                                                                                                                                      #
#                                                                                                                                                      #
#   PLEASE READ THE DESCRIPTION BEFORE USING THIS !!!! (JOKING THERE IS NO GUIDE, YOU'RE ON YOUR OWN)                                                  #
#   CONTACTS: SAMI SAFARBATI (samsafarbati@hotmail.com)                                                                                                #
#             ILHAME BELARREM (ilhame.BELARREM@etu.uca.fr)                                                                                             #
########################################################################################################################################################


import cv2
import numpy as np
def imageProcessing(x):
    #I= cv2.imread('radiologie-hirntumor-vor-nach-op.jpg')
    I= cv2.imread(x)
    #cv2.waitKey(0)

    #print('shape of  ',I.shape)
    scale_percent = 200 # pourcentage taille de l'image original
    width = int(I.shape[1] * scale_percent / 100)
    height = int(I.shape[0] * scale_percent / 100)
    dim = (width, height)
    
    # resize image ---------------------------------------------------------------------------------
    IR = cv2.resize(I, dim, interpolation = cv2.INTER_AREA)
    #cv2.imshow("Resized image",IR)
    #cv2.waitKey(0)

    #reduction de bruit
    IR=cv2.medianBlur(src=I, ksize= 9)

    # binarized image -------------------------------------------------------------------------------------
    th, I_th = cv2.threshold(IR, 156 , 255 , cv2.THRESH_BINARY)
    # 'for second brain tumour image '   th, I_th = cv2.threshold(IR, 136 , 255 , cv2.THRESH_BINARY)
    print('value of th is  : ',th)
    #cv2.imshow('image binarized',I_th)

    #edged image-------------------------------------------------------------------------------
    edged = cv2.Canny(I_th , 30 , 200)
    #finding contours--------------------------------------------------------------
    contours, hierarchy = cv2.findContours(edged, 
        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.imshow('Canny Edges After Contouring', edged)
    #cv2.waitKey(0)

    print("Number of Contours found = " + str(len(contours)))
    #drawing contours --------------------------------------------------------------------
    cv2.drawContours(IR, contours ,-1, (0, 255, 0), 2)

    kernel3 = np.array([[0, -1,  0],
                    [-1,  5, -1],
                        [0, -1,  0]])
    sharp_img = cv2.filter2D(src=IR, ddepth=-1, kernel=kernel3)

    #cv2.imshow('final image with Contours', IR)
    #cv2.waitKey(0)
    #  choisir une des deux images sharp_img ou IR-----------------------------------

    #cv2.imshow('final image with Contours 2', sharp_img)
    #cv2.waitKey(0)
    return IR



