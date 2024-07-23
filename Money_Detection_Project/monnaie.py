import cv2
import numpy as np

# Charger l'image
image = cv2.imread('pieces5DH/5dh(1).png') #3!!
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_blurred = cv2.GaussianBlur(gray, (9, 9), 0)

# Détecter les cercles avec HoughCircles
circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=50,
                           param1=120, param2=40, minRadius=50, maxRadius=300)

# Assurer qu'au moins un cercle a été trouvé
if circles is not None:
    # Convertir les coordonnées et les rayons des cercles en entiers
    circles = np.round(circles[0, :]).astype("int")

    # Boucle sur les cercles détectés
    for (x, y, r) in circles:
        # Dessiner le cercle détecté
        cv2.circle(image, (x, y), r, (0, 255, 0), 4)
        # Dessiner le centre du cercle
        cv2.circle(image, (x, y), 1, (0, 0, 255), 4)
        print(circles)
        if(circles[0][2] <110):
            print("5DH")
            cv2.putText(image, "5DH", (x, y+50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        else:
            print("10DH")
            cv2.putText(image, "10DH", (x, y+50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    # Afficher l'image avec les cercles détectés
    cv2.imshow("Circles Detected", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Aucun cercle n'a été détecté.")

