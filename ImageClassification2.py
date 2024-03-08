import numpy as np
import time
import cv2



image_path = "C:\\Users\\ASUS\\Desktop\\truck.jpg"
label_path = "C:\\Users\\ASUS\\Desktop\\imagenet_labels.txt"
prototxt_path = "C:\\Users\\ASUS\\Desktop\\googlenet.prototxt"
model_path = "C:\\Users\\ASUS\\Desktop\\googlenet.caffemodel"

image = cv2.imread(image_path)
rows = open(label_path).read().strip().split("\n")
classes = [r.split(",")[0] for r in rows]


blob = cv2.dnn.blobFromImage(image, 1, (224, 224), (104, 117, 123))

print("Loading model...")
net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

net.setInput(blob)
start = time.time()
preds = net.forward()
end = time.time()
print("Classification time: {:.5} seconds".format(end - start))


idxs = np.argsort(preds[0])[::-1][:5]

for (i, idx) in enumerate(idxs):
      if i == 0:
          text = "Label: {}, {:.2f}%".format(classes[idx], preds[0][idx] * 100)
          cv2.putText(image, text, (5, 25),  cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
          print("{}.  label:  {},  probability:  {:.5}".format(i  +  1,  classes[idx], preds[0][idx]))


cv2.imshow("Frame", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
