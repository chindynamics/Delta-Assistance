## INTRODUCCIÓN

Los padecimientos neuromusculares como la esclerosis lateral amiotrófica (ELA) o las lesiones medulares generan una pérdida progresiva de la movilidad, relegando a los pacientes a una dependencia crítica de terceros para actividades cotidianas. Frente a este desafío, nuestro proyecto desarrolla una silla de ruedas eléctrica controlada mediante seguimiento ocular, una solución que empodera a los usuarios reconquistando su autonomía a través de la tecnología. A diferencia de sistemas comerciales que requieren componentes físicos (como joysticks o pulsadores), nuestro prototipo interpreta la intención de movimiento directamente desde la mirada, eliminando barreras para quienes han perdido el control muscular.

El sistema combina algoritmos de visión por computadora para el rastreo del iris con un módulo de navegación autónoma. Utilizando una cámara de bajo costo y técnicas de procesamiento de imágenes en tiempo real, el software traduce coordenadas oculares en comandos direccionales (avance, retroceso, giros) que son enviados a un controlador Arduino Mega. Paralelamente, sensores ultrasónicos y un acelerómetro integrado detectan obstáculos en un radio de 1.5 metros, activando frenos automáticos cuando el riesgo de colisión supera umbrales predefinidos. Esta capa de seguridad es clave para entornos domésticos con espacios reducidos.

Las estadísticas subrayan la urgencia de estas soluciones, la incidencia global de ELA alcanza 1.9 casos por cada 100,000 personas, con un crecimiento proyectado del 69% para 2040 debido al envejecimiento poblacional. Sin embargo, el acceso a tecnologías asistivas sigue siendo limitado. 

Este proyecto no solo demuestra la viabilidad técnica de sistemas accesibles, sino que también abre puertas a futuras mejoras.

![image](:/media/diagramafuncionamiento.png)
