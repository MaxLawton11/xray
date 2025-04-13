import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QLineEdit, QComboBox, QPushButton,
    QGridLayout, QLabel, QHBoxLayout
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import brems
import atten

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 with Multiple Matplotlib Plots")
        self.setGeometry(100, 100, 1200, 800)

        # Input layout
        input_layout = QHBoxLayout()
        input_layout.setAlignment(Qt.AlignLeft)  # Align inputs to the left

        # Energy input
        self.energy_input = QLineEdit(self)
        self.energy_input.setPlaceholderText("Enter energy")
        input_layout.addWidget(QLabel("Energy (keV):"))
        input_layout.addWidget(self.energy_input)

        # Thickness input FIRST
        self.thickness_input = QLineEdit(self)
        self.thickness_input.setPlaceholderText("Enter thickness")
        input_layout.addWidget(QLabel("Thickness (mm):"))
        input_layout.addWidget(self.thickness_input)

        # Material dropdown
        self.dropdown = QComboBox(self)
        self.dropdown.addItems(['Fe', 'Al', 'Si', 'Pb'])
        input_layout.addWidget(QLabel("Material:"))
        input_layout.addWidget(self.dropdown)

        # Submit button
        self.submit_button = QPushButton("Submit", self)
        self.submit_button.clicked.connect(self.on_submit)
        input_layout.addWidget(self.submit_button)

        # Create 4 matplotlib canvases
        self.figure1 = Figure()
        self.canvas1 = FigureCanvas(self.figure1)
        self.ax1 = self.figure1.add_subplot(111)

        self.figure2 = Figure()
        self.canvas2 = FigureCanvas(self.figure2)
        self.ax2 = self.figure2.add_subplot(111)

        self.figure3 = Figure()
        self.canvas3 = FigureCanvas(self.figure3)
        self.ax3 = self.figure3.add_subplot(111)

        self.figure4 = Figure()
        self.canvas4 = FigureCanvas(self.figure4)
        self.ax4 = self.figure4.add_subplot(111)

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)

        grid_layout = QGridLayout()
        grid_layout.addWidget(self.canvas1, 0, 0)
        grid_layout.addWidget(self.canvas2, 0, 1)
        grid_layout.addWidget(self.canvas3, 1, 0)
        #grid_layout.addWidget(self.canvas4, 1, 1)

        main_layout.addLayout(grid_layout)
        self.setLayout(main_layout)

    def on_submit(self):
        # Parse energy input
        energy_text = self.energy_input.text()
        try:
            energy = float(energy_text)
        except ValueError:
            print("Please enter a valid energy.")
            return

        # Parse thickness input
        thickness_text = self.thickness_input.text()
        try:
            thickness = float(thickness_text)
        except ValueError:
            print("Please enter a valid thickness.")
            return

        element = self.dropdown.currentText()
        x=6

        # Plot brems spectrum
        specs = brems.spectrum(energy)
        self.ax1.clear()
        self.ax1.plot(specs["karr"], specs["spkarr"], color='blue')
        self.ax1.set_title(f"Brems X-Ray Spectrum ({energy} keV)")
        self.ax1.set_xlabel("Energy [keV]")
        self.ax1.set_ylabel("Fluence [photons/cm²/mAs/keV]")

        # Plot transmission
        trans = atten.transmission(element, thickness, len(specs["karr"]), energy)
        self.ax2.clear()
        self.ax2.plot(trans["energies"], trans["transmission_per"], color='orange')
        self.ax2.set_title(f"Transmission Through {element} ({thickness:.2f} mm)")
        self.ax2.set_xlabel("Energy (eV)")
        self.ax2.set_ylabel("Transmission (%)")

        print(len(specs["karr"]), len(trans["energies"]))

        # Dummy plot 1
        energies_x_transmission = []
        for k, j in enumerate(trans["energies"]) :
            energies_x_transmission.append(specs["spkarr"][k] * trans["transmission_per"][k])

        self.ax3.clear()
        self.ax3.plot(trans["energies"], energies_x_transmission, color='green')
        self.ax3.set_title("Brems X-Ray Spectrum * Transmission (%)")
        self.ax3.set_xlabel("Energy (eV)")
        self.ax3.set_ylabel("Fluence [photons/cm²/mAs/keV]")

        # Dummy plot 2
        y_dummy2 = x**2
        self.ax4.clear()
        self.ax4.plot(x, y_dummy2, color='purple')
        self.ax4.set_title("Dummy Plot 2")
        self.ax4.set_xlabel("X-Axis")
        self.ax4.set_ylabel("Y-Axis")

        # Redraw all plots
        self.canvas1.draw()
        self.canvas2.draw()
        self.canvas3.draw()
        self.canvas4.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
