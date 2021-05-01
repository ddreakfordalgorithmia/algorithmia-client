# Python client setup
import Algorithmia
import os

client = Algorithmia.client(os.getenv('ALGO_API_KEY'), 'https://api.algosales.productionize.ai')
algo = client.algo('algorithmia_se/CreditCardApproval/1.0.6')
algo.set_options(timeout=300) # optional

