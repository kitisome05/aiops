import streamlit as st

st.set_page_config(page_title="Mi App en Azure", page_icon="🚀")

st.title("🚀 ¡Bienvenido a mi App en Azure con Streamlit!")
st.write("Esta es una aplicación de prueba desplegada en Azure App Service usando Terraform.")

st.sidebar.header("Menú")
option = st.sidebar.selectbox("Selecciona una opción", ["Inicio", "Acerca de"])

if option == "Inicio":
    st.subheader("🌍 Página de Inicio")
    st.write("Aquí puedes mostrar contenido dinámico.")
    nombre = st.text_input("¿Cómo te llamas?", "")
    if nombre:
        st.write(f"¡Hola, {nombre}! Bienvenido a la app. 🎉")

elif option == "Acerca de":
    st.subheader("ℹ️ Acerca de")
    st.write("Esta aplicación fue desplegada en Azure usando GitHub Actions y Terraform.")