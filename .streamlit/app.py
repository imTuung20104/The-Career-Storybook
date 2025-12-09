import streamlit as st

# --- CẤU HÌNH TRANG ---
st.set_page_config(
    page_title="Bui Xuan Tung | Career Storybook",
    page_icon="🎥",
    layout="wide"
)

# --- CSS TÙY CHỈNH (GIAO DIỆN CINEMATIC + HOVER EFFECT) ---
st.markdown("""
<style>
    /* Font tiêu đề vàng kim sang trọng */
    h1, h2, h3 { color: #D4AF37 !important; font-family: 'serif'; }
    
    /* Chỉnh màu chữ nội dung */
    p, li, span, div { color: #e0e0e0; font-size: 16px; }
    
    /* --- HIỆU ỨNG ẢNH CAO CẤP --- */
    img { 
        border-radius: 10px; /* Bo góc mềm mại */
        transition: transform 0.3s ease, box-shadow 0.3s ease; /* Hiệu ứng mượt */
    }
    
    /* Khi di chuột vào ảnh */
    img:hover {
        transform: scale(1.02); /* Phóng to nhẹ 2% */
        box-shadow: 0 10px 20px rgba(212, 175, 55, 0.2); /* Đổ bóng màu vàng kim */
        z-index: 10;
    }
    
    /* Ẩn menu mặc định */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR (CỘT TRÁI: THÔNG TIN CÁ NHÂN) ---
with st.sidebar:
    # Avatar của bạn
    st.image("https://raw.githubusercontent.com/imTuung20104/imTuung20104.github.io/f0ff9cbbe9fc6759195b0b4ceb1ddea3f6d8e7e8/my_avatar.JPG", width=180)
    
    st.title("BÙI XUÂN TÙNG")
    st.caption("📍 Hanoi, Vietnam")
    st.info("Logistics Specialist | Visual Creator")
    
    st.write("---")
    st.write("📧 tungbx15.lsc@gmail.com")
    st.write("🔗 [LinkedIn Profile](#)") # Bạn có thể thay link LinkedIn vào dấu #
    
    # Nút tải CV (Giả lập)
    st.button("📄 Download CV (PDF)")

# --- MAIN PAGE (SÂN KHẤU CHÍNH) ---
st.title("THE CAREER STORYBOOK")
st.markdown("##### *Directed by Bui Xuan Tung*")

# Ảnh bìa Cinematic (Giữ nguyên hoặc thay bằng ảnh ngang rộng của bạn nếu có)
st.image("https://images.unsplash.com/photo-1492551557933-34265f7af79e?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&h=400&q=80")

# --- MENU CHUYỂN TAB ---
tab1, tab2, tab3, tab4 = st.tabs(["📜 KỊCH BẢN", "🎞️ HÀNH TRÌNH", "📸 LOOKBOOK", "📦 DỰ ÁN"])

# === TAB 1: GIỚI THIỆU ===
with tab1:
    col1, col2 = st.columns([2, 1])
    with col1:
        st.header("Chapter I: The Origin")
        st.write("""
        Chào mừng đến với không gian của tôi. 
        Tôi là sự giao thoa giữa **Tư duy Logic** của Logistics và **Tư duy Hình ảnh** của Nhiếp ảnh gia.
        
        * 🎓 **Education:** Foreign Trade University (FTU) - Kinh tế đối ngoại.
        * 🗣️ **Languages:** Vietnamese, English, Chinese (HSK 5).
        * 🎯 **Goal:** Tối ưu hóa chuỗi cung ứng bằng dữ liệu và công nghệ.
        """)
        st.success("💡 **Triết lý:** Logistics là bộ khung sườn. Nghệ thuật là linh hồn.")
    
    with col2:
        st.header("🎧 Vibe Check")
        # Widget Spotify (Sơn Tùng M-TP Playlist)
        st.markdown('<iframe style="border-radius:12px" src="https://open.spotify.com/embed/artist/5dfZ5uSmzR7VQK0udbAVpf?utm_source=generator&theme=0" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>', unsafe_allow_html=True)

# === TAB 2: KINH NGHIỆM ===
with tab2:
    st.header("Chapter II: The Journey")
    
    st.markdown("### 🏢 2023 - Present: VLIGHT VIETNAM")
    st.caption("*Role: Commercial Executive*")
    st.write("- Quản lý hợp đồng thương mại & Điều phối quy trình.")
    st.write("- Thành tích: Top 4 Sales Performance (10/2024).")
    
    st.divider()
    
    st.markdown("### ☕ 2024: TRUNG COFFEE")
    st.caption("*Role: Sales & Customer Service*")
    st.write("- Tư vấn bán hàng & Chăm sóc khách hàng quốc tế.")
    st.write("- Sử dụng tiếng Anh/Trung để giao tiếp và xử lý khiếu nại.")

# === TAB 3: BỘ SƯU TẬP ẢNH (LOOKBOOK) ===
with tab3:
    st.header("Chapter III: The Visual Lab")
    st.write("📸 *Captured with Sony a6400 | 18-105mm f4 G*")
    
    # HÀNG 1: 3 ẢNH
    c1, c2, c3 = st.columns(3)
    with c1:
        st.image("https://raw.githubusercontent.com/imTuung20104/The-Career-Storybook/88da9d5d839d98e0bd2473a145b14def53a5f8c5/photo_1.jpg", caption="Shot 01")
    with c2:
        st.image("https://raw.githubusercontent.com/imTuung20104/The-Career-Storybook/88da9d5d839d98e0bd2473a145b14def53a5f8c5/photo_2.jpg", caption="Shot 02")
    with c3:
        st.image("https://raw.githubusercontent.com/imTuung20104/The-Career-Storybook/88da9d5d839d98e0bd2473a145b14def53a5f8c5/photo_3.jpg", caption="Shot 03")
        
    # HÀNG 2: 2 ẢNH (CĂN GIỮA CHO ĐẸP)
    c4, c5 = st.columns(2)
    with c4:
        st.image("https://raw.githubusercontent.com/imTuung20104/The-Career-Storybook/88da9d5d839d98e0bd2473a145b14def53a5f8c5/photo_4.jpg", caption="Shot 04")
    with c5:
        st.image("https://raw.githubusercontent.com/imTuung20104/The-Career-Storybook/88da9d5d839d98e0bd2473a145b14def53a5f8c5/photo_6.jpg", caption="Shot 05")

# === TAB 4: DỰ ÁN ===
with tab4:
    st.header("Chapter IV: The Logic Core")
    
    col_p1, col_p2 = st.columns(2)
    
    with col_p1:
        st.info("📦 **Logistics Cost Analyzer**")
        # Thay link ảnh dưới bằng ảnh chụp tool của bạn nếu có (du_an_logistics.jpg)
        st.image("https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d", use_column_width=True)
        st.write("Tool Python tự động so sánh giá cước vận chuyển.")
        st.markdown("[👉 Xem Code trên GitHub](https://github.com/imTuung20104/Logistics-Cost-Analyzer)")
        
    with col_p2:
        st.error("🇨🇳 **China-Vietnam Trade Dashboard**")
        # Thay link ảnh dưới bằng ảnh chụp dashboard của bạn nếu có (du_an_dashboard.jpg)
        st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71", use_column_width=True)
        st.write("Bảng điều khiển theo dõi kim ngạch XNK.")
        st.markdown("[👉 Xem Code trên GitHub](https://github.com/imTuung20104/China-Vietnam-Trade-Report)")

# --- FOOTER ---
st.markdown("---")
st.markdown("<center>© 2025 The Career Storybook | Directed by Bui Xuan Tung</center>", unsafe_allow_html=True)

