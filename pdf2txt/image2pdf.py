def routine_00():
    print("routine_00 -- image 2 pdf")
    from PIL import Image
    from img2pdf import convert
    import matplotlib.pyplot as plt
    im_org = Image.open(r"D:\Informations\articles\test3.jpg")

    plt.imshow(im_org)
    plt.title("original image")
    # plt.show()

    # im = im_org.resize([200,200]) # scale image
    im = im_org.crop([20,20,220,220])
    im_org.close()

    plt.imshow(im)
    plt.title("crop image")
    # plt.show()

    if False: # use raw process method
        pixels = im.load()
        for i in range(200):
            for j in range(200):
                pixels[i, j] = (0,0,0) if pixels[i, j] < (100,100,100) else (255,255,255)
    else: # use eval, should assign back to im
        if False: # use self-increased value for test
            global val
            val = 0
            def getval():
                global val
                val += 1
                return val-1
            im = Image.eval(im, lambda a : getval() if a < 100 else 255)
        else: # hist graph image split
            im = Image.eval(im, lambda a : 0 if a < 100 else 255)

    plt.imshow(im)
    plt.title("fixed image")
    # plt.show()

    with open("test_img.jpg", "wb") as f:
        im.save(f, format="jpeg")

    with open("test_img.pdf", "wb") as f:
        convert("test_img.jpg", outputstream=f)

    print("all good")


def routine_01():
    print("routine_01 -- image 2 txt")
    from PIL import Image
    import pytesseract

    pytesseract.pytesseract.tesseract_cmd = r'E:\Program_files\Tesseract-OCR\tesseract.exe'

    im = Image.open("test.png")
    # text = pytesseract.image_to_string(im)
    text = pytesseract.image_to_string(im, lang='chi_sim')
    im.close()
    print("result :")
    print(text)


def routine_02():
    print("routine_02 -- image 2 pdf")
    from img2pdf import convert
    with open("test.pdf", "wb") as f:
        convert("test.png", outputstream=f)


def routine_03():
    print("routine_03 -- pdf2txt")
    import os
    r = os.popen("pipenv run pdf2txt test.pdf")
    # r = os.popen("pipenv run python --help")
    print("result :")
    print(r.read())


def routine_04():
    print("routine_03 -- pdf2image")
    from pdf2image import convert_from_path, convert_from_bytes
    import matplotlib.pyplot as plt
    import sys
    print("sys path = {}".format(sys.path))

    images = convert_from_path('test1.pdf')
    # images = convert_from_bytes(open('/home/belval/example.pdf', 'rb').read())
    plt.imshow(images[0])
    plt.title("from pdf")
    plt.show()

def routine_05():
    print("routine_03 -- pdf to txt")
    from pdf2image import convert_from_path, convert_from_bytes
    import pytesseract

    pytesseract.pytesseract.tesseract_cmd = r'E:\Program_files\Tesseract-OCR\tesseract.exe'

    images = convert_from_path('crime.pdf')
    for i in range(10,11):
        im = images[i]
        with open("tmp.jpg", "wb") as f:
            im.save(f, format="jpeg")
        text = pytesseract.image_to_string(im, lang='chi_sim')
        print(text)


def convert_pdf_to_txt(path_to_pdf, path_to_txt, with_chinese):
    print("")
    print("convert_pdf_to_txt :")
    print("  from    : {}".format(path_to_pdf))
    print("  to      : {}".format(path_to_txt))
    print("  chinese : {}".format(with_chinese))
    from pdf2image import convert_from_path
    import os
    import pytesseract
    pytesseract.pytesseract.tesseract_cmd = r'E:\Program_files\Tesseract-OCR\tesseract.exe'

    language = 'eng' if not with_chinese else 'chi_sim'
    images = convert_from_path(path_to_pdf)
    with open(path_to_txt, "wb") as ft:
        for i in range(len(images)):
            try:
                im = images[i]
                text = pytesseract.image_to_string(im, lang=language)
                ft.write((text + '\n').encode('utf-8'))
                # print(text)
            except Exception as err:
                print("failed for page {}, info : {}".format(i, err))


def shell_entry():
    print("image2pdf shell_entry :", end=" ", flush=True)
    convert_pdf_to_txt("crime.pdf", "crime.txt", True)