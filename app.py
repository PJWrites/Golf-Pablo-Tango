import openai
import json
import requests 
import streamlit as st 
from PIL import Image
from io import BytesIO

openai.api_key = st.secrets["openaiApiKey"]


def BasicGeneration(userPrompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": userPrompt}]
    )
    return completion.choices[0].message.content



st.title('What is the Prescription Drug For?')
prompt = st.text_input('Type of Drug')

if st.button('OK', key = 'type_of_drug'):
    chatGPTPrompt = f"""You are a person who comes up with brand names for pharmaceutical drugs. 
    The names you come up are easy to remember, and focus on the feelings that 
    the words can bring out at a subconscious level. For example, the drug “Ambien” 
    is a sleep aid, and the name implies that you will sleep well, and your “am” 
    (as in the morning after) will be “bien” (as in good, in Spanish). So “Ambien” 
    is a sleep aid with a name that subconsciously implies that you will have a good 
    morning. Another example is the drug “Viagra”, which helps men with erectile 
    dysfunction. “Via” sounds a lot like vitality, and “gra” sounds like growth, 
    indicating a sense of vitality and growth. So “Viagra” is a erectile dysfunction 
    drug with a name that subconsciously implies that their genitals will grow and be 
    erect, thus giving them a sense of vitality. Another one will be Avodart, which 
    is a drug that reduces the size of an enlarged prostate. “Avo” sounds like 
    “avocado”, which resembles the male sexual organ, and “dart” is literally a dart, 
    like a needle that can pop a balloon, thus deflating it, and making it smaller. 
    So “Avodart” is a drug that treats an enlarge prostate that subconsciously imply 
    that their prostate will be reduced dramatically. 
    The drug that the user is developing is {prompt}. Generate for them a list of 5 
    words. The words will have two or three syllables only, and you will provide 
    explanations for each syllable of the word. You will check your drug name with 
    any current drug names out on the market, and if there are names that are 
    currently listed, you will come up with another name."""

    analysis = BasicGeneration(chatGPTPrompt)
    st.write(analysis)

    picturePrompt = st.text_input('Which Drug Would You Like To Advertise?')
    if st.button2('OK', key = 'name_of_drug'):
        dallEPrompt = f"""you are a dall-e pharmaceutical advertisement prompt 
        generator. You will describe an ultra realistic picture of a person typical 
        person that the drug is meant for. They will always appear to be in the middle 
        of an activity (like painting, rock climbing, running through a flower field, 
        swimming in a pool, but stopping for a moment to stare at the camera and smiling 
        for a genuinely happy picture. You will use {picturePrompt} from the text above 
        as the title of the picture and use small font to describe what this 
        medication will do, and also use generic words to use legal language about 
        medications in general, like, "side effects include headache, nausea, vomiting, 
        hallucinations" and always include, "talk to your doctor if this medication is 
        right for you." """
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="600x400"
        )

        image_url = response['data'][0]['url']
        
# Replace with the URL returned by the DALL-E API
# image_url = "https://api.openai.com/v1/images/generations/GENERATION_ID"

# response = requests.get(image_url)
# image = Image.open(BytesIO(response.content))

# st.image(image, caption="DALL-E generated image")