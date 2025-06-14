from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableMap, RunnableLambda
from dotenv import load_dotenv
load_dotenv()

llm = OpenAI(temperature=0.7)

def get_details(country, language):

    restaurant_name_chain = RunnableMap({
        'restaurant_name': PromptTemplate(
            template='Suggest a fancy restaurant name for {country} cuisine',
            input_variables=['country']
        ) | llm
    })

    food_menu_chain = RunnableMap({
        'food_menu': PromptTemplate(
            template='Generate menu items for the {restaurant_name}',
            input_variables=['restaurant_name']
        ) | llm
    })

    restaurant_tagline_chain = RunnableMap({
        'restaurant_tagline': PromptTemplate(
            template='Generate an attractive tagline for {restaurant_name} in {language}',
            input_variables=['restaurant_name', 'language']
        ) | llm
    })

    def chain_wrapper(inputs: dict) -> dict:
        name = restaurant_name_chain.invoke(inputs)
        menu = food_menu_chain.invoke(name)
        tagline = restaurant_tagline_chain.invoke({**name, **inputs})
        return {**name, **menu, **tagline}

    full_chain = RunnableLambda(chain_wrapper)

    result = full_chain.invoke({"country": country, "language": language})

    return result

if __name__ == "__main__":
    print(get_details('Indian', 'Hindi'))