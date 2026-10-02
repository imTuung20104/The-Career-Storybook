import streamlit as st

# 1. CÀI ĐẶT TRANG
st.set_page_config(
    page_title="Bui Xuan Tung | Visual Artist",
    page_icon="📸",
    layout="wide"
)

# 2. NHÚNG FONT CHỮ NGHỆ THUẬT VÀ CSS GIAO DIỆN TỐI
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400;1,600&family=Montserrat:wght@300;400&display=swap');
        
        .stApp { background-color: #0A0A0A; color: #FFFFFF; }
        
        /* Ẩn các menu mặc định của Streamlit cho giống web xịn */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# 3. HEADER: THÔNG TIN GIỚI THIỆU THUẦN NHIẾP ẢNH
header_html = """
<table align="center" style="border: none; width: 100%; margin-top: 20px;">
  <tr>
    <td width="35%" align="right" style="padding-right: 30px;">
      <img src="https://raw.githubusercontent.com/imTuung20104/imTuung20104.github.io/f0ff9cbbe9fc6759195b0b4ceb1ddea3f6d8e7e8/my_avatar.JPG" width="180" height="180" style="border-radius: 50%; filter: grayscale(80%) contrast(1.1) brightness(0.9); box-shadow: 0px 0px 40px rgba(212, 175, 55, 0.15); object-fit: cover;" alt="Director Avatar" />
    </td>
    <td width="65%" align="left">
      <p style="font-family: 'Montserrat', sans-serif; font-size: 11px; letter-spacing: 6px; color: #888; margin-bottom: 0; text-transform: uppercase;">Lens & Light directed by</p>
      <h1 style="font-family: 'Cormorant Garamond', serif; font-size: 60px; margin: 0; letter-spacing: 2px; color: #fff; font-weight: 600;">BÙI XUÂN TÙNG</h1>
      <img src="https://readme-typing-svg.herokuapp.com?font=Cormorant+Garamond&weight=500&size=22&pause=1500&color=D4AF37&width=600&lines=Portrait+%26+Beauty+Photographer;Cinematic+Visual+Storyteller;Chasing+Light+in+Hanoi" alt="Cinematic Title" />
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px;">
  <img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/solar.png" width="80%" style="opacity: 0.15;">
</div>

<!-- LỜI DẪN NGHỆ THUẬT -->
<div align="center" style="font-family: 'Cormorant Garamond', serif; max-width: 700px; margin: 35px auto; color: #d0d0d0; font-size: 22px; line-height: 1.6;">
  <p>
    <i>"Nhiếp ảnh không chỉ là thao tác bấm máy, mà là cách chúng ta giao tiếp với ánh sáng và cảm xúc.<br/>
    Tôi ở đây để lưu giữ thanh xuân, tôn vinh vẻ đẹp nguyên bản <br/>và kể câu chuyện của bạn qua những khung hình điện ảnh."</i>
  </p>
</div>

<br/>

<!-- ĐỒ NGHỀ (Đã tinh chỉnh cho sang trọng hơn) -->
<h3 align="center" style="font-family: 'Montserrat', sans-serif; font-size: 14px; letter-spacing: 4px; color: #888;">I. THE VISUAL RIG</h3>

<table align="center" style="border-collapse: collapse; border: none; max-width: 800px; margin: 20px auto;">
  <tr>
    <td width="50%" align="center" style="padding: 20px; border-right: 1px solid #222;">
      <img src="https://raw.githubusercontent.com/imTuung20104/imTuung20104.github.io/main/my_sony_gear.jpg" width="90%" style="border-radius: 4px; filter: grayscale(40%);" />
    </td>
    <td width="50%" valign="middle" style="padding: 20px 20px 20px 40px;">
      <h4 style="font-family: 'Cormorant Garamond', serif; font-size: 24px; letter-spacing: 2px; margin-bottom: 5px; color: #D4AF37;">SONY ALPHA SYSTEM</h4>
      <p style="font-family: 'Montserrat', sans-serif; font-size: 10px; letter-spacing: 2px; color: #666; margin-top: 0;">PRIMARY WEAPON</p>
      <br/>
      <code style="background: transparent; color: #aaa; font-family: monospace; font-size: 13px; line-height: 24px;">
        ✦ BODY.....: Sony A7C / a6400<br/>
        ✦ LENS.....: Sigma 24-70mm f/2.8 Art<br/>
        ✦ COLOR....: Cinematic / Korean Vibe<br/>
        ✦ POST.....: Adobe Lightroom
      </code>
    </td>
  </tr>
</table>
<br/><br/>
"""
st.markdown(header_html, unsafe_allow_html=True)


# ==========================================
# 4. KHU VỰC PORTFOLIO 
# ==========================================
st.markdown("<h3 align='center' style='font-family: \"Montserrat\", sans-serif; font-size: 14px; letter-spacing: 4px; color: #888; margin-bottom: 30px;'>II. SELECTED WORKS</h3>", unsafe_allow_html=True)

# Chia làm 3 cột để hiển thị ảnh
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://images.unsplash.com/photo-1516161599424-4c28f97ce111?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", use_container_width=True)
    st.markdown("<p style='text-align: center; font-family: \"Cormorant Garamond\", serif; font-size: 18px; font-style: italic; color: #ccc;'>Nàng Thơ Tà Xùa</p>", unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1524504388940-b1c1722653e1?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", use_container_width=True)
    st.markdown("<p style='text-align: center; font-family: \"Cormorant Garamond\", serif; font-size: 18px; font-style: italic; color: #ccc;'>Autumn Vibe</p>", unsafe_allow_html=True)

with col2:
    st.image("https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", use_container_width=True)
    st.markdown("<p style='text-align: center; font-family: \"Cormorant Garamond\", serif; font-size: 18px; font-style: italic; color: #ccc;'>Commercial Beauty</p>", unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", use_container_width=True)
    st.markdown("<p style='text-align: center; font-family: \"Cormorant Garamond\", serif; font-size: 18px; font-style: italic; color: #ccc;'>Korean Cinematic</p>", unsafe_allow_html=True)

with col3:
    st.image("https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", use_container_width=True)
    st.markdown("<p style='text-align: center; font-family: \"Cormorant Garamond\", serif; font-size: 18px; font-style: italic; color: #ccc;'>Portrait in Hanoi</p>", unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", use_container_width=True)
    st.markdown("<p style='text-align: center; font-family: \"Cormorant Garamond\", serif; font-size: 18px; font-style: italic; color: #ccc;'>The Golden Hour</p>", unsafe_allow_html=True)

# 5. SOUNDTRACK VÀ FOOTER
footer_html = """
<br/><br/>
<div align="center">
  <img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/solar.png" width="50%" style="opacity: 0.15;">
</div>
<br/>
<h3 align="center" style="font-family: 'Montserrat', sans-serif; font-size: 14px; letter-spacing: 4px; color: #888; margin-bottom: 20px;">III. INSPIRATION TUNE</h3>
<div align="center" style="border: 1px solid #222; padding: 25px; width: 60%; border-radius: 8px; background: #080808; margin: 0 auto;">
  <table style="border: none; width: 100%;">
    <tr>
      <td width="20%" align="center">
         <img src="https://i.scdn.co/image/ab67616d0000b2730a8801d01308a34241e3d069" width="70" style="border-radius: 50%; border: 2px solid #D4AF37; animation: spin 10s linear infinite; opacity: 0.9;" />
      </td>
      <td width="60%" align="center">
        <p style="font-family: 'Montserrat', sans-serif; letter-spacing: 3px; font-size: 9px; margin: 0; color: #D4AF37; text-transform: uppercase;">Now Playing</p>
        <p style="font-family: 'Cormorant Garamond', serif; font-weight: 600; font-size: 20px; margin: 5px 0; color: #fff;">ĐỪNG LÀM TRÁI TIM ANH ĐAU</p>
        <p style="font-family: 'Montserrat', sans-serif; font-size: 11px; color: #888;">SƠN TÙNG M-TP</p>
      </td>
      <td width="20%" align="center">
        <a href="https://open.spotify.com/track/622M65s1b5A7xZg73Sj4qg" target="_blank" style="text-decoration: none; color: #D4AF37; font-family: 'Montserrat', sans-serif; font-size: 12px; border: 1px solid #D4AF37; padding: 8px 15px; border-radius: 20px;">
          LISTEN
        </a>
      </td>
    </tr>
  </table>
</div>
<br/><br/><br/>
<div align="center">
  <p style="font-family: 'Montserrat', sans-serif; font-size: 10px; letter-spacing: 4px; color: #555; text-transform: uppercase;">
    PHOTOGRAPHED BY BUI XUAN TUNG<br/>HANOI, VIETNAM
  </p>
  <br/>
  <a href="mailto:tungbx15.lsc@gmail.com" style="color: #888; text-decoration: none; margin: 0 10px; font-family: 'Montserrat', sans-serif; font-size: 12px;">EMAIL</a>
  <a href="https://github.com/imTuung20104" style="color: #888; text-decoration: none; margin: 0 10px; font-family: 'Montserrat', sans-serif; font-size: 12px;">GITHUB</a>
</div>
<br/><br/>
"""
st.markdown(footer_html, unsafe_allow_html=True)
