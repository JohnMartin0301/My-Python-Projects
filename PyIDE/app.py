from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess

compiler = Tk()
compiler.title('PyIDE')
file_path = ''

# Create editor and code_output widgets using grid
editor = Text()
editor.grid(row=0, column=0, padx=0, pady=0, sticky='nsew')  # Use sticky='nsew' to make it expand in all directions

code_output = Text(height=10)
code_output.grid(row=1, column=0, padx=0, pady=0, sticky='nsew')

# Configure rows and columns to expand when the window is resized
compiler.grid_rowconfigure(0, weight=1)
compiler.grid_columnconfigure(0, weight=1)

# Define color themes
themes = {
    "Light Theme": {'bg': 'white', 'fg': 'black'},
    "Dark Theme": {'bg': 'black', 'fg': 'white'},
    "Blespin": {'bg': '#483C32', 'fg': '#FFFF66'},
    "Blackboard": {'bg': '#0C1021', 'fg': '#F8F8F8'},
    "Dracula": {'bg': '#282A36', 'fg': '#F8F8F2'},
    "Duotone Dark": {'bg': '#2A2734', 'fg': '#9A86FD'},
    "Erlang Dark": {'bg': '#06243d', 'fg': '#FCF55F'},
    "Hacker" :{'bg': '#0D0E0E', 'fg': '#39FF14'},
    "Lesser Dark": {'bg': '#303030', 'fg': '#77aaed'},
    "Lucario": {'bg': '#2B3E50', 'fg': '#C5D4DD'},
    "Material": {'bg': '#263238', 'fg': '#EEFFFF'},
    "Monokai": {'bg': '#272822', 'fg': '#F8F8F2'},
    "Neo": {'bg': '#FBFFFF', 'fg': '#4781cc'},
    "Tomorrow Night Bright": {'bg': '#040406', 'fg': '#FFD700'},
    "Visual Studio": {'bg': '#1E1E1E', 'fg': '#D4D4D4'},
}

# Function to set the theme based on theme_name
def set_theme(theme_name):
    theme = themes.get(theme_name)
    if theme:
        editor.config(bg=theme['bg'], fg=theme['fg'])
        code_output.config(bg=theme['bg'], fg=theme['fg'])
        if theme_name in ['Dark Theme', 'Blespin', 'Blackboard', 'Dracula', 'Duotone Dark', 'Erlang Dark', 'Hacker', 'Lesser Dark', 'Lucario', 'Monokai', 'Tomorrow Night Bright', 'Visual Studio']:
            editor.config(insertbackground='white')  # Set caret color to white for darker themes
        else:
            editor.config(insertbackground='black')  # Set caret color to black for lighter themes
    else:
        print(f"Theme '{theme_name}' not found.")

# Set default theme
set_theme("Light Theme")

def set_file_path(path):
    global file_path
    file_path = path

def open_file():
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)

def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)

def run():
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Please save your code')
        text.pack()
        return
    command = f'python "{file_path}"'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0',  error)

menu_bar = Menu(compiler)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='File', menu=file_menu)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run', command=run)
menu_bar.add_cascade(label='Run', menu=run_bar)

# Create a Themes submenu
theme_menu = Menu(menu_bar, tearoff=0)
for theme_name in themes.keys():
    theme_menu.add_command(label=theme_name, command=lambda name=theme_name: set_theme(name))

menu_bar.add_cascade(label='Themes', menu=theme_menu)

compiler.config(menu=menu_bar)

compiler.mainloop()