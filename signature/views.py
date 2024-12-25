from django.shortcuts import render
from django.http import JsonResponse
from .models import Signature
from .utils import verify_signature

def upload_signature(request):
    if request.method == 'POST' and request.FILES:
        original_image = request.FILES['original_image']
        uploaded_signature = request.FILES['uploaded_signature']

        signature = Signature.objects.create(
            original_image=original_image,
            uploaded_signature=uploaded_signature
        )

        result = verify_signature(
            signature.original_image.path,
            signature.uploaded_signature.path
        )

        return JsonResponse({
            'status': 'success',
            'verification_result': 'Match' if result else 'Mismatch'
        })

    return render(request, 'signature/upload.html')
