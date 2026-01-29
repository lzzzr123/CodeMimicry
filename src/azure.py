from openai import AzureOpenAI,OpenAI
def client_call(model_name):
    api_version = "2024-12-01-preview"
    if 'gpt' in model_name:
        client=AzureOpenAI(
                api_version='2024-12-01-preview',
                azure_endpoint="https://xxx.openai.azure.com/" ,
                api_key="5------",
            )
        return client
        
    elif 'DeepSeek' in model_name:
    #elif "grok-3" in model_name or 'Llama-3.3-70B-Instruct' in model_name:
        client=AzureOpenAI(
                api_version='2024-12-01-preview',
                azure_endpoint='https://xxxxx.openai.azure.com/',
                api_key='D9-----k',
            )
        return client
            
    else:
        client=OpenAI(base_url="https://xxx", api_key="sk-xxxxx")
        return client  

