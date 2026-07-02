import streamlit as st
from pathlib import Path
import os

# --- Page Configuration ---
st.set_page_config(
    page_title="AI-Ready File Manager",
    page_icon="📁",
    layout="centered"
)

# --- Custom Styling for Premium Look ---
st.markdown("""
    <style>
    .main-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-title {
        font-size: 1.1rem;
        color: #555;
        text-align: center;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- UI Headers ---
st.markdown('<div class="main-title">📁 Core File Handling Engine</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">A clean, functional CRUD application built with Python & Streamlit</div>', unsafe_allow_html=True)
st.write("---")

# --- Tabs for Clean Organization ---
tab1, tab2, tab3, tab4 = st.tabs([
    "✨ Create File", 
    "📖 Read File", 
    "✍️ Append/Update", 
    "🗑️ Delete File"
])

# ==========================================
# TAB 1: CREATE FILE
# ==========================================
with tab1:
    st.subheader("Create a New Document")
    c_name = st.text_input("Enter file name (e.g., notes.txt)", key="create_name")
    c_content = st.text_area("Enter your file content", placeholder="Type something here...", key="create_content")
    
    if st.button("Create File", type="primary"):
        if not c_name:
            st.warning("⚠️ Please provide a valid file name.")
        elif Path(c_name).exists():
            st.error(f"❌ '{c_name}' already exists in this directory!")
        else:
            with open(c_name, 'w') as fs:
                fs.write(c_content)
            st.success(f"🎉 File '{c_name}' created successfully!")

# ==========================================
# TAB 2: READ FILE
# ==========================================
with tab2:
    st.subheader("Read Document Content")
    r_name = st.text_input("Enter file name to read", key="read_name")
    
    if st.button("Read File"):
        if not r_name:
            st.warning("⚠️ Please enter a file name.")
        elif Path(r_name).exists():
            with open(r_name, 'r') as fs:
                content = fs.read()
            st.info(f"📄 **Showing contents of {r_name}:**")
            st.code(content if content else "[Empty File]")
        else:
            st.error("❌ The specified file does not exist!")

# ==========================================
# TAB 3: UPDATE / APPEND FILE
# ==========================================
with tab3:
    st.subheader("Append Data to File")
    u_name = st.text_input("Enter file name to update", key="update_name")
    u_content = st.text_area("Enter data to append", placeholder="This text will be added to the end of the file...", key="update_content")
    
    if st.button("Update File"):
        if not u_name:
            st.warning("⚠️ Please enter a file name.")
        elif Path(u_name).exists():
            with open(u_name, 'a') as fs:
                fs.write("\n" + u_content) # Adds a clean new line before appending
            st.success(f"✅ Data added to '{u_name}' successfully!")
        else:
            st.error("❌ The specified file does not exist!")

# ==========================================
# TAB 4: DELETE FILE
# ==========================================
with tab4:
    st.subheader("Delete Document")
    st.markdown("<p style='color:red;'>⚠️ <b>Warning:</b> This action is permanent and cannot be undone.</p>", unsafe_allow_html=True)
    d_name = st.text_input("Enter file name to delete", key="delete_name")
    
    if st.button("Delete File", type="secondary"):
        if not d_name:
            st.warning("⚠️ Please enter a file name.")
        elif Path(d_name).exists():
            os.remove(d_name)
            st.success(f"🗑️ File '{d_name}' was securely deleted from disk.")
        else:
            st.error("❌ The specified file does not exist!")

# --- Sidebar Info Panel ---
with st.sidebar:
    st.header("Project Insights")
    st.markdown("""
    **Core Technologies Used:**
    *   **Python Engine:** Built utilizing native File I/O procedures.
    *   **Path Validation:** Powered by `pathlib` for secure file-system checking.
    *   **UI Layer:** Handled entirely by Streamlit components.
    
    *Developed as part of a pre-college software foundations sprint.*
    """)