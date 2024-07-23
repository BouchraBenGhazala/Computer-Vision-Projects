import numpy as np
import cv2

# Create a black image
ca = np.zeros((400, 700, 3), dtype=np.uint8)
ca[:]=(240,240,240) 

# Draw a filled red rectangle
start_point = (300, 100)
end_point = (670, 280)
color = (149, 86, 27)  # Blue color in BGR #27,86,149,255
color_gris=(220,220,220)
thickness = cv2.FILLED
logo = cv2.rectangle(ca, (30, 90), (260, 280), (255,255,255), thickness) #rectangle blanc
logo = cv2.rectangle(ca, (270, 90), (290, 280), color, thickness) #rectangle bleu milieu
logo = cv2.rectangle(ca, (300, 90), (670, 280), color, thickness)  #rectangle bleu de ensam
logo = cv2.rectangle(ca, (65, 230), (95, 231), color_gris, thickness) #middle H
logo = cv2.rectangle(ca, (50, 195), (55, 265), color_gris, cv2.LINE_4) #left H
logo = cv2.rectangle(ca, (105, 195), (110, 265), color_gris, cv2.LINE_4) #right H
cv2.ellipse(ca,(105,192),(4,4),340,0,140,color_gris  ,3,cv2.LINE_8) #left H #(255,255,255) 
cv2.ellipse(ca,(54,192),(4,4),60,0,140,color_gris  ,3,cv2.LINE_8) #right H #(255,255,255) 
logo = cv2.rectangle(ca, (38, 260), (120, 270), color_gris, cv2.FILLED) #down H
logo = cv2.rectangle(ca, (65, 260), (95, 270), (255,255,255), cv2.FILLED) #down middle H

cv2.ellipse(ca,(36,257),(8,8),320,0,140,(255,255,255),6,cv2.LINE_8) #left bottom left H #(255,255,255) 
cv2.ellipse(ca,(68,257),(8,8),60,0,140,(255,255,255),6,cv2.LINE_8) #right bottom left H #(255,255,255) 

cv2.ellipse(ca,(91,257),(8,8),320,0,140,(255,255,255),6,cv2.LINE_8) #left bottom right H #(255,255,255) 
cv2.ellipse(ca,(125,257),(8,8),60,0,140,(255,255,255),6,cv2.LINE_8) #right bottom right H #(255,255,255) 

#University logo
cv2.ellipse(ca,(80,160),(30,30),350,0,200,color,8,cv2.LINE_8) ,
logo = cv2.rectangle(ca, (48, 120), (52, 160), color, cv2.LINE_4)  #left U
logo = cv2.rectangle(ca, (108, 120), (113, 160), color, cv2.LINE_4) #right U
logo = cv2.rectangle(ca, (140, 110), (145, 270), color_gris, cv2.LINE_4) #vertical 1
logo = cv2.rectangle(ca, (160, 110), (165, 270), color_gris, cv2.LINE_4) #vertical 2

logo = cv2.rectangle(ca, (184, 111), (186, 136), color, cv2.FILLED) #vertical z
logo = cv2.rectangle(ca, (186, 111), (240, 126), color, cv2.FILLED) #horizontal z
cv2.ellipse(ca,(240, 128),(10,10),240,0,140,color,13,cv2.LINE_8) #ellipse z
logo = cv2.rectangle(ca, (220, 135), (256, 150), color, cv2.FILLED) #horizontal 2 z
cv2.ellipse(ca,(218, 166),(24,24),150,20,140,color,13,cv2.LINE_8) #ellipse 2 z



logo = cv2.rectangle(ca, (32, 110), (130, 120), color, cv2.FILLED) #up U
cv2.ellipse(ca,(80,133),(17,17),190,0,160,(255,255,255)  ,18,cv2.LINE_8) #Milieu U #(255,255,255) 
cv2.ellipse(ca,(31,126),(9,9),280,0,140,(255,255,255)  ,12,cv2.LINE_8) #left U #(255,255,255) 
cv2.ellipse(ca,(130,126),(9,9),120,0,140,(255,255,255)  ,12,cv2.LINE_8) #right U #(255,255,255) 

# Write letters inside the rectangle
font = cv2.FONT_HERSHEY_SIMPLEX
letter1 = 'E'
letter2 = 'N'
letter3 = 'S'
letter4 = 'A'
letter5 = 'M'
org1 = (320, 220)
org2 = (380, 220)
org3 = (450,220)
org4 = (520, 220)
org5 = (580, 220)
font_scale = 3
font_color = (240, 240, 240)  # White color in BGR
line_thickness = 12
logo = cv2.putText(logo, letter1, org1, font, font_scale, font_color, line_thickness)
logo = cv2.putText(logo, letter2, org2, font, font_scale, font_color, line_thickness)
logo = cv2.putText(logo, letter3, org3, font, font_scale, font_color, line_thickness)
logo = cv2.putText(logo, letter4, org4, font, font_scale, font_color, line_thickness)
logo = cv2.putText(logo, letter5, org5, font, font_scale, font_color, line_thickness)

#Text
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
text1 = 'ECOLE NATIONALE SUPERIEURE D\'ARTS ET METIERS'
text2= 'UNIVERSITE HASSAN II DE CASABLANCA'
org1 = (30, 310)
org2 = (90, 330)
font_scale = 1  # Adjust the font scale to make the text smaller
font_color = (0, 0, 0)  # White color in BGR
line_thickness = 1
logo=cv2.putText(logo, text1, org1, font, font_scale, font_color, line_thickness)
logo=cv2.putText(logo, text2, org2, font, font_scale, font_color, line_thickness)

# Display the image
cv2.imshow('Logo Ensam', logo)
cv2.waitKey(0)
cv2.destroyAllWindows()
