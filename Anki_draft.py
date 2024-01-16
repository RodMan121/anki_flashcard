import os
import openai
import clipboard

# set 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="YOUR_OPENAI_API_KEY" , Get-ChildItem Env: | Where-Object { $_.Name -like "*OPENAI*" }


# Set up OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]

