import streamlit as st 

st.set_page_config(layout="wide")

import pandas as pd

import numpy as np

import plotly.graph_objects as go

import plotly.express as px

st.write('''<style>
         a:hover {
         background-color: yellow;
         text-decoration: none;
         }
         </style>''', unsafe_allow_html=True)






st.write('''<br><br><br><center><font color = "#0000ff" size = 7>PENELUSURAN LITERATUR: APLIKASI PLS-SEM PADA KINERJA KEUANGAN ATAU KINERJA PERUSAHAAN</font></center>



             ''', unsafe_allow_html = True)

















st.write('''<style>
         a:hover {
         background-color: yellow;
         text-decoration: none;
         }
         </style>''', unsafe_allow_html=True)





pilih_publisher = st.radio(
    "Pilih Publisher: ",
    [":rainbow[Taylor and Francis]", ":rainbow[Elsevier]",":rainbow[John Wiley & Sons]" , ":rainbow[Springer]", ":rainbow[Emerald]",     ])


if pilih_publisher == ":rainbow[Taylor and Francis]":
    pilih_jurnal = st.radio(
    "Pilih Jurnal: ",
    [":rainbow[Cogent Economics & Finance]",     ])
    st.write('''<br><br><br><center><font color = "#0000ff" size = 7>2024</font></center>''', unsafe_allow_html = True)
    st.markdown(
    """<a href="https://www.tandfonline.com/doi/full/10.1080/23322039.2024.2325834">
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2024/1/3.png" width="900"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2024/1/2.png" width="800"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2024/1/1.png" width="1200"><br>
        </a>""",
    unsafe_allow_html=True)


    st.markdown(
    """<br><br><a href="https://www.tandfonline.com/doi/full/10.1080/23311975.2023.2297458#abstract">
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2024/2/1.png" width="900"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2024/2/2.png" width="800"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2024/2/3.png" width="1200"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2024/2/4.png" width="1200"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2024/2/5.png" width="1200"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2024/2/6.png" width="1200"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2024/2/7.png" width="1200"><br>
        </a>""",
    unsafe_allow_html=True)



    st.markdown(
    """<br><br><a href="https://www.tandfonline.com/doi/full/10.1080/23311975.2024.2363415#abstract">
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2024/3/1.png" width="900"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2024/3/2.png" width="800"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2024/3/3.png" width="1200"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2024/3/4.png" width="1200"><br>
        </a>""",
    unsafe_allow_html=True)








    st.markdown(
    """<br><br><a href="https://www.tandfonline.com/doi/full/10.1080/23311975.2024.2381087#abstract">
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2024/4/1.png" width="900"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2024/4/2.png" width="800"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2024/4/3.png" width="1200"><br>
        </a>""",
    unsafe_allow_html=True)




    st.markdown(
    """<br><br><a href="https://www.tandfonline.com/doi/full/10.1080/23311975.2024.2318635#abstract">
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2024/5/1.png" width="900"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2024/5/2.png" width="800"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2024/5/3.png" width="1200"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2024/5/4.png" width="1200"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2024/5/5.png" width="1200"><br>
        </a>""",
    unsafe_allow_html=True)









    st.write('''<br><br><br><center><font color = "#0000ff" size = 7>2023</font></center>''', unsafe_allow_html = True)
    st.markdown(
    """<br><a href="https://www.tandfonline.com/doi/full/10.1080/23311975.2023.2174246#abstract">
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2023/1/1.png" width="900"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2023/1/2.png" width="800"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2023/1/3.png" width="1200"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2023/1/4.png" width="1200"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2023/1/5.png" width="1200"><br>
        </a>""",
    unsafe_allow_html=True)


    st.markdown(
    """<br><br><a href="https://www.tandfonline.com/doi/full/10.1080/23311975.2023.2232159#d1e1012">
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2023/2/1.png" width="900"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2023/2/2.png" width="800"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2023/2/3.png" width="1200"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2023/2/4.png" width="1200"><br>
        </a>""",
    unsafe_allow_html=True)



    st.markdown(
    """<br><br><a href="https://www.tandfonline.com/doi/full/10.1080/23311975.2023.2207880#abstract">
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2023/3/1.png" width="900"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2023/3/2.png" width="800"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2023/3/3.png" width="1200"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2023/3/4.png" width="1200"><br>
        </a>""",
    unsafe_allow_html=True)









    st.write('''<br><br><br><center><font color = "#0000ff" size = 7>2022</font></center>''', unsafe_allow_html = True)
    st.markdown(
    """<br><a href="https://www.tandfonline.com/doi/full/10.1080/23322039.2022.2127486#abstract">
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2022/1/1.png" width="900"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2022/1/2.png" width="800"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2022/1/3.png" width="1200"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2022/1/4.png" width="1200"><br>
        </a>""",
    unsafe_allow_html=True)


    st.markdown(
    """<br><br><br><a href="https://www.tandfonline.com/doi/full/10.1080/23311975.2022.2147123#abstract">
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2022/2/1.png" width="900"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2022/2/2.png" width="1200"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2022/2/3.png" width="1200"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2022/2/4.png" width="1200"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2022/2/5.png" width="1200"><br>
        </a>""",
    unsafe_allow_html=True)










    st.write('''<br><br><br><center><font color = "#0000ff" size = 7>2019</font></center>''', unsafe_allow_html = True)
    st.markdown(
    """<br><a href="https://www.tandfonline.com/doi/full/10.1080/23322039.2019.1589406#abstract">
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2019/1/1.png" width="900"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2019/1/2.png" width="800"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2019/1/3.png" width="1200"><br>
        </a>""",
    unsafe_allow_html=True)










    st.write('''<br><br><br><center><font color = "#0000ff" size = 7>2017</font></center>''', unsafe_allow_html = True)
    st.markdown(
    """<br><a href="https://www.tandfonline.com/doi/full/10.1080/23311975.2017.1364056#abstract">
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2017/1/1.png" width="900"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2017/1/2.png" width="800"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2017/1/3.png" width="1200"><br>
        </a>""",
    unsafe_allow_html=True)
























































st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")






st.markdown(
    """<center><img src="https://statkomat.com/gambar/ugi.png" width="500"></center>
    <h2 style='text-align: justify; color: blue;'><center>Prana Ugiana Gio, Founder of <a href = 'https://statcal.com/' target = '_blank' style = 'text-decoration:none'><font color = 'orange'>STATCAL</a></center></h2>""",
    unsafe_allow_html=True)




col1, col2, col3, col4, col5, col6 = st.columns([2, 2, 2, 2, 2, 2])
with col1:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/logo_figshare2.png" width="50"><br><a href = 'https://figshare.com/authors/prana_ugiana_gio/17826386' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>FIGSHARE</b></font></center></a>""",unsafe_allow_html=True)
with col2:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/statkomat.gif" width="50"><br><a href = 'https://statkomat.com/download_tulisan.php' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>STATKOMAT</b></font></center></a>""",unsafe_allow_html=True)
with col3:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/youtube.png" width="50"><br><a href = 'https://www.youtube.com/@STATKOMAT/videos' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>YOUTUBE</b></font></center></a>""",unsafe_allow_html=True)
with col4:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/literature-review.gif" width="50"><br><a href = 'https://literaturereview.streamlit.app/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>LITERATURE REVIEW</b></font></center></a>""",unsafe_allow_html=True)
with col5:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/list-papers.gif" width="50"><br><a href = 'https://daftar-paper.streamlit.app/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>LIST OF JOURNALS</b></font></center></a>""",unsafe_allow_html=True)
with col6:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/my-papers.gif" width="50"><br><a href = 'https://ugi-publikasi.streamlit.app/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>MY PAPERS</b></font></center></a>""",unsafe_allow_html=True)

st.markdown("")
st.markdown("")

col7, col8, col9, col10, col11, col12 = st.columns([2, 2, 2, 2, 2, 2])
with col7:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/pls-sem.gif" width="50"><br><a href = 'https://aplikasi-plssem.streamlit.app//' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>STRUCTURAL EQUATION MODELING (PLS-SEM)</b></font></center></a>""",unsafe_allow_html=True)
with col8:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/statcal.gif" width="50"><br><a href = 'https://statcal.com/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>STATCAL</b></font></center></a>""",unsafe_allow_html=True)
with col9:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/shiny.gif" width="50"><br><a href = 'https://share-your-shiny-app.id/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>SHINY</b></font></center></a>""",unsafe_allow_html=True)
with col10:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/ugi-gio.gif" width="50"><br><a href = 'https://ugi-gio.id/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>UGI</b></font></center></a>""",unsafe_allow_html=True)
with col11:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/indcomp.gif" width="50"><br><a href = 'https://indcomp-stats.id/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>INDCOMP</b></font></center></a>""",unsafe_allow_html=True)
with col12:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/github.png" width="50"><br><a href = 'https://github.com/gioprana89' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>GITHUB</b></font></center></a>""",unsafe_allow_html=True)






















st.markdown("")
st.markdown("")

col13, col14, col15, col16, col17, col18 = st.columns([2, 2, 2, 2, 2, 2])
with col13:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/cfa.gif" width="50"><br><a href = 'https://cfa-aplikasi.streamlit.app/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>CONFIRMATORY FACTOR ANALYSIS (CFA)</b></font></center></a>""",unsafe_allow_html=True)
with col14:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/pls-sem-kinerja-keuangan.gif" width="50"><br><a href = 'https://pls-sem-kinerja-keuangan.streamlit.app/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>APLIKASI PLS-SEM PADA KINERJA KEUANGAN</b></font></center></a>""",unsafe_allow_html=True)































st.markdown("")
st.markdown("")

st.markdown("""<a href = 'https://saweria.co/statkomat' target = '_blank' style = 'text-decoration:none'><center><img src="https://statkomat.com/streamlit-ugi/kopi.gif" width="150"></center></a><br><center><b><a href = 'https://saweria.co/statkomat' target = '_blank' style = 'text-decoration:none'><font color = 'orange' size = 7>Buy Me a Cup of Coffee</font></a></b></font></center>""",unsafe_allow_html=True)












