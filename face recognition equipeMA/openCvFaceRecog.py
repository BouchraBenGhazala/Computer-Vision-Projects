import cv2
import numpy as np
import face_recognition
from PIL import Image, ImageDraw


# Charger les images des personnes à reconnaître et leurs signatures
AKLY_image = face_recognition.load_image_file("C:\\Ensamc\\CI\\S4\\AI\\face recognition equipeMA\\images\\AKLY_Aya.jpeg")
AKLY_visage_signature = face_recognition.face_encodings(AKLY_image)[0]

ELGHAZOUANI_image = face_recognition.load_image_file("C:\\Ensamc\\CI\\S4\\AI\\face recognition equipeMA\\images\\amina_elghazouani.jpg")
ELGHAZOUANI_visage_signature = face_recognition.face_encodings(ELGHAZOUANI_image)[0]

# Ajoutez le chargement des autres visages et signatures ici
#BERRABEH Anass
BERRABEH_image = face_recognition.load_image_file("C:\\Ensamc\\CI\\S4\\AI\\face recognition equipeMA\\images\\Anass_Berrabeh.jpeg")
BERRABEH_visage_signature = face_recognition.face_encodings(BERRABEH_image)[0]

#ASSEl Mouhssin
ASSEL_image = face_recognition.load_image_file("C:\\Ensamc\\CI\\S4\\AI\\face recognition equipeMA\\images\\Assel_Mohssin.png")
ASSEL_visage_signature = face_recognition.face_encodings(ASSEL_image)[0]

#BAHAFID Oumaima
BAHAFID_image = face_recognition.load_image_file("C:\\Ensamc\\CI\\S4\\AI\\face recognition equipeMA\\images\\Bahafid_Oumaima.jpeg")
BAHAFID_visage_signature = face_recognition.face_encodings(BAHAFID_image)[0]

#ELMOUHI Yassine
ELMOUHI_image = face_recognition.load_image_file("C:\\Ensamc\\CI\\S4\\AI\\face recognition equipeMA\\images\\ELMOUHI_Yassine.jpeg")
ELMOUHI_visage_signature = face_recognition.face_encodings(ELMOUHI_image)[0]

#RAIS Ilias
RAIS_image = face_recognition.load_image_file("C:\\Ensamc\\CI\\S4\\AI\\face recognition equipeMA\\images\\ILIAS_RAIS.jpg")
RAIS_visage_signature = face_recognition.face_encodings(RAIS_image)[0]

#IZRAL Ahmed
IZRAL_image = face_recognition.load_image_file("C:\\Ensamc\\CI\\S4\\AI\\face recognition equipeMA\\images\\IZRAL AHMED.jpg")
IZRAL_visage_signature = face_recognition.face_encodings(IZRAL_image)[0]

#ZETATI Abdelhakim
ZETATI_image = face_recognition.load_image_file("C:\\Ensamc\\CI\\S4\\AI\\face recognition equipeMA\\images\\ZETATI_Abdelhakim.jpg")
ZETATI_visage_signature = face_recognition.face_encodings(ZETATI_image)[0]

#BENGHAZALA Bouchra
BENGHAZALA_image = face_recognition.load_image_file("C:\\Ensamc\\CI\\S4\\AI\\face recognition equipeMA\\images\\Bouchra_BENGHAZALA.jpg")
BENGHAZALA_visage_signature = face_recognition.face_encodings(BENGHAZALA_image)[0]

# Créer des listes de visages reconnus et de noms associés
reconnu_visage_signatures = [AKLY_visage_signature, ELGHAZOUANI_visage_signature,BERRABEH_visage_signature,ASSEL_visage_signature,BAHAFID_visage_signature,ELMOUHI_visage_signature,RAIS_visage_signature,IZRAL_visage_signature,ZETATI_visage_signature,BENGHAZALA_visage_signature]
reconnu_visage_noms = ["AKLY Aya", "ELGHAZOUANI Amina","BERRABEH Anass","ASSEl Mouhssin","BAHAFID Oumaima","ELMOUHI Yassine","RAIS Ilias","IZRAL Ahmed","ZETATI Abdelhakim","BENGHAZALA Bouchra"]


# Capture de la vidéo à partir de la caméra
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    small_frame=cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame=np.ascontiguousarray(small_frame[:,:,::-1])

    visage_locations = face_recognition.face_locations(rgb_small_frame) 
    visage_encodings=face_recognition.face_encodings(rgb_small_frame,visage_locations)

    print("Visage Locations:", visage_locations)  # Ajoutez cette ligne pour déboguer


    for visage_encoding in visage_encodings:
        matches=face_recognition.compare_faces(reconnu_visage_signatures,visage_encoding)
        nom_personne="Non reconnu"

        if True in matches:
            first_match_index=matches.index(True)
            nom_personne=reconnu_visage_noms[first_match_index]
        
        print("Nom de la personne:",nom_personne)



    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
