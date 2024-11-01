import streamlit as st 

st.set_page_config(layout="wide")

import pandas as pd

import numpy as np

import plotly.graph_objects as go

import plotly.express as px







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


    st.write('''<br><br><br><center><font color = "#0000ff" size = 7>2022</font></center>''', unsafe_allow_html = True)
    st.markdown(
    """<br><a href="https://www.tandfonline.com/doi/full/10.1080/23322039.2022.2127486#abstract">
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2022/1/1.png" width="900"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2022/1/2.png" width="800"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2022/1/3.png" width="1200"><br>
        <img src="https://statkomat.com/aplikasi-plsem-kinerjakeuangan-kinerjaperusahaan/taylor and francis/Cogent Economics & Finance/2022/1/4.png" width="1200"><br>
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