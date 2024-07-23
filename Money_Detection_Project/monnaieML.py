import cv2
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# Fonction pour extraire les caractéristiques et les étiquettes à partir d'une image
def extract_features_and_labels(image_path, label):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_blurred = cv2.GaussianBlur(gray, (9, 9), 0)
    circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=50,
                           param1=120, param2=40, minRadius=50, maxRadius=300)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        features = circles[:, 2].reshape(-1, 1)
        labels = np.full((len(circles),), label)  # Assigner la même étiquette à toutes les pièces de cette classe
        return features, labels
    else:
        return None, None

# Liste des chemins d'accès aux images pour chaque classe #Money_Detection_Project\pieces10DH\10dh(1).png
image_paths_5dh = ['pieces5DH/5dh(1).png', "pieces5DH/5dh(2).png", "pieces5DH/5dh(4).png","pieces5DH/5dh(5).png","pieces5DH/5dh(6).png"]  # Ajoutez tous les chemins d'accès nécessaires
image_paths_10dh = ["pieces10DH/10dh(1).png", "pieces10DH/10dh(2).png","pieces10DH/10dh(4).png","pieces10DH/10dh(5).png","pieces10DH/10dh(6).png" ] # Ajoutez tous les chemins d'accès nécessaires
#Money_Detection_Project\pieces5DH\5dh(1).png
# Initialisez des listes pour stocker les caractéristiques et les étiquettes de chaque classe
all_features = []
all_labels = []

# Extraire les caractéristiques et les étiquettes pour les pièces de 5 DH
for image_path in image_paths_5dh:
    features, labels = extract_features_and_labels(image_path, label=0)  # Assigner l'étiquette 0 pour les pièces de 5 DH
    if features is not None:
        all_features.append(features)
        all_labels.append(labels)

# Extraire les caractéristiques et les étiquettes pour les pièces de 10 DH
for image_path in image_paths_10dh:
    features, labels = extract_features_and_labels(image_path, label=1)  # Assigner l'étiquette 1 pour les pièces de 10 DH
    if features is not None:
        all_features.append(features)
        all_labels.append(labels)

# Concaténer toutes les caractéristiques et étiquettes pour former l'ensemble de données d'entraînement
X_train = np.concatenate(all_features)  
y_train = np.concatenate(all_labels)  

# Entraîner le modèle KNN
knn_classifier = KNeighborsClassifier(n_neighbors=1)  
knn_classifier.fit(X_train, y_train)

# Charger une nouvelle image à prédire  
image_test = cv2.imread('test/1.jpg') 
gray_test = cv2.cvtColor(image_test, cv2.COLOR_BGR2GRAY)
gray_blurred_test = cv2.GaussianBlur(gray_test, (9, 9), 0)

# Détecter les cercles avec HoughCircles pour l'image de test
circles_test = cv2.HoughCircles(gray_blurred_test, cv2.HOUGH_GRADIENT, dp=1, minDist=50,
                           param1=120, param2=40, minRadius=50, maxRadius=300)

# Assurer qu'au moins un cercle a été trouvé
if circles_test is not None:
    # Convertir les coordonnées et les rayons des cercles en entiers
    circles_test = np.round(circles_test[0, :]).astype("int")
    features_test = circles_test[:, 2].reshape(-1, 1)  # Extraire les rayons comme caractéristiques 
    print("circles test ",circles_test)
    # Prédire les étiquettes de classe pour les cercles détectés dans l'image de test
    predicted_labels_test = knn_classifier.predict(features_test)
    print("predicted_labels_test: ",predicted_labels_test)

    # Assigner les étiquettes prédites aux cercles détectés dans l'image de test et afficher les résultats
    for i, (x, y, r) in enumerate(circles_test):
        if predicted_labels_test[i] == 0:
            cv2.circle(image_test, (x, y), r, (0, 255, 0), 4)  # Pièce de 5DH
            cv2.circle(image_test, (x, y), 1, (0, 0, 255), 4)
            cv2.putText(image_test, "5DH", (x, y+50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            print("Pièce de test 5DH détectée")
        else:
            cv2.circle(image_test, (x, y), r, (255, 0, 0), 4)  # Pièce de 10DH
            cv2.circle(image_test, (x, y), 1, (0, 0, 255), 4)
            cv2.putText(image_test, "10DH", (x, y+50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            print("Pièce de test 10DH détectée")

    # Afficher l'image de test avec les cercles détectés et classifiés
    cv2.imshow("Circles Detected and Classified - Test Image", image_test)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Aucun cercle n'a été détecté dans l'image de test.")
