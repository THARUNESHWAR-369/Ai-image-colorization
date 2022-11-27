# Import flask Library
from flask import Flask
from flask import render_template, url_for, redirect, request

"""
Import From Packages
"""
from packages._variables import VARIABLES
from packages._utils import UTILS


# Initialize Flask app
app = Flask(__name__)

# Initialize Packages Liabries
variables = VARIABLES()
utils = UTILS()


app.secret_key = variables.SECRET_KEY

# Home route
@app.route('/', methods=["POST", "GET"])
def index():
    
    if request.method == "POST":
        print(request.files['color-img'])

        bw_img = request.files['color-img']

        # get file, name, fileExtensiion
        filename, name, file_extension = utils.getFilenameExtension(
            bwImageData=bw_img
        )

        # define filename
        bw_filename = f"techAI_image_colorization_{name}_{variables.SUFFIX_FILENAME}.{file_extension}"

        bw_img_buf = utils.imgToBuf(bw_img)
        
        __colored_successfully, __colored_buff_img = utils.startColor(bw_img_buf)
        
        print("__colored_successfully: ", __colored_successfully)
        
                
        if __colored_successfully:

                return {
                    "status":True,
                    "bw_img":utils.htmlFormat(bw_img_buf),
                    "colored_img":utils.htmlFormat(__colored_buff_img),
                    "filename":bw_filename
                }    
        
        
    return render_template('index.html', context={'status': 'false'})


# Run the app
if __name__ == '__main__':
    app.run(debug=True)