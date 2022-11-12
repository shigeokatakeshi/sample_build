from flask import Flask
from flask import render_template
from flask import request
from PIL import Image

import pyocr

app = Flask(__name__)


# print(tool)
# print(tool.get_name())

# img = Image.open("uploadFile") # pillowで画像をオープンして保存
# img.show()

# txt = tool.image_to_string(img, lang="eng+jpn", builder=pyocr.builders.TextBuilder())

# print(txt)


@app.route("/")
def index():
    return render_template("index.html")


# methodはhtml分で指定しないとGETになる


@app.route("/upload", methods=["POST"])
def upload():
    # リクエストファイルの読込
    ocr_file = request.files["ocrFile"]
    img = Image.open(ocr_file)
    # OCR準備
    tools = pyocr.get_available_tools()
    tool = tools[0]
    # OCR
    txt = tool.image_to_string(
        img, lang="eng+jpn", builder=pyocr.builders.TextBuilder()
    )
    print(txt)
  #  return render_template("index.html")

    if txt == "":
        txt = "読込エラー"

    return render_template("index.html", txt=txt)


if __name__ == "__main__":
    app.run(debug=True)
