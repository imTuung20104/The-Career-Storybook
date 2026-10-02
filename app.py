import streamlit as st

# 1. CÀI ĐẶT TRANG (Bắt buộc để full màn hình và đổi tên tab)
st.set_page_config(
    page_title="Tung Visual | Portfolio",
    page_icon="🎬",
    layout="wide"
)

# 2. ÉP GIAO DIỆN TỐI (DARK MODE) BẰNG CSS
st.markdown("""
    <style>
        .stApp { background-color: #0E1117; color: #FFFFFF; }
    </style>
""", unsafe_allow_html=True)

# 3. ĐOẠN CODE HTML "VIBE ĐIỆN ẢNH" CỦA BẠN
header_html = """
<table align="center" style="border: none; width: 100%;">
  <tr>
    <td width="30%" align="right" style="padding-right: 25px;">
      <img src="https://raw.githubusercontent.com/imTuung20104/imTuung20104.github.io/f0ff9cbbe9fc6759195b0b4ceb1ddea3f6d8e7e8/my_avatar.JPG" width="160" height="160" style="border-radius: 50%; filter: grayscale(100%) contrast(1.1) brightness(0.95); box-shadow: 15px 15px 40px rgba(0,0,0,0.6); object-fit: cover;" alt="Director Avatar" />
    </td>
    <td width="70%" align="left">
      <p style="font-family: serif; font-size: 14px; letter-spacing: 4px; color: #666; margin-bottom: 0;">DIRECTED BY</p>
      <h1 style="font-family: sans-serif; font-size: 45px; margin: 5px 0 5px 0; letter-spacing: -2px; color: #fff;">BUI XUAN TUNG</h1>
      <img src="https://readme-typing-svg.herokuapp.com?font=Cinzel&weight=500&size=18&pause=1000&color=D4AF37&width=600&lines=The+Visual+Logistics+Architect;Combining+Art+with+Supply+Chain;From+Hanoi+with+Passion..." alt="Cinematic Title" />
    </td>
  </tr>
</table>

<div align="center">
  <img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/solar.png" width="90%" style="opacity: 0.2;">
</div>

<div align="center" style="font-family: serif; max-width: 650px; margin: 20px auto; color: #bbb;">
  <p>
    <i>"Logistics là bộ khung sườn. Nghệ thuật là linh hồn.<br/>
    Tôi kể những câu chuyện kinh doanh bằng tư duy của một đạo diễn hình ảnh."</i>
  </p>
</div>

<h3 align="center" style="font-family: serif; letter-spacing: 2px;">I. THE VISUAL RIG</h3>

<table align="center" style="border-collapse: collapse; border: none;">
  <tr>
    <td width="50%" align="center" style="padding: 20px; border-right: 1px solid #333;">
      <img src="https://raw.githubusercontent.com/imTuung20104/imTuung20104.github.io/main/my_sony_gear.jpg" width="100%" style="border-radius: 2px; box-shadow: 10px 10px 0px #111; filter: grayscale(20%);" />
    </td>
    <td width="50%" valign="middle" style="padding: 20px;">
      <h4 style="letter-spacing: 2px; margin-bottom: 5px; color: #fff;">SONY A6400</h4>
      <p style="font-size: 11px; color: #888; margin-top: 0;">PRIMARY WEAPON</p>
      <br/>
      <code style="color: #999; font-size: 12px; line-height: 20px;">
        ⚡ SENSOR.....: APS-C Exmor CMOS<br/>
        🔭 LENS.......: Sony G 18-105mm f/4<br/>
        🎨 PROFILE....: S-Log2 / HLG<br/>
        🎬 RES........: 4K HDR
      </code>
      <br/><br/>
      <img src="https://img.shields.io/badge/EDIT-Lightroom-black?style=for-the-badge&logo=adobe-lightroom&logoColor=white"/>
    </td>
  </tr>
</table>
<br/><br/>
"""
# Đẩy HTML lên Streamlit
st.markdown(header_html, unsafe_allow_html=True)


# ==========================================
# 4. KHU VỰC PORTFOLIO (DỄ DÀNG CẬP NHẬT ẢNH)
# ==========================================
st.markdown("<h3 align='center' style='font-family: serif; letter-spacing: 2px;'>II. THE BEAUTY & PORTRAIT</h3><br/>", unsafe_allow_html=True)

# Chia làm 3 cột để hiển thị ảnh
col1, col2, col3 = st.columns(3)

# CỘT 1
with col1:
    # Sau này bạn chỉ cần thay đường dẫn ảnh vào trong dấu ngoặc kép này
    st.image("https://images.unsplash.com/photo-1516161599424-4c28f97ce111?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", use_container_width=True)
    st.caption("Dự án Nàng Thơ 1")
    
    st.image("https://images.unsplash.com/photo-1524504388940-b1c1722653e1?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", use_container_width=True)
    st.caption("Lookbook Mùa Thu")

# CỘT 2
with col2:
    st.image("https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", use_container_width=True)
    st.caption("Dự án Beauty 1")
    
    st.image("https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", use_container_width=True)
    st.caption("Chân dung Cinematic")

# CỘT 3
with col3:
    st.image("https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", use_container_width=True)
    st.caption("Commercial Campaign")
    
    st.image("https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", use_container_width=True)
    st.caption("Góc nghiêng")

# 5. SOUNDTRACK VÀ FOOTER
footer_html = """
<br/><br/>
<h3 align="center" style="font-family: serif; letter-spacing: 2px;">III. SOUNDTRACK</h3>
<div align="center" style="border: 1px solid #333; padding: 25px; width: 85%; border-radius: 2px; background: #050505; margin: 0 auto;">
  <table style="border: none; width: 100%;">
    <tr>
      <td width="20%" align="center">
         <img src="https://i.scdn.co/image/ab67616d0000b2730a8801d01308a34241e3d069" width="80" style="border-radius: 50%; border: 2px solid #222; animation: spin 10s linear infinite; opacity: 0.8;" />
      </td>
      <td width="60%" align="center">
        <p style="font-family: monospace; letter-spacing: 3px; font-size: 10px; margin: 0; color: #555;">NOW PLAYING</p>
        <p style="font-weight: bold; font-size: 16px; margin: 10px 0; color: #fff;">ĐỪNG LÀM TRÁI TIM ANH ĐAU</p>
        <p style="font-size: 12px; color: #888;">SƠN TÙNG M-TP</p>
      </td>
      <td width="20%" align="center">
        <a href="https://open.spotify.com/track/622M65s1b5A7xZg73Sj4qg">
          <img src="https://img.shields.io/badge/PLAY-black?style=for-the-badge&logo=spotify&logoColor=white"/>
        </a>
      </td>
    </tr>
  </table>
</div>
<br/><br/>
<div align="center">
  <p style="font-family: monospace; font-size: 10px; letter-spacing: 3px; color: #444;">
    DIRECTED BY BUI XUAN TUNG<br/>BASED IN HANOI, VIETNAM
  </p>
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)
