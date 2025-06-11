#!/usr/bin/env python3

#---------------------------------------------------IMPORTAR LIBRERÍAS-------------------------------------------------------

import sys
import os
import time
import serial # Importar
from PySide6 import *
from PySide6.QtCore import QPropertyAnimation, QThread, Signal, Slot, QTimer, QEvent  # Importa directamente la clase
import cv2
import numpy as np
import pyautogui

#---------------------------------------------------IMPORTAR EYETRACKING----------------------------------------------------------

from deltatrackersmall import calibrate, train_mapping, process_frame, camera_w, camera_h, SCREEN_W, SCREEN_H, smooth_center, process_video

#---------------------------------------------------IMPORTAR ARCHIVO GUI-------------------------------------------------------


from ui_delta import *


#---------------------------------------------------CREAR CLASE PARA EYETRACKING---------------------------------------------------------


class EyeTrackerThread(QThread):
    def __init__(self, a_coeffs, b_coeffs, camera_index=1, alpha_percent=80, parent=None):
        super().__init__(parent)
        self.a = a_coeffs
        self.b = b_coeffs
        self.camera_index = camera_index
        self.alpha = alpha_percent
        self.stop_flag = False

    def run(self):
        try:
            #VERIFICAR SI LA CAMARA ESTA FUNCIONANDO
            cap = cv2.VideoCapture(self.camera_index)
            if not cap.isOpened():
                print(f"[ERROR] No se pudo abrir la cámara {self.camera_index}")
                return
            cap.release()

            print("[EyeTrackerThread] Llamando a process_video...")
            process_video(
                input_method=2,
                camera_index=self.camera_index,
                alpha_percent=self.alpha,
                a_coeffs=self.a,
                b_coeffs=self.b,
                stop_flag=lambda: self.stop_flag,
                show_window=False
            )
        except Exception as e:
            # Capturamos cualquier error e imprimimos para que no cierre todo
            print(f"[EyeTrackerThread] Excepción en process_video: {e}")
            import traceback
            traceback.print_exc()

    def stop(self):
        self.stop_flag = True
        # cv2.destroyAllWindows()  # cierra cualquiera de las ventanas OpenCV
        # self.quit()
        self.wait()

#---------------------------------------------------CREAR CLASE PARA LA CÁMARA-------------------------------------------------------

class CameraThread(QThread):

    frame_ready = Signal(QtGui.QImage) #Señal para enviar el frame procesado

    def __init__(self, camera_index=0, parent=None):
        super().__init__()
        self.camera_index = camera_index
        self.running = True

    def run(self):
        cap = cv2.VideoCapture(self.camera_index)
        while self.running:
            ret, frame = cap.read()
            if ret:
                #Convertir de BGR a RGB y a un QImage
                rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                qt_image = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
                self.frame_ready.emit(qt_image)
            time.sleep(0.01) #Liberar CPU
        cap.release()

    def stop(self):
        self.running = False
        self.wait()

#---------------------------------------------------CREAR CLASE DE VENTANA PRINCIPAL-------------------------------------------------------

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, a_coeffs, b_coeffs):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) #Quita la barra de título de ventana
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground) #Pone el fondo principal transparante
        self.shadow = QGraphicsDropShadowEffect(self) #Empieza a crear un efecto de sombra
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 550))
        self.ui.centralwidget.setGraphicsEffect(self.shadow) #Aplica la sombra al widget central

        #Los íconos y título no se verán porque quitamos la barra de título
        self.setWindowIcon(QtGui.QIcon(u":/iconos/iconsselect/Delta.svg")) #Poner icono a la ventana
        self.setWindowTitle("Delta UI")
        QSizeGrip(self.ui.size_grip) #Crear lugar para agarrar ventana y modificar tamaño
        self.ui.minimize_window_button.clicked.connect(lambda: self.showMinimized()) #Minimizar ventana
        self.ui.close_window_button.clicked.connect(lambda: self.close()) #Cerrar ventana con botón de cerrado
        self.ui.exit_button.clicked.connect(lambda: self.close()) #Cerrar ventana con botón de salir
        #Configuración serial Python - Arduino
        self.serial_port = "/dev/ttyACM0" #Modificar a lo necesario
        self.baud_rate = 9600 #Modificar a lo necesario

        # En el __init__ de MainWindow:
        try:
            self.arduino = serial.Serial(port = self.serial_port, baudrate = self.baud_rate, timeout = 0.5, write_timeout =0.5)
            time.sleep(2) # Espera a que Arduino se inicialice.
            print("Conexión serial establecida correctamente")
        except Exception as e:
            print(f"Error de conexión: {str(e)}")
            QtWidgets.QMessageBox.critical(self, "Error de conexión", f"No se pudo conectar al Arduino: {self.serial_port}:\n{str(e)}")
            self.arduino = None  # Añadir este atributo para verificar conexión

        self.debounce_interval = 0.5 #ms

        self.buttons_commands = {
            'up': {
                'last_time': 0, 
                'msg': 'Arriba presionado',
                'command': ['U']
            },
            'down': {
                'last_time': 0,
                'msg': 'Abajo presionado',
                'command': ['D']
            },
            'right': {
                'last_time': 0,
                'msg': 'Derecha presionado',
                'command': ['R']
            },
            'left': {
                'last_time': 0,
                'msg': 'Izquierda presionado',
                'command': ['L']
            },
            'exit1': {
                'last_time': 0,
                'msg': 'Salida1 presionado',
                'command': ['exit1']
            },
            'exit2': {
                'last_time': 0,
                'msg': 'Salida2 presionado',
                'command': ['exit2']
            },
            'stop': {
                'last_time': 0,
                'msg': 'Parar presionado',
                'command': ['B']
            },
            'assistance': {
                'last_time': 0,
                'msg': 'Asistencia presionado',
                'command': ['Assistance']
            },
            'company': {
                'last_time': 0,
                'msg': 'Compania presionado',
                'command': ['Company']
            },
            'entertainment': {
                'last_time': 0,
                'msg': 'Entretenimiento presionado',
                'command': ['Entertainment']
            },
            'food': {
                'last_time': 0,
                'msg': 'Comida presionado',
                'command': ['Food']
            },
            'toilet': {
                'last_time': 0,
                'msg': 'Banio presionado',
                'command': ['Toilet']
            },
            'water': {
                'last_time': 0,
                'msg': 'Agua presionado',
                'command': ['Water']
            },
            'slide': {
                'last_time': 0,
                'msg': 'Slide presionado',
                'command': ['Slide']
            },
            'minimize': {
                'last_time': 0,
                'msg': 'Minimizar presionado',
                'command': ['min']
            }
        }


        self.ui.up_button.clicked.connect(lambda: self.handle_button('up'))  #Mostrar en el monitor serial que el botón fue presionado
        self.ui.down_button.clicked.connect(lambda:self.handle_button('down'))  #Mostrar en el monitor serial que el botón fue presionado
        self.ui.left_button.clicked.connect(lambda:self.handle_button('left'))  #Mostrar en el monitor serial que el botón fue presionado
        self.ui.right_button.clicked.connect(lambda:self.handle_button('right'))  #Mostrar en el monitor serial que el botón fue presionado
        self.ui.exit_button.clicked.connect(lambda: self.handle_button('exit1'))
        self.ui.close_window_button.clicked.connect(lambda: self.handle_button('exit2'))
        self.ui.stop_button.clicked.connect(lambda:self.handle_button('stop')) #Mostrar en el monitor serial que el botón fue presionado
        self.ui.ask_assistance_btn.clicked.connect(lambda:self.handle_button('assistance'))
        self.ui.ask_company_btn.clicked.connect(lambda:self.handle_button('company'))
        self.ui.ask_entertenaiment_btn.clicked.connect(lambda:self.handle_button('entertainment'))
        self.ui.ask_food_btn.clicked.connect(lambda:self.handle_button('food'))
        self.ui.ask_toilet_btn.clicked.connect(lambda:self.handle_button('toilet'))
        self.ui.ask_water_btn.clicked.connect(lambda:self.handle_button('water'))
        self.ui.open_close_side_bar_btn.clicked.connect(lambda:self.handle_button('slide')) #Prender y quitar menú de izquierda

        self.ui.minimize_window_button.clicked.connect(lambda: self.handle_button('minimize'))
        self.ui.restore_window_button.clicked.connect(lambda: self.handle_button('max'))
        

        #Añadir función de restaurar / maximizar pantalla
        self.ui.restore_window_button.clicked.connect(lambda: self.restore_or_maximize_window())

        self.velocidades = ['lenta', 'normal', 'rápida']
        self.idx = 0

        self.ui.speed_btn.clicked.connect(self.cambiar_velocidad)
        


        self.hover_threshold = 1000 #Umbral para hacer click en el boton si se hace hover en ms

        #Creación de timers para cada boton
        self.hover_timers = {}
        for name, btn in {
            'up': self.ui.up_button,
            'down': self.ui.down_button,
            'left': self.ui.left_button,
            'right': self.ui.right_button,
            'exit1': self.ui.exit_button,
            'exit2': self.ui.close_window_button,
            'stop': self.ui.stop_button,
            'slide': self.ui.open_close_side_bar_btn,
            'assistance': self.ui.ask_assistance_btn,
            'company': self.ui.ask_company_btn,
            'entertainment': self.ui.ask_entertenaiment_btn,
            'food': self.ui.ask_food_btn,
            'toilet': self.ui.ask_toilet_btn,
            'water': self.ui.ask_water_btn,
            'slide': self.ui.open_close_side_bar_btn,
            'min': self.ui.minimize_window_button,
            'max': self.ui.restore_window_button
        }.items():
            timer = QTimer(self, singleShot=True)
            timer.timeout.connect(lambda n=name: self.handle_button(n))
            self.hover_timers[btn] = timer
            #Instalar filtro de eventos
            btn.installEventFilter(self)


        #Función para mover la ventana con drag del mouse en la barra de título.
        def moveWindow(e):
            #Detecta si la ventana está en tamaño normal
            if self.isMaximized() == False: #No maximizado
                #Mover ventana solo cuando está en tamaño normal
                #Si el botón del mouse izquierdo se presiona...
                if e.buttons() == Qt.LeftButton:  
                    #Mover ventana
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        #Añadir evento de click de mouse y movimiento en el header para mover la ventana
        self.ui.header_frame.mouseMoveEvent = moveWindow

        

        #Configuración de cámara
        self.camera_thread = CameraThread(camera_index=0)
        self.camera_thread.frame_ready.connect(self.update_camera_view)
        self.camera_thread.start()
        
        #Asegurarse que la cámara se detenga al cerrar
        self.destroyed.connect(lambda: self.camera_thread.stop())
        
        # #Eyetracking en el fondo
        self.eye_thread = EyeTrackerThread(a_coeffs, b_coeffs, camera_index=2, alpha_percent=20)
        self.eye_thread.start()


        self.show()

    def closeEvent(self, event):
        # Parar el eyetracker
        if hasattr(self, 'eye_thread'):
            self.eye_thread.stop()
            print('Eyetracking closed')
        # Parar la cámara de la UI
        if hasattr(self, 'camera_thread') and self.camera_thread is not None:
            self.camera_thread.stop()
            print('UI Camera closed')
        # Cerrar ventanas OpenCV
        cv2.destroyAllWindows()
        # Cerrar serial
        if getattr(self, 'arduino', None):
            self.arduino.close()
            print('Arduino closed')
        super().closeEvent(event)

    def cambiar_velocidad(self):
        #Incrementar el índice
        self.idx = (self.idx + 1) % len(self.velocidades)
        #Actualizar el texto del botón
        self.ui.speed_btn.setText(f"Velocidad: {self.velocidades[self.idx]}")

    def eventFilter(self, watched, event):
        #Solo nos interesan los botones a los que instalamos filtro
        if watched in self.hover_timers:
            timer = self.hover_timers[watched]
            if event.type() == QEvent.Enter:
                #Iniciar el conteo regresivo
                timer.start(self.hover_threshold)
            elif event.type() == QEvent.Leave:
                #Cancela si se sale antes del umbral
                timer.stop()
        #Dejar que Qt procese el resto normalmente
        return super().eventFilter(watched, event)

    @Slot(QtGui.QImage)
    def update_camera_view(self, image):
        pixmap = QtGui.QPixmap.fromImage(image)
        #Verificar nombre de label, en QtDesigner se llama camera_feed_label
        self.ui.camera_feed_label.setPixmap(pixmap.scaled(
            self.ui.camera_feed_label.size(),
            QtCore.Qt.KeepAspectRatio,
            QtCore.Qt.SmoothTransformation
        ))

    def handle_button(self, btn_name):
        if self.arduino is None:  # Verificar si hay conexión
            return
    
        current_time = time.monotonic()
        # btn_data debe ser de self.buttons_commands
        if btn_name == 'slide':
            self.slideLeftMenu()
        if btn_name == 'exit1' or btn_name == 'exit2':
            self.close()
        if btn_name == 'min':
            self.showMinimized()
        if btn_name == 'max':
            self.restore_or_maximize_window()
        if btn_name in self.buttons_commands:
            btn_data = self.buttons_commands[btn_name]
            
            if current_time - btn_data['last_time'] >= self.debounce_interval:
                print(btn_data['msg'])
                # Enviar solo el carácter sin comas ni separadores
                comando = btn_data['command'][0] + '\n'
                self.arduino.write(comando.encode('ascii'))
                self.arduino.flush() #Asegurar envio inmediato
                btn_data['last_time'] = current_time
                print(f"Enviado: {comando.strip()}")

    #Función para prender y quitar menú izquierda
    def slideLeftMenu(self):
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, False)  # Desactiva translucidez
        #Conseguir el ancho del menú izquierdo actual
        width = self.ui.slide_menu_container.width()

        #Si está minimizado
        if width == 0:
            #Expandir el menú
            newWidth = 300
            self.ui.open_close_side_bar_btn.setIcon(QtGui.QIcon(u":/iconos/iconsselect/IconoirMenu.svg"))
        #Si está maximizado
        else:
            #Restaurar menú
            newWidth = 0
            self.ui.open_close_side_bar_btn.setIcon(QtGui.QIcon(u":/iconos/iconsselect/IconoirMenu.svg"))

        self.animation = QPropertyAnimation(self.ui.slide_menu_container, b"maximumWidth") #Animar
        #Minimo ancho   
        self.animation.setDuration(400) #
        self.animation.setStartValue(width) #El valor inicial es el ancho del menú actual
        self.animation.setEndValue(newWidth) #El valor de final es el nuevo ancho del menú
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        #self.animation.finished.connect(lambda: self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True))  # Reactiva al finalizar
        self.animation.start()



    #Agregar eventos de presionado de mouse
    def mousePressEvent(self, event):
        #Conseguir la posición actual
        self.clickPosition = event.globalPos()
        #Se usa esto como valor para mover la ventana

    def restore_or_maximize_window(self):
        #Si la ventana está maximizada
        if self.isMaximized():
            self.showNormal()
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u":/iconos/iconsselect/IconoirExpand.svg")) #Cambia ícono
        else:
            self.showMaximized()
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u":/iconos/iconsselect/IconoirExpand.svg")) #Cambia ícono, actualmente es el mismo



#---------------------------------------------------EJECUTAR PROGRAMA-------------------------------------------------------

if __name__ == "__main__":
    #Calibration
    print("Iniciando calibración...")
    puntos = calibrate(camera_index=2, alpha_percent=20)
    cv2.destroyAllWindows() #COMO SEA ESTO ME MATO
    if len(puntos) < 3:
        a_coeffs = np.array([1, 0, 0], dtype=np.float32)
        b_coeffs = np.array([0, 1, 0], dtype=np.float32)
    else:
        a_coeffs, b_coeffs = train_mapping(puntos)
    print("Calibración lista. Coeficientes obtenidos.")

    #Launch UI
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(a_coeffs, b_coeffs)
    window.show()

    sys.exit(app.exec_())