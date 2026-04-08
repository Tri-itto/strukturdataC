import streamlit as st
from collections import deque

st.set_page_config(page_title="Antrian Pasien", layout="centered")
st.title("🏥 Antrian Pasien (Circular Queue)")
st.caption("FIFO + kapasitas terbatas")

# Kapasitas
capacity = st.slider("Kapasitas", 3, 8, 5)

# Init queue
if "queue" not in st.session_state:
    st.session_state.queue = deque(maxlen=capacity)

# Reset kalau kapasitas berubah
if st.session_state.queue.maxlen != capacity:
    st.session_state.queue = deque(list(st.session_state.queue), maxlen=capacity)

# Input
nama = st.text_input("Nama pasien")
col1, col2 = st.columns(2)

# Enqueue
with col1:
    if st.button("➕ Datang"):
        if nama:
            if len(st.session_state.queue) < capacity:
                st.session_state.queue.append(nama)
            else:
                st.warning("Penuh!")
        else:
            st.warning("Isi nama!")

# Dequeue
with col2:
    if st.button("👨‍⚕️ Layani"):
        if st.session_state.queue:
            st.session_state.queue.popleft()
        else:
            st.warning("Kosong!")

# ---------------- VISUAL ---------------- #

st.subheader("📊 Antrian")

queue_list = list(st.session_state.queue)
cols = st.columns(capacity)

for i in range(capacity):
    with cols[i]:
        if i < len(queue_list):
            text = queue_list[i]

            if i == 0:
                st.markdown(f"🟢 **{text}**\n\n(FRONT)")
            elif i == len(queue_list) - 1:
                st.markdown(f"🔵 **{text}**\n\n(REAR)")
            else:
                st.markdown(f"⚪ {text}")
        else:
            st.markdown("⬜")

# Info
st.write("---")

if queue_list:
    st.success(f"Next: {queue_list[0]}")
    st.info(f"Total: {len(queue_list)}/{capacity}")
else:
    st.info("Antrian kosong")