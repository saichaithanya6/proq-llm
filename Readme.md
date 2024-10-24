## Cold Email Generator
The project goal is to generate a cold email with relavance to the job description ehich is given as input.

###  Loading the URL Content using Langchain Web Base Loader
* In this step the goal is to extract relevant job description content from a given URL. This could be a job posting or a       company’s career page, which contains the details of the job requirements.

* Used Langcahin Web Base Loader to extract the relevant information from the URL. This tool reads through the HTML content, identifies key sections, and extracts the text related to the job.

### Matching Portfolio Link and Job Skills
* To ensure that the generated cold email aligns with both the job requirements and the applicant’s qualifications, we extract key details from the portfolio and job description and use them to craft a personalized email prompt.
* Loaded the portifolio using .csv file and stored in vector database

* Provided the portfolio link and matching with the job skills, relevant infomation is given as prompt to the LLM.
* Created an LLM Chain using Langchain to integrate the Chatgroq and prompt.