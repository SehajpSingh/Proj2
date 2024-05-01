import streamlit as st
import pandas

st.set_page_config(layout="wide");
col1, col2 = st.columns(2)

with col1:
    st.image("images/SehajSingh.png", width=400)

with col2:
    st.title('Sehaj Punit Singh')
    content = """
      Hello, this is Sehaj!!
      """
    st.info(content) #blue box around text
    #st.write(content)

content2 = """
Below you will find some stuff
"""
st.info(content2)

#creating columns and adding space b/w them
col3, empty_col, col4 = st.columns([1.5,0.5,1.5])
df = pandas.read_csv("data.csv",sep=";")

with col3:
    for index, row in df.iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

# col3 and col 4 do the same things except
# creating two different columns to divide up
#'title', 'description, 'image', 'url' are
#column names inside df for each of the 19 entries
#row refers to that object

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])

