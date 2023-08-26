# Import necessary libraries
import os  # For operating system related operations
import cv2  # OpenCV library for image processing
import tkinter as tk  # Tkinter library for GUI
from tkinter import messagebox, filedialog  # Specific components from Tkinter
import qrcode  # Library for generating QR codes
from pyzbar import pyzbar  # Library for decoding QR codes

# Define a class for the Attendance System
class AttendanceSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Automated Attendance System using QR Code")  # Set the title of the GUI window
        self.root.geometry("400x300")  # Set the size of the GUI window
        self.root.configure(bg="#F0F0F0")  # Set the background color of the GUI window

        self.main_frame = tk.Frame(self.root, padx=20, pady=20, bg="#F0F0F0")  # Create a frame for the main content
        self.main_frame.pack()  # Pack the frame into the window

        # Create and pack labels and entry fields for ID and Name
        self.label_id = tk.Label(self.main_frame, text="Enter ID:", font=("Arial", 12), bg="#F0F0F0")
        self.label_id.pack()
        self.entry_id = tk.Entry(self.main_frame, font=("Arial", 12), width=30)
        self.entry_id.pack(pady=10)
        self.label_name = tk.Label(self.main_frame, text="Enter Name:", font=("Arial", 12), bg="#F0F0F0")
        self.label_name.pack()
        self.entry_name = tk.Entry(self.main_frame, font=("Arial", 12), width=30)
        self.entry_name.pack(pady=10)

        # Create and pack buttons for generating and scanning QR codes
        self.button_generate = tk.Button(self.main_frame, text="Generate QR Code", command=self.generate_qr_code, font=("Arial", 12), width=15, bd=0, bg="#4CAF50", fg="white", activebackground="#45A049", activeforeground="white")
        self.button_generate.pack(pady=10)
        self.button_scan = tk.Button(self.main_frame, text="Scan QR Code", command=self.scan_qr_code, font=("Arial", 12), width=15, bd=0, bg="#2196F3", fg="white", activebackground="#1976D2", activeforeground="white")
        self.button_scan.pack(pady=10)

    # Function to generate QR code
    def generate_qr_code(self):
        id_number = self.entry_id.get()  # Get ID from the entry field
        name = self.entry_name.get()  # Get Name from the entry field
        if id_number and name:  # Check if both ID and Name are provided
            data = f"ID: {id_number}, Name: {name}"  # Format the data
            qr = qrcode.QRCode(version=1, box_size=10, border=5)  # Create a QR code object
            qr.add_data(data)  # Add the data to the QR code
            qr.make(fit=True)  # Generate the QR code
            img = qr.make_image(fill="black", back_color="white")  # Create an image from the QR code

            # Ask the user to select a directory to save the QR code image
            save_directory = filedialog.askdirectory(title="Select Directory to Save QR Code")
            if save_directory:  # If a directory is selected
                save_path = os.path.join(save_directory, "qrcode.png")  # Set the save path
                img.save(save_path)  # Save the image
                messagebox.showinfo("QR Code Generated", f"QR Code has been generated successfully!\nSaved at: {save_path}")  # Show a success message
            else:  # If no directory is selected
                messagebox.showwarning("Directory Not Selected", "Please select a directory to save the QR code!")  # Show a warning message
        else:  # If ID or Name is missing
            messagebox.showwarning("Missing Information", "Please enter ID and Name!")  # Show a warning message

    # Function to scan QR code
    def scan_qr_code(self):
        capture = cv2.VideoCapture(0)  # Initialize video capture
        scanned_attendances = []  # List to store scanned attendances
        while True:
            _, frame = capture.read()  # Read a frame from the video capture
            decoded_objects = pyzbar.decode(frame)  # Decode QR codes from the frame
            for obj in decoded_objects:
                if obj.type == 'QRCODE':
                    data = obj.data.decode('utf-8')  # Decode the data from the QR code
                    if data not in scanned_attendances:
                        scanned_attendances.append(data)  # Add the attendance data to the list
                        messagebox.showinfo("QR Code Scanned", f"Attendance recorded for: {data}")  # Show an information message
            cv2.imshow("QR Code Scanner", frame)  # Display the frame in a window
            if cv2.waitKey(1) == ord('q'):  # If 'q' key is pressed, exit the loop
                break
        capture.release()  # Release the video capture
        cv2.destroyAllWindows()  # Close all the windows

# Main program
if __name__ == "__main__":
    root = tk.Tk()  # Create the root window
    root.resizable(False, False)  # Disable window resizing
    attendance_system = AttendanceSystem(root)  # Create an instance of the AttendanceSystem class
    root.mainloop()  # Run the GUI main loop