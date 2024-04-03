from tkinter import Tk, Button, Label, filedialog, simpledialog, messagebox
from PIL import Image, ImageTk
import os

FONT_STYLE = ("Arial", 10)


def convert_to_ico(input_image_path, output_directory, prefix):
    # Open the image
    image = Image.open(input_image_path)

    # Save the modified image as ICO format
    ico_image_path = os.path.join(output_directory,
                                  prefix + os.path.splitext(os.path.basename(input_image_path))[0] + ".ico")
    image.save(ico_image_path)

    return ico_image_path


def browse_file():
    filenames = filedialog.askopenfilenames()
    for filename in filenames:
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            input_files.append(filename)
        else:
            messagebox.showerror("Error", f"Unsupported file type: {os.path.basename(filename)} \n Try again bruz.")
    update_label()


def browse_output_directory():
    global output_directory
    output_directory = filedialog.askdirectory()
    update_label()


def get_prefix():
    global prefix
    prefix = simpledialog.askstring("Prefix", "Enter prefix:", initialvalue="icon_")
    if not prefix:
        prefix = "icon_"
    update_label()


def update_label():
    files_label.config(text="\n".join([os.path.basename(file) for file in input_files]))
    output_label.config(text=output_directory if output_directory else "Icons")
    prefix_label.config(text=prefix)


def convert_images():
    if not input_files:
        return

    for file_path in input_files:
        output_path = output_directory if output_directory else os.path.expanduser("~/Downloads/Icons")
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        ico_image_path = convert_to_ico(file_path, output_path, prefix)
        print(f"Converted {os.path.basename(file_path)} to ICO format: {ico_image_path}")

    messagebox.showinfo("Success", "Images successfully converted!")


if __name__ == "__main__":
    # Initialize Tkinter
    root = Tk()
    root.title("Image to ICO Converter")
    root.geometry("400x400")

    # Set default font style
    root.option_add("*Font", FONT_STYLE)

    # Global variables
    input_files = []
    output_directory = ""
    prefix = "icon_"

    # Add padding around the entire window
    root.configure(pady=10)

    browse_input_button = Button(root, text="Select file(s)", command=browse_file)
    browse_input_button.pack(pady=10, padx=10)

    browse_output_button = Button(root, text="Output directory", command=browse_output_directory)
    browse_output_button.pack(pady=3, padx=3)

    output_label = Label(root, text="Default: ~/Downloads/Icon")
    output_label.pack(pady=3)

    get_prefix_button = Button(root, text="Set prefix", command=get_prefix)
    get_prefix_button.pack(pady=3)

    prefix_label = Label(root, text="Example: " + prefix + "hello.ico")
    prefix_label.pack(pady=3)

    convert_button = Button(root, text="CONVERT", command=convert_images)
    convert_button.pack(pady=10)

    input_label = Label(root, text="Files to convert:")
    input_label.pack(pady=5)

    files_label = Label(root, text="")
    files_label.pack(pady=5)

    root.mainloop()
