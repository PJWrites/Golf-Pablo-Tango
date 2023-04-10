# Golf-Pablo-Tango
import openai
import json
import requests 
import streamlit as st 

openai.api_key = st.secrets["openaiApiKey"]

def BasicGeneration(userPrompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": userPrompt}]
    )
    return completion.choices[0].message.content

st.title('Bitcoin Analyzer with ChatGPT')
st.subheader('Press the button to be blown away with analysis')

def GetBitcoinPrices():

    # Define the API endpoint and query parameters
    url = "https://coinranking1.p.rapidapi.com/coin/Qwsogvtv82FCd/history"

    querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","timePeriod":"7d"}
    
    # Define the request headers with API key and host
    headers = {
        "X-RapidAPI-Key": "9c66426824mshd0048ae0fe48c15p185f6ejsnd7f6c6a46d5d",
        "X-RapidAPI-Host": "coinranking1.p.rapidapi.com"
    }
    
    # Send a GET request to the API endpoint with query parameters and headers
    response = requests.request("GET", url, headers=headers, params=querystring)
    
    #Parse the response datat as a JSON object
    JSONResult = json.loads(response.text)

    #Extract the "history" field from the JSON response
    history = JSONResult["data"]["history"]

    #Extract the "price" field from each element in the "history" array and add to a list
    prices = []
    for change in history:
        prices.append(change["price"])
    
    #join the list of prices into a comma-separated string
    pricesList = ','.join(prices)

    #return the comma-separated string of prices
    return pricesList


if st.button('Analyze'):
    with st.spinner('Getting Bitcoin Prices...'):
        bitcoinPrices = GetBitcoinPrices()
        st.success('Done!')
    with st.spinner('Analyzing Bitcoin Prices...'):
        chatGPTPrompt = f"""You are an expert crypto trader with more than 10 years of experience, 
            I will provide you with a list of bitcoin prices for the last 7 days
            can you provide me with a technical analysis
            of Bitcoin based on these prices. here is what I want:
            Price Overview, 
            Moving Averages, 
            Relative Strength Index (RSI),
            Moving Average Convergence Divergence (MACD),
            Advice and Suggestion,
            Do I buy or sell?
            Please be as detailed as much as you can, and explain in a way any beginner can understand. 
            Here is the price list: {bitcoinPrices}"""

        analysis = BasicGeneration(chatGPTPrompt)
        st.text_area("Analysis", analysis, height=500)
        st.success('Done!')