# OPEN SOURCED BY JASON ORLOSKY, CONTRIBUTION BY CHIN CANTILLO https://github.com/chindynamics


#Import dependencies

import cv2
import numpy as np
import random
import math
import pyautogui
import time

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False

camera_w = 640 #Modify to change camera width
camera_h = 480 #Modify to change camera height

#Smoothing filter state
_smoothed_center_persistent = None
lost_tracking_counter = 0

calibration_points = [] #Points of calibration

#Get screen resolution size
SCREEN_W, SCREEN_H = pyautogui.size()

def smooth_center(current_center, alpha_percent=80): #This function smooths the pupil center, for better cursor movement
    global _smoothed_center_persistent, lost_tracking_counter
    alpha = max(0.01, alpha_percent / 100.0)
    if current_center:
        lost_tracking_counter = 0
        if _smoothed_center_persistent:
            smoothed_x = int(alpha * current_center[0] + (1 - alpha) * _smoothed_center_persistent[0])
            smoothed_y = int(alpha * current_center[1] + (1 - alpha) * _smoothed_center_persistent[1])
            smoothed_center = (smoothed_x, smoothed_y)
        else:
            smoothed_center = current_center
        _smoothed_center_persistent = smoothed_center
    else:
        #lost tracking
        lost_tracking_counter += 1
        smoothed_center = _smoothed_center_persistent
    return smoothed_center

def train_mapping(calibration_points): #Mapping from camera to cursor
    #Matrixes for least squares
    P = [] 
    Sx = []
    Sy = []
    for (px, py), (sx, sy) in calibration_points:
        P.append([px, py, px*py, px*px, py*py, 1]) #Terminos cuadrados
        Sx.append(sx)
        Sy.append(sy)
    P = np.array(P, dtype=np.float32)
    Sx = np.array(Sx, dtype=np.float32)
    Sy = np.array(Sy, dtype=np.float32)
    #Solve for P * a = Sx, P * b = Sy
    a_coeffs, _, _, _ = np.linalg.lstsq(P, Sx, rcond=None)
    b_coeffs, _, _, _ = np.linalg.lstsq(P, Sy, rcond=None)
    return a_coeffs, b_coeffs


def calibrate(camera_index=1, alpha_percent=50):  #Calibration routine, 4x4 grid
    global calibration_points
    pasos = 6 #Dividir en pasos + 1 (puntos)
    grid = [(i / pasos, j / pasos) for j in range(pasos+1) for i in range(pasos+1)]

    #Windows prep
    cv2.namedWindow('Calibration', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Calibration', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.namedWindow('Calibration Camera', cv2.WINDOW_NORMAL)

    cap = cv2.VideoCapture(camera_index)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, camera_w)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, camera_h)
    if not cap.isOpened():
        print("Error: No se pudo abrir la cámara para calibración.")
        return []

    for pct_x, pct_y in grid:
        #Draw points
        marker = np.zeros((SCREEN_H, SCREEN_W, 3), dtype=np.uint8)
        cx, cy = int(pct_x*SCREEN_W), int(pct_y*SCREEN_H)
        cv2.circle(marker, (cx, cy), 20, (255,255,255), -1)
        cv2.imshow('Calibration', marker)

        #Show camera while waiting for key
        while True:
            ret, frame = cap.read()
            if not ret:
                continue
            rotated_rect = process_frame(frame)
            current_center = None
            if rotated_rect and isinstance(rotated_rect, tuple):
                current_center = tuple(map(int, rotated_rect[0]))
                sm_center = smooth_center(current_center, alpha_percent)
                cv2.circle(frame, sm_center, 5, (0,0,255), -1)

            cv2.imshow('Calibration Camera', frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord(' '):  #Press space key for capture
                samples = []
                #Take 5 samples and get average
                for _ in range(5):
                    ret, f2 = cap.read()
                    if not ret:
                        continue
                    rr = process_frame(f2)
                    if rr and isinstance(rr, tuple):
                        cc = tuple(map(int, rr[0]))
                        sm = smooth_center(cc, alpha_percent)
                        samples.append(sm)
                    #Wait 
                    cv2.waitKey(50)

                if samples:
                    avg_x = int(sum(p[0] for p in samples) / len(samples))
                    avg_y = int(sum(p[1] for p in samples) / len(samples))
                    calibration_points.append(((avg_x, avg_y), (cx, cy)))
                break
            elif key == ord('q'):
                cap.release()
                cv2.destroyAllWindows()
                return calibration_points

    cap.release()
    cv2.destroyAllWindows()
    return calibration_points

#Crop the image to maintain a specific aspect ratio (width:height) before resizing.
def crop_to_aspect_ratio(image, width=640, height=480):
    current_height, current_width = image.shape[:2]
    desired_ratio = width / height
    current_ratio = current_width / current_height

    if current_ratio > desired_ratio:
        new_width = int(desired_ratio * current_height)
        offset = (current_width - new_width) // 2
        cropped_img = image[:, offset:offset+new_width]
    else:
        new_height = int(current_width / desired_ratio)
        offset = (current_height - new_height) // 2
        cropped_img = image[offset:offset+new_height, :]

    return cv2.resize(cropped_img, (width, height))

#Apply thresholding to an image
def apply_binary_threshold(image, darkestPixelValue, addedThreshold):
    threshold = darkestPixelValue + addedThreshold
    _, thresholded_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY_INV)
    return thresholded_image

# Finds a square area of dark pixels in the image
# @param image: BGR image
# @return a point within the pupil region
def get_darkest_area(image):
    ignoreBounds = 120 #It depends on resolution
    imageSkipSize = 20 #It depends on resolution
    searchArea = 10 #It depends on resolution
    internalSkipSize = 10

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    min_sum = float('inf')
    darkest_point = None

    for y in range(ignoreBounds, gray.shape[0] - ignoreBounds, imageSkipSize):
        for x in range(ignoreBounds, gray.shape[1] - ignoreBounds, imageSkipSize):
            current_sum = 0
            num_pixels = 0
            for dy in range(0, searchArea, internalSkipSize):
                if y + dy >= gray.shape[0]:
                    break
                for dx in range(0, searchArea, internalSkipSize):
                    if x + dx >= gray.shape[1]:
                        break
                    current_sum += gray[y + dy][x + dx]
                    num_pixels += 1

            if current_sum < min_sum and num_pixels > 0:
                min_sum = current_sum
                darkest_point = (x + searchArea // 2, y + searchArea // 2)

    return darkest_point

#Mask all pixels outside a square defined by center and size
def mask_outside_square(image, center, size):
    x, y = center
    half_size = size // 2

    mask = np.zeros_like(image)
    top_left_x = max(0, x - half_size)
    top_left_y = max(0, y - half_size)
    bottom_right_x = min(image.shape[1], x + half_size)
    bottom_right_y = min(image.shape[0], y + half_size)
    mask[top_left_y:bottom_right_y, top_left_x:bottom_right_x] = 255
    return cv2.bitwise_and(image, mask)


# Returns the largest contour that is not extremely long or tall
def filter_contours_by_area_and_return_largest(contours, pixel_thresh, ratio_thresh):
    max_area = 0
    largest_contour = None

    for contour in contours:
        area = cv2.contourArea(contour)
        if area >= pixel_thresh:
            x, y, w, h = cv2.boundingRect(contour)
            length_to_width_ratio = max(w / h, h / w)
            if length_to_width_ratio <= ratio_thresh:
                if area > max_area:
                    max_area = area
                    largest_contour = contour

    return [largest_contour] if largest_contour is not None else []

def process_frames(thresholded_image_medium, frame, gray_frame, darkest_point, debug_mode_on, render_cv_window):
    kernel_size = 5
    kernel = np.ones((kernel_size, kernel_size), np.uint8)

    dilated_image = cv2.dilate(thresholded_image_medium, kernel, iterations=2)
    contours, _ = cv2.findContours(dilated_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    reduced_contours = filter_contours_by_area_and_return_largest(contours, 1000, 3)

    final_rotated_rect = ((0, 0), (0, 0), 0)
    if len(reduced_contours) > 0 and len(reduced_contours[0]) > 5:
        ellipse = cv2.fitEllipse(reduced_contours[0])
        cv2.ellipse(frame, ellipse, (0, 255, 0), 2)
        center_x, center_y = map(int, ellipse[0])
        cv2.circle(frame, (center_x, center_y), 3, (255, 255, 0), -1)
        final_rotated_rect = ellipse

    # Calculate FPS
    current_time = time.time()
    fps = int(1 / (current_time - process_frames.last_time)) if hasattr(process_frames, "last_time") else 0
    process_frames.last_time = current_time

    # Display FPS on the frame
    cv2.putText(frame, f"FPS: {fps}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    frame = cv2.resize(frame, (320, 240))
    cv2.imshow("Frame with Ellipse", frame)

    if render_cv_window:
        cv2.imshow("Best Thresholded Image Contours on Frame", frame)

    return final_rotated_rect

# Process a single frame for pupil detection
def process_frame(frame):
    start_time = time.time()
    
    frame = crop_to_aspect_ratio(frame)
    #print(f"Time after crop_to_aspect_ratio: {time.time() - start_time:.6f} seconds")
    
    darkest_point = get_darkest_area(frame)
    #print(f"Time after get_darkest_area: {time.time() - start_time:.6f} seconds")
    
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #print(f"Time after cvtColor to gray: {time.time() - start_time:.6f} seconds")
    
    darkest_pixel_value = gray_frame[darkest_point[1], darkest_point[0]]
    thresholded_image_medium = apply_binary_threshold(gray_frame, darkest_pixel_value, 15)
    #print(f"Time after apply_binary_threshold: {time.time() - start_time:.6f} seconds")
    
    thresholded_image_medium = mask_outside_square(thresholded_image_medium, darkest_point, 250)
    #print(f"Time after mask_outside_square: {time.time() - start_time:.6f} seconds")
    
    result = process_frames(thresholded_image_medium, frame, gray_frame, darkest_point, False, False)
    #print(f"Time after process_frames: {time.time() - start_time:.6f} seconds")
    
    return result

#Real-time eye tracking from webcam only
def process_video(input_method=2, camera_index=1, alpha_percent=50, a_coeffs=None, b_coeffs=None, stop_flag=None, show_window=False):


    if a_coeffs is None or b_coeffs is None:
        raise ValueError("process_video requiere a_coeffs y b_coeffs ya calculados")

    #Only real time camera
    if input_method != 2:
        print("Solo se soporta entrada en tiempo real (input_method=2)")
        return
    
    cap = cv2.VideoCapture(camera_index)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, camera_w)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, camera_h)
    if not cap.isOpened():
        print("Error: No se pudo abrir la cámara.")
        return

    dead_zone = 10 #Dead zone
    prev_x, prev_y = SCREEN_W//2, SCREEN_H//2 
    debug_mode_on = False

    try:
        while True:
            # Si nos han pedido parar, rompemos
            if stop_flag is not None and stop_flag():
                break

            ret, frame = cap.read()
            if not ret:
                print("Error al leer frame de la cámara.")
                break

            #Pupil detection
            rotated_rect = process_frame(frame)
            current_center = None
            if rotated_rect and isinstance(rotated_rect, tuple):
                current_center = tuple(map(int, rotated_rect[0]))

            #Apply smoothing
            smoothed_center = smooth_center(current_center, alpha_percent)

            #Apply mapping
            if smoothed_center:
                px, py = smoothed_center
                v = np.array([px, py, px*py, px*px, py*py, 1], dtype=np.float32)
                screen_x = int(np.dot(a_coeffs, v))
                screen_y = int(np.dot(b_coeffs, v))

                # LIMITAR Y PROTEGER moveTo
                try:
                    screen_x = max(0, min(screen_x, SCREEN_W - 1))
                    screen_y = max(0, min(screen_y, SCREEN_H - 1))


                    if abs(screen_x - prev_x) > dead_zone or abs(screen_y - prev_y) > dead_zone:
                        pyautogui.moveTo(screen_x, screen_y)
                        prev_x, prev_y = screen_x, screen_y
                except Exception as e_move:
                    print(f"[process_video] moveTo fallo, coordenadas ({screen_x},{screen_y}): {e_move}")

                cv2.circle(frame, smoothed_center, 5, (0, 0, 255), -1)  #Debug

            if show_window:
                cv2.imshow('Eyetracker -Real Time', frame)
                key = cv2.waitKey(1) & 0xFF
                if key == ord('d'):
                    debug_mode_on = not debug_mode_on
                    if not debug_mode_on:
                        cv2.destroyAllWindows()
                elif key == ord('q'):
                    break
            time.sleep(0.005)

    except Exception as e:
        print(f"[process_video] excepción interna: {e}")
        import traceback; traceback.print_exc()
    finally:
        cap.release()
        if show_window:  
            cv2.destroyAllWindows()
    

if __name__ == "__main__":
    #Execute code
    print("Iniciando calibración 5x5...")
    puntos = calibrate(camera_index=0, alpha_percent=30)
    cv2.destroyAllWindows()

    if len(puntos) < 3:
        # Si no se consigue calibrar correctamente, usar mapeo identidad
        a_coeffs = np.array([1, 0, 0, 0, 0, 0], dtype=np.float32)
        b_coeffs = np.array([0, 0, 1, 0, 0, 0], dtype=np.float32)
    else:
        a_coeffs, b_coeffs = train_mapping(puntos)

    print("Calibración completada. Iniciando eyetracker...")
    process_video(input_method=2, 
                  a_coeffs=a_coeffs, 
                  b_coeffs=b_coeffs, 
                  camera_index=2, 
                  alpha_percent=30)
