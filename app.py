import streamlit as st
import google.generativeai as genai

# Configure the Gemini API
GOOGLE_API_KEY = "AIzaSyCZ3ggj_IN42WHt44I65dHRytLlM_X5ZXA"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# Define CSS for custom styling
st.markdown(
    """
    <style>
    .title {
        text-align: center;
        font-size: 32px;
        color: #0066cc;
    }
    .code-area {
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 10px;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title for the app
st.snow()
  
# If the button is clicked, generate response
def main():
    st.title(":rainbow[Python code Analysis Reviewer]")
    st.markdown("---")
    
    st.sidebar.title("Options")
    st.sidebar.write("Customize your review")
    st.title("Smart Code Analysis with AI")
    code = st.text_area("Enter your Python code for review:", height=150)
    
    if st.button("Review Code"):
        st.balloons()
        with st.spinner("loading..."):
             response = model.generate_content(f"This Python code snippet potentially contains bugs or areas for improvement:\n\npython\n{code}\n\nPlease identify potential issues and suggest fixes, including code snippets demonstrating the improvements.")
             st.markdown("---")
             st.subheader("Analysis Conclusion:")
             st.write(response.text)

if __name__== "__main__":
    main()