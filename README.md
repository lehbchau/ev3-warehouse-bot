# Autonomous Product Retrieval System (EV3 Robot)

### Overview
This project implements a scaled prototype of an **Autonomous Product Retrieval (APR) System** for Buy More, a home entertainment, computer, and gaming store that is transitioning to online sales. The robot, built using LEGO EV3 components and programmed in Python through Visual Studio Code, retrieves boxes from designated locations in a simulated warehouse environment and delivers them to specified order fulfillment areas.

### Features
- **Autonomous Navigation**: The robot navigates a scaled warehouse environment without using GPS or traditional indoor navigation aids, instead relying on precise location tracking.
- **Barcode Scanning**: Uses simple barcode scanning techniques to verify if a retrieved box matches the requested product.
- **Product Retrieval**: Picks up a box if it matches the requested barcode and transports it to the designated fulfillment area.
- **Error Handling**: If the retrieved product does not match the requested one, displays the location and barcode on the screen and returns to the starting position.
- **Collision Avoidance**: Designed to avoid obstacles and other objects while in motion, ensuring safe operations.

### Hardware Requirements
- LEGO EV3 Robot Kit
- Computer with Visual Studio Code installed
- MicroSD/MicroSDHC memory card (above 2GB and below 32GB)

### Software Requirements
- Python 3.x
- EV3 MicroPython libraries
- Visual Studio Code with Python extension
- LEGO EV3 Device Manager

### Getting Started
1. **Setup the Development Environment**:
   - Install Python 3.x and Visual Studio Code on your computer
   - Set up the MicroSD/MicroSDHC card for use with EV3 Robot (Instructions: [EV3 Dev Getting Started](https://www.ev3dev.org/docs/getting-started/))
   - Clone this repository using:
     ```bash
     git clone https://github.com/lehbchau/ev3-warehouse-bot.git
     ```
   - Connect the EV3 brick to your computer using a USB or Bluetooth connection

2. **Deploy the Code to EV3**:
   - Copy the Python scripts from the `src/` directory to the EV3 brick using the LEGO EV3 Device Manager
   - Ensure the EV3 brick has the necessary Python libraries installed

3. **Configure the Warehouse Layout**:
   - Set up the scaled warehouse area as described in the RFP document
   - Place boxes with barcodes at designated locations

4. **Run the Robot**:
   - Execute the Python script on the EV3 brick
   - The robot will await a product code, navigate to the box location, verify the barcode, retrieve the box, and deliver it to the correct fulfillment area

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments

- **LEGO Group**: For providing the EV3 robot kit
- **MicroPython Team**: For developing MicroPython, which enables Python programming on the EV3 brick
- **My Teammates**: Sarah Barazi and Jacob Haire for their collaboration and contributions throughout this project
