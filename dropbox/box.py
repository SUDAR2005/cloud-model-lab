import dropbox
# Replace with your Dropbox access token
#ACCESS_TOKEN = 'sl.B-7kJ5AV9FvCpgRxjB-09kwKuhgog-Z5Ki5I_Ws_UVn4-mft79Xble__Hs2o_v7BL36TfeQABKmX2Z_Vp29MVT0YhyyVWOU6OeOwPhekC4cxLtjBctI8xgjfg6dSNAxSuFvwICtNkrlInAJ4axcGMPE'
ACCESS_TOKEN ='Your_ACCESS_TOken'
# Function to upload a file to Dropbox
def upload_file(fp, dropboxpath):
    dbx = dropbox.Dropbox(ACCESS_TOKEN)
    with open(fp, 'rb') as f:
        dbx.files_upload(f.read(), dropboxpath)
    print("Uploaded")

# Function to list files in the Dropbox app folder
def list_files():
    dbx = dropbox.Dropbox(ACCESS_TOKEN)
    try:
        response = dbx.files_list_folder('')
        return [file.name for file in response.entries]
    except dropbox.exceptions.ApiError as e:
        print(f"Error: {e}")
        return []


upload_file('dropbox.txt', '/remote_file.txt')
print(list_files())