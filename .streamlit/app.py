import streamlit as st

# --- CẤU HÌNH TRANG ---
st.set_page_config(
    page_title="Bui Xuan Tung | Career Storybook",
    page_icon="🎥",
    layout="wide"
)

# --- CSS TÙY CHỈNH ---
st.markdown("""
<style>
    h1, h2, h3 { color: #D4AF37 !important; font-family: 'serif'; }
    p, li, span, div { color: #e0e0e0; font-size: 16px; }
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR (CỘT TRÁI) ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/imTuung20104/imTuung20104.github.io/f0ff9cbbe9fc6759195b0b4ceb1ddea3f6d8e7e8/my_avatar.JPG", width=150)
    st.title("BÙI XUÂN TÙNG")
    st.caption("📍 Hanoi, Vietnam")
    st.info("Logistics Specialist | Visual Creator")
    st.write("---")
    st.write("📧 tungbx15.lsc@gmail.com")
    st.write("🔗 [LinkedIn Profile](#)")

# --- MAIN PAGE ---
st.title("THE CAREER STORYBOOK")
st.markdown("##### *Directed by Bui Xuan Tung*")
st.image("https://images.unsplash.com/photo-1492551557933-34265f7af79e?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&h=400&q=80")

# --- NỘI DUNG CHÍNH ---
tab1, tab2, tab3, tab4 = st.tabs(["📜 KỊCH BẢN", "🎞️ HÀNH TRÌNH", "📸 PHÒNG TỐI", "📦 DỰ ÁN"])

with tab1: # GIỚI THIỆU
    col1, col2 = st.columns([2, 1])
    with col1:
        st.header("Chapter I: The Origin")
        st.write("Chào mừng đến với không gian của tôi. Tôi là sự kết hợp giữa **Tư duy Logic** của Logistics và **Tư duy Hình ảnh** của Nhiếp ảnh gia.")
        st.success("💡 **Triết lý:** Logistics là bộ khung sườn. Nghệ thuật là linh hồn.")
    with col2:
        st.header("🎧 Vibe Check")
        st.markdown('<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/4jV6W9UvV6HjQz6Y1K9G5H?utm_source=generator" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>', unsafe_allow_html=True)

with tab2: # KINH NGHIỆM
    st.header("Chapter II: The Journey")
    st.markdown("### 🏢 2023 - Present: VLIGHT VIETNAM")
    st.write("- Quản lý hợp đồng thương mại & Điều phối quy trình.\n- Thành tích: Top 4 Sales Performance.")
    st.divider()
    st.markdown("### ☕ 2024: TRUNG COFFEE")
    st.write("- Tư vấn bán hàng & Chăm sóc khách hàng quốc tế.")

with tab3: # NHIẾP ẢNH
    st.header("Chapter III: The Visual Lab")
    c1, c2, c3 = st.columns(3)
    with c1: st.image("https://images.unsplash.com/photo-1516035069371-29a1b244cc32", caption="Street")
    with c2: st.image("https://images.unsplash.com/photo-1555421689-491a97ff2040", caption="Logistics")
    with c3: st.image("https://images.unsplash.com/photo-1511379938547-c1f69419868d", caption="Music")

with tab4: # DỰ ÁN
    st.header("Chapter IV: The Logic Core")
    c1, c2 = st.columns(2)
    with c1:
        st.info("📦 **Logistics Cost Analyzer**")
        st.write("Tool Python tự động so sánh giá cước vận chuyển.")
    with c2:
        st.error("🇨🇳 **Trade Dashboard**")
        st.write("Bảng điều khiển theo dõi kim ngạch XNK.")

st.markdown("---")
st.markdown("<center>© 2025 The Career Storybook | Directed by Bui Xuan Tung</center>", unsafe_allow_html=True)