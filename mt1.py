import cv2
import pycda
input_name='NAC_DTM_APOLLO12_M120012135_2M.TIF'
img = cv2.imread(input_name)
cda=pycda.CDA()
detections=cda.predict(img)
print(detections.head(10))
predictions=cda.get_prediction(img)
predictions.show()

