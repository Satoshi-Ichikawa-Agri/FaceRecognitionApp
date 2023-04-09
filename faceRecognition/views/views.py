from django.shortcuts import render
import cv2 # OpenCV
import numpy as np

from faceRecognition.models.models import UploadImages, DetectResult
from .image_recognition import image_save, convert_gray, detect


def get_cascade_file():
    """ カスケードファイルを取得する
    """
    cascade_file = 'C:/Users/daiko/Develop_satoshi/FaceRecognitionApp/static/cascade/cascade.xml'
    return cascade_file


def top(request):
    """ Top page
    """
    if request.method == 'POST':
        # 画面のアップロードファイルを取得
        upload_file = request.FILES.get('upload_file')

        # numpyarray型に変換
        file_ndArray = np.asarray(bytearray(upload_file.read()), dtype=np.uint8)
        file_ndArray_decode = cv2.imdecode(file_ndArray, cv2.IMREAD_COLOR)

        # オリジナル画像をDBに保存する
        original_file_path, create_image = image_save(file_ndArray_decode, upload_file)

        # グレースケール
        img_gray = convert_gray(file_ndArray_decode)

        # detect&rectangle
        cascade_file = get_cascade_file()
        result, count = detect(img_gray, cascade_file, original_file_path, create_image)
        
        detect_result = DetectResult.objects.all()

        return render(
            request,
            'result.html',
            context={
                'detect_result': detect_result,
                'count': count
                },
            )
    
    # GET
    return render(request, 'top.html')
