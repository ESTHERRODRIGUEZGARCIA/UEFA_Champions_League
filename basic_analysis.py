import os
from sales_gpt import SalesGPT
from langchain.chat_models import ChatOpenAI

os.environ['OPENAI_API_KEY'] = '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' # sustituye esto por tu propia clave de API

llm = ChatOpenAI(temperature=0.9)

# Creamos una instancia del agente SalesGPT
sales_agent = SalesGPT.from_llm(llm, verbose=False,
                            salesperson_name="Ted Lasso",
                            salesperson_role="Sales Representative",
                            company_name="Sleep Haven",
                            company_business='''Sleep Haven 
                            is a premium mattress company that provides
                            customers with the most comfortable and
                            supportive sleeping experience possible. 
                            We offer a range of high-quality mattresses,
                            pillows, and bedding accessories 
                            that are designed to meet the unique 
                            needs of our customers.''')

# Inicializamos el agente y determinamos la etapa de la conversación
sales_agent.seed_agent()
sales_agent.determine_conversation_stage()

# Realizamos un paso con el agente (SalesGPT)
sales_agent.step()

# El método step() genera una respuesta del agente basada en el contexto actual y la etapa de la conversación.

# Recibimos la respuesta del usuario
user_input = input('Your response: ') # Ejemplo: "Sí, claro"
sales_agent.human_step(user_input)

# Actualizamos la etapa de la conversación y realizamos otro paso con el agente
sales_agent.determine_conversation_stage()
sales_agent.step()
