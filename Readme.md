## Cold Email Generator
The project goal is to generate a cold email with relevance to the job description which is given as input.

###  Loading the URL Content using Langchain Web Base Loader
* In this step the goal is to extract relevant job description content from a given URL. This could be a job posting or a company’s career page, which contains the details of the job requirements.
* Used Langcahin Web-Base Loader to extract the relevant information from the URL. This tool reads through the HTML content, identifies key sections, and extracts the text related to the job.

### Matching Portfolio Link and Job Skills
* To ensure that the generated cold email aligns with both the job requirements and the applicant’s qualifications, we extract key details from the portfolio and job description and use them to craft a personalized email prompt.
* Loaded the portifolio using .csv file and stored in vector database

### Creating an LLM Chain Using Langchain to Integrate Chatgroq and Prompt
* An LLM Chain takes the processed input (prompt with relevant job and portfolio information) and sends it through a language model like llama-3.1.
* We integrate this LLM Via Chat Groq.It takes the prompt as input and outputs a cold email.

### Generated Output:
The LLM processes this input and generates a cold email that introduces the candidate and highlights how their skills match the job description. It might include specific project details, technical skills, and a professional closing.
