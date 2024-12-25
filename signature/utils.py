import cv2

def verify_signature(original_image_path, uploaded_image_path):
    original_image = cv2.imread(original_image_path, cv2.IMREAD_GRAYSCALE)
    uploaded_image = cv2.imread(uploaded_image_path, cv2.IMREAD_GRAYSCALE)

    uploaded_image = cv2.resize(uploaded_image, (original_image.shape[1], original_image.shape[0]))

    original_histogram = cv2.calcHist([original_image], [0], None, [256], [0, 256])
    uploaded_histogram = cv2.calcHist([uploaded_image], [0], None, [256], [0, 256])

    original_histogram = cv2.normalize(original_histogram, original_histogram).flatten()
    uploaded_histogram = cv2.normalize(uploaded_histogram, uploaded_histogram).flatten()

    similarity_score = cv2.compareHist(original_histogram, uploaded_histogram, cv2.HISTCMP_CORREL)

    return similarity_score > 0.8
