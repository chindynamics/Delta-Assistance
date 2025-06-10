# Delta Assistance

Delta Assistance es un sistema de movilidad asistida diseñado para personas con parálisis o movilidad reducida, controlado mediante el seguimiento de la mirada. El proyecto combina visión por computadora, control de hardware y diseño accesible para ofrecer una solución funcional, de bajo costo y adaptable.
Este repositorio contiene todo el código, documentación técnica y recursos necesarios para replicar o entender el desarrollo del proyecto.

## CONTENIDO

A continuación, se enlistan los apartados disponibles para conocer el proyecto con mayor detalle:
- [Introducción](https://github.com/chindynamics/Delta-Assistance/blob/main/docs/es/1.-%20introduccion.md): contexto, motivación y objetivos del proyecto.
- [Instalación](https://github.com/chindynamics/Delta-Assistance/blob/main/docs/es/2.-%20instalacion.md): guía paso a paso para clonar el repositorio, instalar dependencias y ejecutar el sistema.
- [Documentación](https://github.com/chindynamics/Delta-Assistance/blob/main/docs/es/3.-%20documentacion.md): explicación técnica completa del proceso de diseño, integración y validación del sistema.

## CARACTERÍSTICAS

El sistema de Delta Assistance está diseñado para ser accesible, modular y adaptable. Su principal innovación radica en el uso de visión por computadora para interpretar la dirección de la mirada del usuario, y convertirla en comandos para mover una silla de ruedas eléctrica. La interfaz de seguimiento ocular fue desarrollada en Python en base al código abierto de Jason Orlosky, mientras que el control de movimiento fue implementado en un microcontrolador Arduino Mega utilizando código en C++. Esta combinación permite una comunicación eficiente entre el usuario y la máquina, incluso sin contacto físico.

Además del seguimiento ocular, se diseñó una placa de circuito personalizada para controlar los motores de la silla y se adaptó una estructura física capaz de integrarse a una silla de ruedas convencional. El sistema es capaz de reconocer cinco comandos: avanzar, retroceder, girar a la izquierda, girar a la derecha y detenerse. Su diseño considera entornos reales, como diferentes condiciones de iluminación o interferencias físicas.

## COLABORACIÓN

Si estás interesado en mejorar este sistema, adaptarlo a nuevas necesidades o contribuir con tu experiencia en software, hardware o diseño accesible, eres bienvenido a colaborar. Puedes hacerlo abriendo un issue para reportar problemas o sugerencias, o enviando un pull request con mejoras específicas. Este proyecto también puede servir como base educativa o de investigación para otros desarrollos en el campo de la ingeniería biomédica y las tecnologías asistivas.

## LICENCIA

Este proyecto se distribuye bajo la licencia MIT, lo que significa que puedes utilizar, modificar y redistribuir libremente el código y los recursos aquí compartidos, siempre y cuando se otorgue el debido crédito a los autores originales.
