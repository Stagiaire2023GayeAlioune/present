import streamlit as st
import os

# Définir les répertoires où les fichiers seront sauvegardés
PHOTO_DIR = "uploaded_photos"
VIDEO_DIR = "uploaded_videos"

# Créer les répertoires s'ils n'existent pas
os.makedirs(PHOTO_DIR, exist_ok=True)
os.makedirs(VIDEO_DIR, exist_ok=True)

# Charger le fichier CSS
#with open("style.css") as f:
 #   st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Titre de l'application
st.title("Application de sauvegarde de photos et de vidéos de Rafik 'say say'")
st.subheader("Téléchargez vos photos et vidéos")

# Téléchargement de fichiers
uploaded_files = st.file_uploader("Choisissez des fichiers", type=["jpg", "jpeg", "png", "mp4", "mov"], accept_multiple_files=True)

# Sauvegarder les fichiers téléchargés
if uploaded_files:
    for uploaded_file in uploaded_files:
        if uploaded_file.type.startswith("image"):
            file_path = os.path.join(PHOTO_DIR, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success(f"Photo sauvegardée : {uploaded_file.name}")
        elif uploaded_file.type.startswith("video"):
            file_path = os.path.join(VIDEO_DIR, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success(f"Vidéo sauvegardée : {uploaded_file.name}")

# Options de sélection dans la barre latérale
option = st.sidebar.selectbox("Choisissez ce que vous voulez voir", ("Photos sauvegardées", "Vidéos sauvegardées"))
st.sidebar.image("raf.jpg")
def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        return True
    return False

if option == "Photos sauvegardées":
    st.subheader("Photos sauvegardées")
    saved_photos = os.listdir(PHOTO_DIR)
    if saved_photos:
        photos_to_delete = st.multiselect("Sélectionnez les photos à supprimer", saved_photos)
        if st.button("Supprimer les photos sélectionnées"):
            for photo_name in photos_to_delete:
                file_path = os.path.join(PHOTO_DIR, photo_name)
                if delete_file(file_path):
                    st.success(f"Photo supprimée : {photo_name}")
                else:
                    st.error(f"Erreur lors de la suppression de la photo : {photo_name}")
        for photo_name in saved_photos:
            st.image(os.path.join(PHOTO_DIR, photo_name))
    else:
        st.write("Aucune photo sauvegardée.")
elif option == "Vidéos sauvegardées":
    st.subheader("Vidéos sauvegardées")
    saved_videos = os.listdir(VIDEO_DIR)
    if saved_videos:
        videos_to_delete = st.multiselect("Sélectionnez les vidéos à supprimer", saved_videos)
        if st.button("Supprimer les vidéos sélectionnées"):
            for video_name in videos_to_delete:
                file_path = os.path.join(VIDEO_DIR, video_name)
                if delete_file(file_path):
                    st.success(f"Vidéo supprimée : {video_name}")
                else:
                    st.error(f"Erreur lors de la suppression de la vidéo : {video_name}")
        for video_name in saved_videos:
            st.video(os.path.join(VIDEO_DIR, video_name))
            st.write(video_name)  # Affiche le nom de la vidéo
    else:
        st.write("Aucune vidéo sauvegardée.")