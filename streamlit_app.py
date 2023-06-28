import requests
import streamlit as st

ip_address = st.text_input("Enter IP address you want to look up : ")
headers = {
  "authorization": st.secrets["api_key"]
}

url = f"http://api.ipstack.com/.format(ip_address)?access_key={hearders}"
response = requests.get (url)

if response.status.code == 200:
  data = response.json()
  st.write(data)

else:
  st.write(f"Error {response.status_code}: {response.text}")
