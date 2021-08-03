from yolov5.detect import Detect

detector = Detect()
results = detector.detect()
labels = [[float(num) for num in line.split()] for line in results]
for label in labels:
    print(label)
