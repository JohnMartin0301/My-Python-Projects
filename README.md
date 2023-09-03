# My-Python-Projects



## *Automated Attendance System using QR Code




The Automated Attendance System using QR Codes offers a fast, accurate, and efficient way to manage attendance, leveraging the power of QR codes. An innovative solution for attendance management.





![pic1](https://github.com/JohnMartin0301/Automated-Attendance-System-using-QR-Code/assets/112761826/f1d61ba9-5645-409f-8d6a-23645d147fe6)





How it works:

Sample:


- Enter the student or participant’s ID and name.



![pic2](https://github.com/JohnMartin0301/Automated-Attendance-System-using-QR-Code/assets/112761826/384b6feb-8010-46d7-a199-b6775af10d62)



- Click generate Qr code containing the attendance information then save the Qr code in a directory. You can take a picture or print it on an ID card or display it digitally for future use. (For this time we will save it on a directory then take a picture of the Qr code).



![pic3](https://github.com/JohnMartin0301/Automated-Attendance-System-using-QR-Code/assets/112761826/c1c9749b-dc3f-4e90-9781-46da5c0d4e3e)



- To record attendance, simply use a camera or QR code scanner to capture the QR code. The system will decode the QR code, extract the attendance information, and mark the individual as present. The attendance record is then displayed to the user, providing immediate feedback.



![pic4](https://github.com/JohnMartin0301/Automated-Attendance-System-using-QR-Code/assets/112761826/cba1506c-e69b-4d47-93d1-01dde61c5d66)





## Usage

To use the Automated Attendance System, follow these steps:

1. **Run the Program:**
   - Run the `main.py` file using Python.
     ```bash
     python main.py
     ```

2. **Enter ID and Name:**
   - Enter the student/participant's ID and Name in the respective fields.

3. **Generate QR Code:**
   - Click the "Generate QR Code" button to create a QR code with the provided information.
   - Save the generated QR code.

4. **Scan QR Code:**
   - Click the "Scan QR Code" button to open the scanner.
   - Use the webcam to scan the QR codes of attendees.
   - The system records attendance and provides real-time feedback.

5. **Attendance Recorded:**
   - The system shows a message indicating that attendance has been recorded successfully.

6. **Repeat for More Attendees:**
   - Repeat the process for each student/participant.





Technical Overview:

> os - The os module provides a way to use operating system-dependent functionality, such as interacting with the file system. In this program, it is used for handling file and directory operations.

> cv2 (OpenCV) - OpenCV (Open Source Computer Vision Library) is a popular computer vision library used for various image and video processing tasks. It provides functions for video capturing, image manipulation, and computer vision algorithms. In this program, it is used for capturing video frames from the webcam and displaying them.

> tkinter - Tkinter is the standard Python interface to the Tk GUI toolkit. It provides a set of tools for creating graphical user interfaces (GUIs). In this program, Tkinter is used for creating the GUI window and various GUI components like labels, buttons, and entry fields.

> messagebox (part of tkinter) - The messagebox module provides a set of functions for displaying various types of message boxes in a GUI application. In this program, it is used to show information and warning messages to the user.

> filedialog (part of tkinter) - The filedialog module provides functions for displaying file dialogs to the user. It allows the user to select files or directories using a system-specific file dialog. In this program, it is used to prompt the user to select a directory to save the generated QR code.

> qrcode - The qrcode library is a Python library for creating QR codes. It allows you to generate QR codes from text or data. In this program, it is used to generate a QR code based on the ID and name entered by the user.

> pyzbar - The pyzbar library is a Python wrapper for the ZBar barcode and QR code scanning library. It provides functions for decoding barcodes and QR codes from images. In this program, it is used to scan and decode QR codes from the video frames captured by OpenCV.

These moduleslibraries are essential for different functionalities in the Automated Attendance System. They handle GUI creation, QR code generation, QR code scanning, and video capturingprocessing tasks.





The Automated Attendance System using QR Codes offers several benefits and features:

- Time-saving and efficient attendance management: The process of scanning QR codes is much faster compared to manual methods, saving valuable time.

- Improved accuracy and reliability: The system ensures accurate attendance records, minimizing errors and providing reliable data.

- Easy retrieval and storage: Attendance records can be easily stored digitally, eliminating the need for physical paperwork and enabling quick retrieval.

- Scalability: Whether you have a small classroom or a large conference, the system can handle attendance for any group size effectively.

- User-friendly interface: The system provides a user-friendly and intuitive interface, making it accessible to users with varying levels of technical expertise.





Use cases and applications:

- Educational institutions: Schools, colleges, and universities can streamline attendance management for classes, exams, and other activities.

- Corporate environments: Meetings, conferences, workshops, and training sessions can benefit from efficient attendance tracking.

- Events and conferences: Organizers can easily manage attendance for participants, speakers, and staff.

- Any setting requiring attendance management: From community organizations to healthcare facilities, the system can be adapted to various contexts.




Simplify attendance management with the Automated Attendance System using QR Code. Whether you're a teacher, event organizer, or manager, this tool makes attendance tracking efficient and hassle-free. Enjoy using the system! 🎫










## *College Course Recommender



 

This Python project helps you discover college courses based on your interests. If you're unsure about your course of study, this program is here to assist you.





![Courserecommender](https://github.com/JohnMartin0301/My-Python-Projects/assets/112761826/392c803a-1343-4c12-b37e-7f599e6f35fa)





The College Course Recommender Program simplifies your decision-making process when choosing a college course. By entering your interests, the program generates course recommendations tailored to your preferences.





## Features

- Interest-Based Recommendations: Discover college courses aligned with your interests.

- Years of Study: Find out the duration of each recommended course.

- Detailed Descriptions: Access course descriptions to make informed decisions.




Discover the perfect college course for you with the College Course Recommender Program. Start your educational journey today! 📚🏛🎓










## *Data Analysis on CSV





This Python project demonstrates the process of loading, analyzing, and manipulating data from a CSV (Comma-Separated Values) file using the powerful Pandas library. You can perform basic data exploration, calculate summary statistics, filter data, and even create new columns based on existing data.





![dacsv1](https://github.com/JohnMartin0301/My-Python-Projects/assets/112761826/daccb743-0ffd-400b-ae15-eb97bf8229e9)



![dacsv2](https://github.com/JohnMartin0301/My-Python-Projects/assets/112761826/2d9f5a53-2932-4974-b005-e2e2c9db0892)



![dacsv3](https://github.com/JohnMartin0301/My-Python-Projects/assets/112761826/5292e1fc-4a3b-48aa-8871-a45ac92fbeaa)





Data Analysis on CSV showcases how to work with tabular data stored in CSV format. With this project, you can load your CSV file, explore its contents, calculate summary statistics, filter data based on specific conditions, and perform custom data transformations. Whether you're a data analyst, scientist, or enthusiast, this tool provides a foundation for data analysis in Python.





## Features

- **CSV Data Loading:** Load your CSV data into a Pandas DataFrame.

- **Basic Data Exploration:** Display basic information and the first few rows of the dataset.

- **Summary Statistics:** Calculate and display summary statistics for numeric columns.

- **Column Averaging:** Calculate and display the average value of a specific column.

- **Data Filtering:** Filter rows based on specified conditions.

- **Data Transformation:** Create new columns based on transformations of existing data.

- **Data Export:** Save manipulated data to new CSV files.





## Usage

To use Data Analysis on CSV, follow these steps:

1. **Prepare Your Data:**
   - Ensure you have a CSV file (`csv_file`) with the data you want to analyze.
   
2. **Run the Program:**
   - Open the Python script in your preferred Python environment.
   - Set the `csv_file` variable to the path of your CSV file.

3. **Execute the Script:**
   - Run the script. It will load the data from your CSV file into a Pandas DataFrame.

4. **Explore the Data:**
   - The script will display basic information, the first few rows, and summary statistics of the dataset.

5. **Custom Analysis:**
   - Customize the script to perform specific data analysis tasks, such as calculating the average, filtering data, or creating new columns based on your requirements.

6. **Save Results:**
   - The script allows you to save filtered data to a new CSV file (`filtered_data.csv`) and the entire DataFrame with new columns to another CSV file (`manipulated_data.csv`).
  




Explore and analyze your CSV data effortlessly with Data Analysis on CSV. Whether you're studying datasets or conducting data-driven research, this tool provides a foundation for data exploration and analysis. Happy data analyzing! 📈










## *Goals Tracker





This Python project allows you to set, track, and manage your goals effectively. Whether you have personal, work-related, or academic goals, this tool will help you stay organized and motivated.





![goals1](https://github.com/JohnMartin0301/My-Python-Projects/assets/112761826/4e6f646c-e4ec-4909-b5cb-1743dddee2b5)



![goals2](https://github.com/JohnMartin0301/My-Python-Projects/assets/112761826/106f370c-2bc0-4590-82ce-8fa308cba3bc)





The Goal Tracker is a simple yet powerful solution for managing your goals. It provides features to add, view, remove, and mark goals as achieved. Additionally, it calculates and displays the percentage of goals achieved, giving you insights into your progress.





## Features

- Goal Management: Add, view, and remove goals with descriptions.

- Goal Achievement: Mark goals as achieved and move them from pending to achieved.

- Progress Tracking: Calculate and display the percentage of goals achieved.

- User-Friendly Interface: A straightforward command-line interface for ease of use.





## Usage

To use the Goal Tracker, follow these steps:

1. **Run the Program:**

   - Open a terminal window.
   - Navigate to the project directory.
   - Run the program using the following command:

     ```bash
     python main.py
     ```

2. **Main Menu:**

   - You will see the main menu with options to add goals, view goals, remove goals, mark goals as achieved, calculate the percentage of goals achieved, and exit.

3. **Choose an Option:**

   - Select an option by entering the corresponding number (1/2/3/4/5/6).

4. **Manage Your Goals:**

   - Follow the prompts to add, view, remove, or mark goals as achieved.
   - The program will display updated information, including the percentage of goals achieved.

5. **Exit:**

   - To exit the program, choose option 6 from the main menu.
  




Track and manage your goals efficiently with the Goal Tracker. Whether you're working on personal development, projects, or tasks, this tool will help you stay on track. Achieve your goals today! 🎯✅










## *Latest Technology News Fetcher





This Python project allows you to fetch and display the latest technology news from various sources. Stay updated with the latest tech trends and articles conveniently.





![latesttehcnews](https://github.com/JohnMartin0301/My-Python-Projects/assets/112761826/82b0f8cb-5c40-40c4-a210-e7e2ac81e86c)





The Latest Technology News Program is your gateway to staying informed about the ever-evolving world of technology. Fetch and display the most recent technology news articles effortlessly.





## Features

- Real-time Technology News: Access the latest technology news articles from various sources.

- Article Details: View article titles, authors, descriptions, content, publication dates, sources, and URLs.

- User-Friendly Interface: Easy-to-use command-line interface for a seamless user experience.





Stay up-to-date with the latest tech news using the Latest Technology News Program. Explore the world of technology with us! 🌐










## *Latest Technology News(GUI version)





This Python application allows you to fetch and display the latest technology news in a graphical user interface (GUI). Stay up-to-date with the latest tech trends and articles conveniently.





![latesttechnews(gui)](https://github.com/JohnMartin0301/My-Python-Projects/assets/112761826/0eb64a20-45ea-49c9-a459-e170df31731c)





The Latest Technology News (GUI) project combines the power of Python and the simplicity of a graphical interface to bring you the latest technology news. You can fetch and read news articles effortlessly, making it a valuable tool for tech enthusiasts and professionals.





## Features

- News Fetching: Fetch the latest technology news articles from various sources.

- User-Friendly GUI: The graphical user interface provides an intuitive way to read news.

- Article Details: View detailed information about each article, including title, author, description, content, publication date, source, and URL.

- Open Articles: Easily open full articles in your web browser or perform any desired action.

- Dark Mode: Enjoy reading news in a stylish dark-themed interface.





## Usage

To use the Latest Technology News (GUI) application, follow these steps:

1. **Run the Program:**

   - Run the `main.py` file using Python.

     ```bash
     python main.py
     ```

2. **Explore the GUI:**

   - The application opens with the latest technology news headlines displayed in the GUI.
   - Scroll through the news articles to find the topics that interest you.

3. **View Article Details:**

   - Click on any news headline to view detailed information about the article.

4. **Open Full Articles:**

   - Click on the "URL" link in an article's details to open the full article in your web browser.

5. **Fetch Latest News:**

   - Click the "Fetch News" button to refresh and fetch the latest technology news.

6. **Enjoy Reading:**

   - Enjoy reading the latest tech news in a user-friendly and visually appealing interface.
  




Stay updated with the latest technology news using the Latest Technology News (GUI) application. Whether you're a tech enthusiast or professional, this tool makes it easy to stay informed about the latest tech trends. Enjoy reading tech news in style! 🌐










## *MasterLock Vault Program 





This Python program allows you to lock and unlock your files using password-based encryption. Keep your sensitive files secure and accessible only to those who have the password.





![ml2](https://github.com/JohnMartin0301/My-Python-Projects/assets/112761826/1fa69ab6-e14c-4b72-b2bc-9ae8d3725dd6)





The MasterLock Vault Program is designed to provide a secure and user-friendly way to lock and unlock files. It uses password-based encryption to protect your files from unauthorized access. Whether you want to secure documents, images, or any other type of file, the MasterLock Vault Program has you covered.





## Features

- File Locking: Lock your files with a password to protect them from unauthorized access.

- File Unlocking: Unlock your locked files by providing the correct password.

- Display Locked Files: View a list of locked files and their paths.





## Usage

The MasterLock Vault Program offers a menu-driven interface for managing your locked files:

- MasterLock a File🔐: Use this option to lock a file by providing its path and a password.

- Unlock a File🔓: Unlock a previously locked file by providing its path and the correct password.

- Display Locked Files📁: View a list of all locked files and their paths.

- Exit🔚: Exit the MasterLock Vault Program.





## Getting Started

- Encryption Key: The program generates an encryption key when you first run it. This key is stored securely for future use.

- Locking a File: Select option 1 to lock a file. Provide the file's path and a password to lock it.

- Unlocking a File: Select option 2 to unlock a file. Provide the file's path and the correct password to unlock it.

- View Locked Files: Select option 3 to view a list of locked files and their paths.

- Password Security: Ensure the security of your passwords. Choose strong and unique passwords for each locked file.


## Example:

- Select option 1 to lock a file. Provide the file's path and a password to lock it.



![ml2](https://github.com/JohnMartin0301/My-Python-Projects/assets/112761826/169975ff-fc12-468f-a580-c03a2ba26439)



![ml1](https://github.com/JohnMartin0301/My-Python-Projects/assets/112761826/1514659c-6257-459d-b64b-9dfddb9d151b)



- After providing a password, the program generates an encryption key and will be stored securely for future use.



![ml3](https://github.com/JohnMartin0301/My-Python-Projects/assets/112761826/96088c45-fa98-4700-b9b4-a57db589c5ff)



- Select option 3 to view a list of locked files and their paths.



![ml4](https://github.com/JohnMartin0301/My-Python-Projects/assets/112761826/524257ab-b754-4482-8aa6-fd9d15fbd35a)



- Select option 2 to unlock a file. Provide the file's path and the correct password to unlock it.



![ml5](https://github.com/JohnMartin0301/My-Python-Projects/assets/112761826/e402359f-00a4-42e3-a050-7491bfb4c6bf)



- The file will be unlocked and gets back to its original form.



![ml6](https://github.com/JohnMartin0301/My-Python-Projects/assets/112761826/cb4ca45c-c2cb-43ff-91a3-19d2685f127a)





Secure your files and keep them away from prying eyes with the MasterLock Vault Program. Protect your files with MasterLock today! 🔒


  








## *PyVault





This Python project allows you to securely store and retrieve your platform credentials. Keep your passwords organized and easily accessible while maintaining a high level of security.





![pyvault1](https://github.com/JohnMartin0301/My-Python-Projects/assets/112761826/a6fc5051-6598-470b-8840-e76559b45af6)



![pyvault2](https://github.com/JohnMartin0301/My-Python-Projects/assets/112761826/e47320b1-ecad-46af-86a2-7c261e8f77a9)





PyVault is your personal password manager, designed to help you keep track of your platform credentials. Whether it's website logins or app passwords, PyVault provides a secure and organized way to store and retrieve this vital information.





## Features

- Secure Password Storage: Safely store your platform details, including the platform name, username (if applicable), and password.

- Efficient Retrieval: Retrieve your stored passwords with ease, ensuring you always have your credentials when you need them.

- Display Details: Quickly view all your stored platform details, including usernames and passwords.





## Usage

- PyVault offers a straightforward menu-driven interface for managing your passwords:

- Store Password🔐: Use this option to store a new platform's credentials securely.

- Retrieve Password🔓: Retrieve a platform's stored credentials.

- Display Details📄: View all stored platform details, including usernames and passwords.

- Exit🔚: Exit PyVault.





## Getting Started

- Ensure CSV File: PyVault uses a CSV file to store your credentials. If you don't already have a file, PyVault will create one for you.

- Choose an Option: When you run PyVault, choose one of the provided options to store, retrieve, or display your credentials.

- Follow Prompts: Follow the prompts to complete your desired action.

- Password Security: Ensure the security of your password file. Keep it safe and protected from unauthorized access.





Enjoy the convenience and security of PyVault for managing your passwords. Secure your secrets with PyVault today! 🔒










## *SecURL





A simple GUI app built using Python that checks if a URL/Link is safe or not. This can help prevent Phishing Attacks which is very common nowadays.





SecURL is a simple Python application that allows you to check the safety of a URL. It helps you determine whether a given URL is safe or potentially harmful by making HTTP requests and analyzing the response status.





![SecURL01](https://github.com/JohnMartin0301/SecURL/assets/112761826/e1746a33-04a8-47aa-9662-81751f8a5511)






SecURL offers the following:

- Accepts user input for a URL/Link to be checked.

- Verifies the safety of the URL/Link by sending a GET request and checking the response status.

- Notifies the user whether the URL/Link is safe or not.





Sample:



![SecURL02](https://github.com/JohnMartin0301/SecURL/assets/112761826/b9d808be-4968-4649-878f-9d56404890dd)



![SecURL03](https://github.com/JohnMartin0301/SecURL/assets/112761826/7b8d47a0-08bf-48fe-a6a9-1a578c2f11af)





SecURL provides a straightforward way to assess the safety of a URL. It sends a GET request to the specified URL and examines the response status code. If the response status code indicates success (less than 400), the URL is considered safe; otherwise, it is flagged as potentially unsafe. This tool is useful for quickly checking the safety of URLs you encounter.





## Usage

To use SecURL, follow these simple steps:

1. **Run the Program:**
   - Run the `main.py` file using Python.
     ```bash
     python main.py
     ```

2. **Enter URL:**
   - Enter the URL you want to check in the provided entry field.

3. **Check URL Safety:**
   - Click the "Check URL Safety" button.
   - The program will send an HTTP request to the URL and display whether it's safe or not.

4. **View Result:**
   - The result label will update with the safety status.
   - A safe URL is indicated in green text, while an unsafe URL is indicated in red text.





Technical Overview:

1. tkinter (import tkinter as tk):
- tkinter is a standard Python library for creating graphical user interfaces (GUIs).
- It provides a set of tools and widgets to build windows, buttons, labels, entry fields, and more.
- In the URL Safety Checker program, tkinter is used to create the GUI elements, such as labels, entry fields, buttons, and the main application window.



2. urllib3 (import urllib3):
- urllib3 is a powerful, user-friendly HTTP client library for Python.
- It provides a higher-level abstraction over the standard urllib library for making HTTP requests.
- In the URL Safety Checker program, urllib3 is used to send HTTP GET requests to check the safety of the provided URL.
- It also handles the response and analyzes the response status to determine the safety of the URL.



3. urllib3.exceptions.MaxRetryError:
- This is an exception class provided by the urllib3 library.
- It is used to handle exceptions that occur when the maximum number of retries is exceeded for an HTTP request.
- In the URL Safety Checker program, this exception is caught to handle potential errors when making HTTP requests.



These modules/libraries provide the necessary functionality for creating the GUI, making HTTP requests, and handling exceptions in the URL Safety Checker program. They enable the program to interact with the user, retrieve the URL for checking, send HTTP requests to validate the safety, and display the result in the GUI.





Check the safety of URLs quickly and easily with SecURL. Whether you're verifying links or ensuring online safety, this tool provides immediate feedback on URL safety. Stay safe online! 🔐










## *Terminal Based Chat App





This Python project allows you to create a simple chat server and client using sockets. Connect with your friends or colleagues over a local network and chat in real-time.





![terminalbasedchatapp](https://github.com/JohnMartin0301/My-Python-Projects/assets/112761826/bcf54480-adaa-4d59-8964-f60ea4b089e9)





The Terminal Based Chat Application is a lightweight chat solution for local network communication. It consists of two components: a chat server (`server.py`) and a chat client (`client.py`). By running the server and connecting clients, you can exchange text messages in a terminal-based chat environment.





## Features

- Real-Time Chat: Enjoy real-time communication with multiple users.

- Usernames: Assign usernames to participants for a personalized chat experience.

- Simplicity: The project's simplicity makes it easy to understand and extend.





## Usage

To use the Terminal Based Chat Application, follow these steps:

1. **Run the Server:**

   - Open a terminal window.
   - Navigate to the project directory.
   - Run the server using the following command:

     ```bash
     python server.py
     ```

   - The server will listen for incoming connections.

2. **Run the Client:**

   - Open a new terminal window (you can run multiple client terminals for testing).
   - Navigate to the project directory.
   - Run the client using the following command:

     ```bash
     python client.py
     ```

   - Enter your desired username when prompted.

3. **Chat Away:**

   - Start typing messages in the client terminals.
   - Press `Enter` to send your message.
   - Messages will be relayed to all connected clients.

4. **Exit the Client:**

   - To exit a client, press `Ctrl+C`.

5. **Exit the Server:**

   - To stop the server, return to its terminal window and press `Ctrl+C`.





Chat with your friends and colleagues effortlessly using the Terminal Based Chat Application. Start chatting today! 💬
