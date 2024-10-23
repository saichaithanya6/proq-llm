import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key= os.getenv("GROQ_API_KEY"), model_name= "llama-3.1-70b-versatile")

    def extract_jobs(self, cleaned_text):
        prompt_extract= PromptTemplate.from_template(
        """
        ### Scraped text from website:
        {page_data}
        ### INSTRUCTION:
        The scraped text is from the career's page of a website.
        Your job is to extract the job postings and return them in json_format containing the following keys: 'role', 'experience', 'skills' and 'description'
        Only return the valid json
        ### VALID JSON(NO PREAMBLE):
        """
        )
        chain_extract= prompt_extract | self.llm
        res= chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Content too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]
    
    def write_mail(self, job, links):
            prompt_email = PromptTemplate.from_template(
                """
                ### JOB DESCRIPTION:
                {job_description}

                ### INSTRUCTION:
                You are job applicant named Sai Chaithanya, a working professional. You have over 4 years of work experience with Machine learning, Python, SQL, Power BI. 
                Your job is to write a cold email to the Hiring Manager regarding the job mentioned above describing the how you can be best applicant.
                Also add the most relevant ones from the following links to showcase Atliq's portfolio: {link_list}
                Remember you are job applicant. 
                Do not provide a preamble.
                ### EMAIL (NO PREAMBLE):

                """
            )
            chain_email = prompt_email | self.llm
            res = chain_email.invoke({"job_description": str(job), "link_list": links})
            return res.content

if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))