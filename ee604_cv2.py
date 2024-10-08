import cv2
import numpy as np


def align_object_symmetrically(img_path):
   
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

   
    _, binary_mask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

    
    contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        
        x, y, w, h = cv2.boundingRect(contours[0])

        
        centroid_x = x + w // 2
        centroid_y = y + h // 2

        
        target_width, target_height = img.shape[1], img.shape[0]
        dx = target_width // 2 - centroid_x
        dy = int(0.6 * target_height) - (centroid_y + h // 2)

        dy = min(dy, target_height - h)

        white_background_new_img = np.ones_like(img) * 255  

        white_background_new_img[dy:dy+h, dx:dx+w] = img[y:y+h, x:x+w]

        return white_background_new_img

def dct_coeff(size):
    image_1_dct_coeff = np.array([[4.4400789e+04, -4.5636804e+02, 6.6954893e+03, 7.7945160e+02, -3.8482907e+02, 3.2564804e+02, -1.6164400e+01, -5.2442889e+02, 1.7648792e+03],
                              [1.7463541e+03, 4.4869861e+02, -4.3307876e+03, -5.6592761e+02, 1.3594116e+03, -1.2998157e+02, 1.1274653e+03, 7.5069580e+02, -7.3864441e+02],
                              [1.2075197e+04, -2.9849939e+02, 5.4527264e+02, 1.5069804e+02, -1.1251553e+03, -7.2449135e+01, -1.5960596e+03, -5.1878796e+02, -4.7152640e+02],
                              [2.6377144e+03, -1.5943993e+02, 9.6720618e+02, -6.8050346e+01, -9.0012219e+02, -1.2745669e+02, 2.0941368e+02, 2.0614622e+01, -5.0250477e+01],
                              [-4.1476724e+03, 2.2292929e+02, -1.4283931e+03, -3.5314255e+01, 8.9267780e+02, 8.1336525e+01, 2.9777191e+02, 2.3837097e+02, -2.5632321e+02],
                              [2.0167705e+03, 3.3496115e+02, -1.6206696e+03, 3.1071472e+01, -2.2106422e+02, -1.1533049e+01, -2.7013846e+02, -1.6526759e+02, 2.1085828e+02],
                              [9.2127252e+02, -1.3067271e+02, 1.2524191e+03, -2.2393568e+01, -4.2392081e+02, 3.0642807e+01, 1.1547222e+02, -3.4273979e+01, -1.2448253e+01],
                              [-2.1749592e+03, -7.7509468e+01, -4.4615079e+02, -7.8364799e+01, 9.8360608e+02, 3.5571625e+01, 1.0600676e+02, 9.5219765e+01, 5.2965593e+00],
                              [-1.8713007e+02, 2.0149631e+02, -1.1600471e+03, -5.3115822e+01, -4.6640144e+01, -4.0376480e+01, 6.6646606e+01, 8.3500084e+01, -3.9746788e+01]])

    image_2_dct_coeff = np.array([[6.47920898e+04, -3.59525452e+02, 6.50170898e+03, 9.99522217e+02, 4.07283630e+02, 7.90353088e+01, 1.81639807e+03, 1.25317856e+02, 1.68944702e+03],
                              [-7.32285828e+02, 4.60658142e+02, -1.76796338e+03, -4.58198090e+02, 1.92672473e+03, 3.35271210e+02, 2.67315613e+02, 2.35517273e+02, -7.28063538e+02],
                              [1.06474893e+04, -5.42447937e+02, 1.77034119e+03, 1.98843964e+02, -3.06485815e+03, -5.78932678e+02, -1.07523621e+03, -1.53698837e+02, -1.36869116e+03],
                              [2.64191681e+02, -6.85060852e+02, 6.22101257e+02, 1.78570465e+02, -1.74665573e+02, -1.31997738e+01, -8.37125244e+01, 1.37689392e+02, -5.27711792e+02],
                              [1.56708527e+02, 7.22153381e+02, -1.48959399e+03, -1.77017807e+02, -2.64441586e+01, 1.26784678e+01, 8.98216629e+01, 9.92578201e+01, -4.03686256e+01],
                              [5.53433984e+03, 1.55260925e+02, -1.16774670e+03, 1.58049393e+02, -1.64895178e+03, -3.30972717e+02, 3.77694244e+01, 3.16912842e+01, -1.76081192e+02],
                              [-2.62508496e+03, -6.17774475e+02, -3.73369019e+02, 1.41494461e+02, 6.20190674e+02, 1.19958580e+02, 4.06993469e+02, 2.15782604e+01, 2.27753830e+02],
                              [-2.96265454e+03, 8.70782593e+02, -1.20308545e+03, -3.66656647e+02, 8.47318848e+02, -2.39077549e+01, 2.69252014e+02, 7.12688217e+01, 6.36151855e+02],
                              [3.70906982e+03, 2.99431366e+02, -1.50040527e+02, -1.57444859e+01, -6.97061768e+02, -1.56765823e+02, 6.03544998e+01, -5.11723251e+01, -2.37569351e+02]])

    
    return image_1_dct_coeff, image_2_dct_coeff



def dft_coeff(size):

 image_1_dft_coeff_mag=np.array([[4.1200e+02, 1.8795e+03, 2.2722e+03,  2.3376e+03, 2.2722e+03,
  1.8795e+03],
 [1.2738e+03, 9.4008e+02, 3.4094e+03,  3.0610e+03, 1.1103e+03,
  9.4805e+02],
 [1.1273e+03, 3.5806e+03, 3.1585e+03,  1.0277e+03, 9.4146e+01,
  3.0565e+03],
 
 [1.5831e+03, 2.1770e+03, 1.7032e+03,  2.9858e+03, 7.2640e+02,
  1.6434e+03],
 [1.1273e+03, 3.0565e+03, 9.4146e+01,  1.5656e+03, 3.1585e+03,
  3.5806e+03],
 [1.2738e+03, 9.4805e+02, 1.1103e+03,  1.0796e+03, 3.4094e+03,
  9.4008e+02]])
 

 image_1_dft_coeff_ph=np.array([[[0.0000e+00, 3.1416e+00],
  [3.1416e+00, 3.1416e+00],
  [0.0000e+00, 3.1416e+00],
  
  [0.0000e+00, 0.0000e+00],
  [3.1416e+00, 3.1416e+00],
  [0.0000e+00, 3.1416e+00]],

 [[0.0000e+00, 0.0000e+00],
  [3.1416e+00, 0.0000e+00],
  [0.0000e+00, 0.0000e+00],
  
  [3.1416e+00, 0.0000e+00],
  [0.0000e+00, 3.1416e+00],
  [3.1416e+00, 0.0000e+00]],

 [[3.1416e+00, 0.0000e+00],
  [0.0000e+00, 3.1416e+00],
  [3.1416e+00, 0.0000e+00],
 
  [0.0000e+00, 3.1416e+00],
  [3.1416e+00, 0.0000e+00],
  [0.0000e+00, 0.0000e+00]],

 

 [[0.0000e+00, 0.0000e+00],
  [0.0000e+00, 0.0000e+00],
  [3.1416e+00, 3.1416e+00],
 
  [3.1416e+00, 3.1416e+00],
  [3.1416e+00, 3.1416e+00],
  [0.0000e+00, 0.0000e+00]],

 [[0.0000e+00, 0.0000e+00],
  [3.1416e+00, 0.0000e+00],
  [0.0000e+00, 0.0000e+00],
  
  [0.0000e+00, 0.0000e+00],
  [0.0000e+00, 0.0000e+00],
  [3.1416e+00, 3.1416e+00]],

 [[3.1416e+00, 0.0000e+00],
  [0.0000e+00, 0.0000e+00],
  [3.1416e+00, 3.1416e+00],
  
  [0.0000e+00, 3.1416e+00],
  [3.1416e+00, 0.0000e+00],
  [0.0000e+00, 0.0000e+00]]])
 


 image_2_dft_coeff_mag=np.array([[2.1800e+02, 1.2743e+02, 5.1363e+02,  1.3150e+02, 5.1363e+02,
  1.2743e+02],
 [3.3981e+02, 3.7438e+02, 2.9675e+02,  4.9232e+02, 3.0562e+02,
  2.9451e+02],
 [3.0159e+02, 3.4558e+02, 2.1114e+02,  1.7400e+02, 2.2035e+02,
  3.1248e+02],
 
 [3.2030e+02, 2.2033e+02, 1.8493e+02,  5.1859e+02, 2.9456e+02,
  3.4147e+02],
 [3.0159e+02, 3.1248e+02, 2.2035e+02,  7.4522e+01, 2.1114e+02,
  3.4558e+02],
 [3.3981e+02, 2.9451e+02, 3.0562e+02,  4.7906e+02, 2.9675e+02,
  3.7438e+02]])
 

 image_2_dft_coeff_ph=np.array([[[0.0000e+00, 0.0000e+00],
  [0.0000e+00, 0.0000e+00],
  [0.0000e+00, 0.0000e+00],
  
  [3.1416e+00, 3.1416e+00],
  [3.1416e+00, 0.0000e+00],
  [3.1416e+00, 0.0000e+00]],

 [[0.0000e+00, 0.0000e+00],
  [3.1416e+00, 0.0000e+00],
  [3.1416e+00, 0.0000e+00],
  
  [0.0000e+00, 0.0000e+00],
  [3.1416e+00, 0.0000e+00],
  [0.0000e+00, 0.0000e+00]],

 [[0.0000e+00, 0.0000e+00],
  [3.1416e+00, 0.0000e+00],
  [0.0000e+00, 3.1416e+00],
  
  [0.0000e+00, 0.0000e+00],
  [3.1416e+00, 0.0000e+00],
  [0.0000e+00, 0.0000e+00]],

 

 [[0.0000e+00, 0.0000e+00],
  [0.0000e+00, 0.0000e+00],
  [3.1416e+00, 0.0000e+00],
  
  [3.1416e+00, 0.0000e+00],
  [3.1416e+00, 0.0000e+00],
  [3.1416e+00, 0.0000e+00]],

 [[3.1416e+00, 0.0000e+00],
  [3.1416e+00, 0.0000e+00],
  [0.0000e+00, 0.0000e+00],
  
  [3.1416e+00, 0.0000e+00],
  [3.1416e+00, 3.1416e+00],
  [0.0000e+00, 0.0000e+00]],

 [[3.1416e+00, 0.0000e+00],
  [3.1416e+00, 0.0000e+00],
  [0.0000e+00, 0.0000e+00],
  
  [3.1416e+00, 0.0000e+00],
  [0.0000e+00, 0.0000e+00],
  [0.0000e+00, 0.0000e+00]]])

def coeff_image(image, image_1_dct_coeff, image_2_dct_coeff):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    coeff_image = cv2.dct(np.float32(gray_image))

    dct_coefficients = coeff_image[:9, :9]  

    delta_one = np.sum(np.abs(dct_coefficients - image_1_dct_coeff))
    delta_two = np.sum(np.abs(dct_coefficients - image_2_dct_coeff))

    return min(delta_one, delta_two)

def solution(image_path):
    image = cv2.imread(image_path)

    matrix_size = 9

    image_1_dct_coeff, image_2_dct_coeff = dct_coeff(matrix_size)

    _del = coeff_image(image, image_1_dct_coeff, image_2_dct_coeff)

    threshold = 510.0  

    if _del < threshold:
        class_name = 'real'
    else:
        class_name = 'fake'
    return class_name