# INTRODUCTION

Neuromuscular conditions such as amyotrophic lateral sclerosis (ALS) or spinal cord injuries lead to progressive mobility loss, forcing patients into critical dependency for daily activities. In response to this challenge, our project presents an electric wheelchair controlled by eye tracking—a solution that empowers users to regain autonomy through technology. Unlike commercial systems that require physical components (such as joysticks or switches), our prototype interprets the user's intention to move directly from their gaze, removing barriers for those who have lost muscular control.

The system combines computer vision algorithms for iris tracking with a semi-autonomous navigation module. Using a low-cost camera and real-time image processing techniques, the software translates eye coordinates into directional commands (forward, backward, turns) that are sent to an Arduino Mega controller. At the same time, ultrasonic sensors and an integrated accelerometer detect obstacles within a 1.5-meter radius, activating automatic brakes when collision risk exceeds predefined thresholds. This safety layer is essential for indoor environments with limited space.

Statistics emphasize the urgency of such solutions—ALS has a global incidence of 1.9 cases per 100,000 people, with a projected 69% increase by 2040 due to population aging. Yet, access to assistive technologies remains limited.

This project not only demonstrates the technical feasibility of accessible systems, but also opens the door to future improvements.

![System Architecture](https://github.com/chindynamics/Delta-Assistance/blob/43641fafab4b2570722a5ae9a48f42b96d3819b5/docs/media/diagramafuncionamientoblanco.drawio.png)

*Figure 1: System data flow. The camera captures eye movement, the algorithm translates it into coordinates, and Arduino sends signals to the motors, while ultrasonic sensors monitor the surroundings.*
