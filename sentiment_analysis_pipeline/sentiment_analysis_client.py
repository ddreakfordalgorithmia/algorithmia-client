import Algorithmia
import os
import json

input = "data://algorithmia_se/SentimentAnalysisPipeline"

client = Algorithmia.client(os.getenv('ALGORITHMIA_API_KEY'), os.getenv('ALGORITHMIA_API'))
algo = client.algo('ddreakford/sentiment_analysis_pipeline/2.0.2')
algo.set_options(timeout=300) # optional

result = algo.pipe(input).result
print(json.dumps(result, indent=2))
