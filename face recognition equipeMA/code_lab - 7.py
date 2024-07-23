import face_recognition
from PIL import Image, ImageDraw

#
# Ce programme est un exemple de reconnaissance de visage
# avec encadrement est reconnaissance sur l'image du nom du personnage 

# charger l'image de la personne est apprendre au système a la reconnaitre  .
#AKLY Aya
AKLY_image = face_recognition.load_image_file("C:\\Ensamc\\CI\\S4\\AI\\face recognition equipeMA\\images\\AKLY_Aya.jpeg")
AKLY_visage_signature = face_recognition.face_encodings(AKLY_image)[0]

#ELGHAZOUANI Amina
ELGHAZOUANI_image = face_recognition.load_image_file("C:\\Ensamc\\CI\\S4\\AI\\face recognition equipeMA\\images\\amina_elghazouani.jpg")
ELGHAZOUANI_visage_signature = face_recognition.face_encodings(ELGHAZOUANI_image)[0]

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

# creer un tableau des signature des visages associés au nom de personnes
reconnu_visage_signatures = [
    AKLY_visage_signature,
    ELGHAZOUANI_visage_signature,
    BERRABEH_visage_signature,
    ASSEL_visage_signature,
    BAHAFID_visage_signature,
    ELMOUHI_visage_signature,
    RAIS_visage_signature,
    IZRAL_visage_signature,
    ZETATI_visage_signature,
    BENGHAZALA_visage_signature
]
reconnu_visage_noms = [
    "AKLY Aya",
    "ELGHAZOUANI Amina",
    "BERRABEH Anass",
    "ASSEl Mouhssin",
    "BAHAFID Oumaima",
    "ELMOUHI Yassine",
    "RAIS Ilias",
    "IZRAL Ahmed",
    "ZETATI Abdelhakim"
    "BENGHAZALA Bouchra",

]

# Charger l'image avec les visages non reconnus
non_reconnu_image = face_recognition.load_image_file("C:\\Ensamc\\CI\\S4\\AI\\face recognition equipeMA\\equipeBoys.jpg")

# trouver tout les visages et leurs signature dans une image source 
visage_locations = face_recognition.face_locations(non_reconnu_image)
visage_signatures = face_recognition.face_encodings(non_reconnu_image, visage_locations)

# convertire l'image en PIL-format pour qu'on puisse dessiner avec la librairie pillow  
# regarder http://pillow.readthedocs.io/ pour plus d'informations sur PIL/Pillow
pil_image = Image.fromarray(non_reconnu_image)
# creer une image ou nous allons faire des dessin sous format d'instance de Pillow ImageDraw 
img_dessin=ImageDraw.Draw(pil_image)
# boucler sur les visage trouver dans l'image à reconnaite
for (top, right, bottom, left), visage_signature in zip(visage_locations, visage_signatures):
    # voir si le visage extrait correspond a un(des) visage(s) reconnu(s)
    matches = face_recognition.compare_faces(reconnu_visage_signatures, visage_signature)

    nom_personne = "non_reconnu"

    # Si une correspondance est retrouvé dans les reconne_visage_signatures, seulement prendre le premier!
    if True in matches:
        first_match_index = matches.index(True)
        nom_personne = reconnu_visage_noms[first_match_index]

    # dessiner un rectangle autour du visage utilisant les modules de pillow
    img_dessin.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

    # dessiner un label avec le text du nom de visage reconnus
    #text_width= img_dessin.textlength(nom_personne)  # Ajoutez également la police si nécessaire
    img_dessin.rectangle(((left, bottom ), (right, bottom)), fill=(0, 255, 0), outline=(0, 0, 255))
    img_dessin.text((left + 10, bottom ), nom_personne, fill=(255, 0, 0, 255))


# supprimer la library de dessin de la  memoire
del img_dessin

# afficher l'image resultant
pil_image.show()

pil_image.save("D:\\cours 2022\\ENSAM\\Cours IAGI 2 Intelligence Artificielle\\Labs\\Lab 2 - Vision intélligentes via OpenCV\\work\\Lab 8\\image_avec_detection.jpg")
