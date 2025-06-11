# Delta Assistance

**Delta Assistance** is an assisted mobility system designed for individuals with paralysis or reduced mobility, controlled through eye-tracking. The project combines computer vision, hardware control, and accessible design to offer a functional, low-cost, and adaptable solution. This repository contains all the code, technical documentation, and resources necessary to replicate or understand the development of the project.

## CONTENT

Below are the sections available to explore the project in more detail:  
- [Introduction](https://github.com/chindynamics/Delta-Assistance/blob/main/docs/es/1.-%20introduccion.md): context, motivation, and project objectives.  
- [Installation](https://github.com/chindynamics/Delta-Assistance/blob/main/docs/es/2.-%20instalacion.md): step-by-step guide to clone the repository, install dependencies, and run the system.  
- [Documentation](https://github.com/chindynamics/Delta-Assistance/blob/main/docs/es/3.-%20documentacion.md): full technical explanation of the design, integration, and validation process.

## FEATURES

The Delta Assistance system is designed to be accessible, modular, and adaptable. Its main innovation lies in the use of computer vision to interpret the user's gaze direction and convert it into commands to move a powered wheelchair. The eye-tracking interface was developed in Python based on Jason Orlosky's open-source code, while motion control was implemented on an Arduino Mega microcontroller using C++. This combination enables efficient communication between the user and the machine—even without physical contact.

In addition to the eye-tracking interface, a custom circuit board was designed to control the wheelchair motors, and a physical structure was adapted to integrate with a conventional wheelchair. The system is capable of recognizing five commands: move forward, move backward, turn left, turn right, and stop. Its design takes into account real-world environments, including varying lighting conditions and physical interference.

## COLLABORATION

This project was developed by the Delta Assistance team:

- [@chindynamics](https://github.com/chindynamics) – Lead on computer vision pipeline and human–computer interaction design.
- [@Sarao2341](https://github.com/Sarao2341) – Responsible for 3D modeling and mechanical integration.
- [@reginaruizz](https://github.com/reginaruizz) – PCB schematic and layout. Selected components for the power regulation stages, designed the custom board in KiCad, and verified signal integrity.
- [@Ulin81](https://github.com/Ulin81) – Electronics integration and firmware support. Assisted with PCB bring-up, wrote and tested the Arduino Mega firmware modules.
- [@haydeevazquez](https://github.com/haydeevazquez) – Sound processing and obstacle detection.
- [@mirelyyc](https://github.com/mirelyyc) – UI and iconography designer. Created the visual assets for the desktop interface, designed status icons and ensured consistency across the user experience.


If you're interested in improving this system, adapting it to new needs, or contributing your expertise in software, hardware, or accessible design, you're welcome to collaborate. You can do so by opening an issue to report problems or suggestions, or by submitting a pull request with specific improvements. This project may also serve as an educational or research base for further developments in biomedical engineering and assistive technologies.

## LICENSE

This project is distributed under the [MIT License](https://github.com/chindynamics/Delta-Assistance/blob/main/LICENSE), meaning you are free to use, modify, and redistribute the code and resources shared here, as long as proper credit is given to the original authors.
