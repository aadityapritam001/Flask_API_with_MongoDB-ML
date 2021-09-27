# from database import db
# from ml.main import extract_data
# import json

# def view(file_names):
#     all_files=[]
#     for file in file_names:
#         path = 'uploads/' + file
#         ml_output=json.dumps(extract_data(path))
#         all_files.append({'path':file,'content':ml_output})

#     db.fileupload(all_files)
#     return None
