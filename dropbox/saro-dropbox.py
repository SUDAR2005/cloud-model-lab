import dropbox
from tkinter import Tk, Button, Label, simpledialog, messagebox, filedialog
import os

# Dropbox access token (replace with your actual token)
ACCESS_TOKEN ='Your_ACCESS_TOken'

# Upload to Dropbox
def upload_file(filepath):
    dbx = dropbox.Dropbox(ACCESS_TOKEN)
    with open(filepath, 'rb') as f:
        dbx.files_upload(f.read(), '/' + os.path.basename(filepath))
    status_label.config(text="Uploaded successfully!")

# Download from Dropbox
def download_file(dropbox_path):
    dbx = dropbox.Dropbox(ACCESS_TOKEN)
    try:
        _, res = dbx.files_download(dropbox_path)
        local_path = os.path.join(os.getcwd(), os.path.basename(dropbox_path))
        with open(local_path, 'wb') as f:
            f.write(res.content)
        status_label.config(text="Downloaded successfully!")
    except Exception as e:
        status_label.config(text="Download failed")

# List files in Dropbox root
def list_dropbox_files():
    dbx = dropbox.Dropbox(ACCESS_TOKEN)
    try:
        return [entry.name for entry in dbx.files_list_folder('').entries]
    except Exception:
        messagebox.showerror("Error", "Unable to list files.")
        return []

# Upload dialog
def select_and_upload():
    filepath = filedialog.askopenfilename()
    if filepath:
        upload_file(filepath)

# Download dialog
def download_dialog():
    files = list_dropbox_files()
    if files:
        selected_file = simpledialog.askstring("Select File", "Choose file:\n" + ', '.join(files))
        if selected_file in files:
            download_file(f'/{selected_file}')
        else:
            messagebox.showinfo("Invalid", "No valid file selected.")
    else:
        messagebox.showinfo("No Files", "No files in Dropbox.")

# Tkinter GUI setup
root = Tk()
root.title("Dropbox Uploader & Downloader")

Button(root, text="Upload File", command=select_and_upload).pack(pady=10)
Button(root, text="Download File", command=download_dialog).pack(pady=10)

status_label = Label(root, text="Select an action to proceed.")
status_label.pack(pady=10)

root.geometry("300x200")
root.mainloop()