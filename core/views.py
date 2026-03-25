from django.shortcuts import render
from .services.gemini_service import GeminiService

import base64

def ocr_view(request):
    result = None
    image_base64 = None
    file_type = "image"

    if request.method == 'POST' and request.FILES.get('image'):


        image_file = request.FILES['image']
        image_data = image_file.read()

        image_base64 = base64.b64encode(image_data).decode('utf-8')
        image_file.seek(0)

        service = GeminiService()
        result = service.execute(request.FILES[file_type])

    return render(request, 'ocr/index.html', {
        'result': result,
        'image_base64': image_base64
    })
