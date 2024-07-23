from ultralytics import YOLO 

model = YOLO('yolov8x')
result=model.predict('input_videos/input_video.mp4',save=True)
print("result is: \n",result)

#print("result 0 is ",result[0])

print("boxes are")

for box in result[0].boxes:
    print("box:",box)
