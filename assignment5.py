import openai
import os
from dotenv import load_dotenv

load_dotenv() 
OpenAI_Key = os.getenv("OPENAI_API_KEY")

# Set your API key
client = openai.OpenAI(api_key=OpenAI_Key)

resume = """

Email: avc.xyz@something.com | Phone: 222-222-2222
 Summary:
Over 8 years of professional work experience in Object Oriented Programming, design and development of multi-Tier distributed applications using Java and J2EE technologies.
Experience:
Software Engineer – TechSolutions Inc. (2023–Present)
•	Developed and maintained infrastructure for applications on AWS using ECS Java, Hibernate, J2EE services and spring framework, JavaScript/ Typescript/Python, lambda/Express.js ensuring efficient container orchestration and autoscaling for high traffic demands.
•	Develop and manage backend services and REST APIs to support mobile and web applications for comcast and its various partners as a cross-functional team.
o	Developed and maintained dynamic, high-performance web applications using React.js and Redux for state management.
o	Integrated React Router for seamless client-side navigation and deep linking.
•	Created and maintained AWS lambdas functions in Python and Node.js for managing WIFI-extenders.
•	Worked on various Spring frameworks for developing microservices with different dependencies such as Spring Security, Spring cloud, Spring cloud sleuth, etc.
Education:
B.S. in Computer and information Science
"""

topic = input("Enter the topic: ")

# Define the prompt
messages = [
    {"role": "system", "content": "You re reviewing the resume"},
    {"role": "user", "content": f'Analyze if the resume is good fit :\n\n"{resume}"\n\n:'}
]


# Call the GPT-4o model
response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    temperature=0 
)

# Extract and print the result
topic_description = response.choices[0].message.content.strip()
print(f"Corrected response : {topic_description}")


