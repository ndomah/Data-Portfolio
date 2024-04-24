import streamlit as st
import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyBVllet_oPOrk7gcMc6NPHukZikD7rboNk"

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

def main():
    st.set_page_config(page_title="SQL Query Generator 🌐", page_icon=":robot:")
    st.markdown(
        """
            <div style="text-align: center;">
                <h1>🤖 SQL Query Generator 🤖</h1>
                <h3>Generate SQL queries (with an explanation) using Google Gemini</h3>
                <p>This is a simple tool that allows you to generate SQL queries based on your input.</p>
            </div>
        """,
        unsafe_allow_html=True
    )

    text_input = st.text_area("Enter your query here in plain english:")

    submit = st.button("Generate SQL query")
    if submit:
        with st.spinner("Generating SQL query..."):
            template = """
                Create a SQL query snippet using the below text:
                ```
                    {text_input}     
                ```            
                I just want a SQL query.
            """
            formatted_template = template.format(text_input=text_input)
            response = model.generate_content(formatted_template)
            sql_query = response.text
            sql_query = sql_query.strip().lstrip("```sql").rstrip("```")
            

            expected_output = """
                What would be the expected response of this SQL query snippet:
                ```
                    {sql_query}     
                ```            
                Provide some tabular response with no explanation.
            """
            expected_output_formatted = expected_output.format(sql_query=sql_query)
            eoutput = model.generate_content(expected_output_formatted)
            eoutput = eoutput.text

            explanation = """
                Explain this SQL query:
                ```
                    {sql_query}     
                ```            
                Please provide with the simplest explanation:
            """
            explanation_formatted = explanation.format(sql_query=sql_query)
            explanation = model.generate_content(explanation_formatted)
            explanation = explanation.text
            
            with st.container():
                st.success("SQL query generated successfully! Here is your query below:")
                st.code(sql_query, language="sql")

                st.success("Expected output of this SQL query will be something like:")
                st.markdown(eoutput)

                st.success("Explanation of this SQL query:")
                st.markdown(explanation)

main()