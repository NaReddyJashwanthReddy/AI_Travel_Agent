from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

api_key=os.getenv('GROQ_API_KEY')


class Models:

    def conversation(self,prompt):
        llm=ChatGroq(
            model='llama-3.1-8b-instant',
            api_key=api_key,
            temperature=0.8
        )

        prompt=f'rephrase the sentence similar to human and give only one output NO PREAMBLE : {prompt}'

        return llm.invoke(prompt).content
    
    def Retrive(self,prompt):
        llm=ChatGroq(
            model='llama-3.1-8b-instant',
            api_key=api_key,
            temperature=0.8
        )

        current_date=datetime.now().strftime("%Y-%m-%d")

        prompt=f"A prompt is given below what you have to do is get elements like location,time,date and other details which can be useful travel purpose and only give the details present in prompt, if possible just provide the only word which is required like suppose the prompt looked like this '''I'm from delhi''' then just generate Delhi. don't give unnecessary data. if it is date convert it into 'YYYY-MM-DD' format(today's date is {current_date}) the date shouldn't be less than today's date NO PREAMBLES : {prompt}"

        return llm.invoke(prompt).content
    
    def GenerateMail(self,form,to,date,hotel,flight):
        llm=ChatGroq(
            model='qwen-2.5-32b',
            api_key=api_key,
            temperature=0.8
        )

        mail=PromptTemplate(
            input_variables=['from','to','date','hotels','flights'],
            template='''
                ## You work in a travel agency. Your in customer service department and your tem lead gave a task to write mail's based on customer prefered details.

                ## Instructions:
                    -> Be as human as possible.
                    -> the mail should be as creative as possible.
                    -> Use emoji's to look attractive.
                    -> You have the freedom to choose in what way do you want to write the mail. You don't have any boundries about it.
                    -> If possible include some tourist spots.
                    -> The mail Should Consist of Correct Content with out any misleading info.
                    -> Mail should be simple.
                    -> Don't show any fill in the blank like [contact],[name] etc.,
                    -> The mail Should Be complete, one without any new details to be added.

                From address : {from}
                To address: {to}
                Date for Trip : {date}
                Flight details : {flights}
                

                ## NO PREAMBLES
        '''
        )

        inputs={
            'from':form,
            'to':to,
            'date':date,
            'hotels':hotel,
            'flights':flight
        }

        chain=LLMChain(llm=llm,prompt=mail)

        generate=chain.run(inputs)
        Subject=generate.split('\n',1)[0]
        Body=generate.split('\n',1)[1]

        return Subject,Body