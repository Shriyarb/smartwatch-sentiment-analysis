import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="ABC Product Review Sentiment Analyzer", layout="wide")

st.markdown(
    "<h1 style='text-align:center;'>ABC Company - Product Review Sentiment Analyzer</h1>",
    unsafe_allow_html=True
)

st.write("Welcome to ABC Company's Product Review Sentiment Analyzer!")
st.write("Enter a review for the **ABC X1 Smartwatch** below to analyze its sentiment:")

review = st.text_area("Product Review", placeholder="Type your review here...")

if st.button("Analyze Sentiment"):
    if review.strip() == "":
        st.warning("Please enter a review to analyze.")
    else:
        polarity = TextBlob(review).sentiment.polarity

        if polarity > 0:
            sentiment = "Positive"
        elif polarity < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        st.subheader(f"The sentiment of the review is: **{sentiment}**")
