# Python client setup
import Algorithmia
import sys
import os
from cca_param_handler import processCmdLine
import random

usageMsg = f"cca_client.py [--approved=true] [--approval_rate=75]"

client = Algorithmia.client(os.getenv('ALGORITHMIA_API_KEY'), os.getenv('ALGORITHMIA_API'))
algo = client.algo('algorithmia_se/CreditCardApproval/1.0.8')
algo.set_options(timeout=300)

inputApproved = {
  "high_balance": 0,
  "owns_home": 1,
  "child_one": 0,
  "child_two_plus": 0,
  "has_work_phone": 0,
  "age_high": 0,
  "age_highest": 1,
  "age_low": 0,
  "age_lowest": 0,
  "employment_duration_high": 0,
  "employment_duration_highest": 0,
  "employment_duration_low": 0,
  "employment_duration_medium": 0,
  "occupation_hightech": 0,
  "occupation_office": 1,
  "family_size_one": 1,
  "family_size_three_plus": 0,
  "housing_coop_apartment": 0,
  "housing_municipal_apartment": 0,
  "housing_office_apartment": 0,
  "housing_rented_apartment": 0,
  "housing_with_parents": 0,
  "education_higher_education": 0,
  "education_incomplete_higher": 0,
  "education_lower_secondary": 0,
  "marital_civil_marriage": 0,
  "marital_separated": 0,
  "marital_single_not_married": 1,
  "marital_widow": 0
}

inputDenied = {
  "high_balance": 0,
  "owns_home": 1,
  "child_one": 0,
  "child_two_plus": 0,
  "has_work_phone": 0,
  "age_high": 0,
  "age_highest": 0,
  "age_low": 0,
  "age_lowest": 0.25,
  "employment_duration_high": 0,
  "employment_duration_highest": 0,
  "employment_duration_low": 0,
  "employment_duration_medium": 0,
  "occupation_hightech": 0,
  "occupation_office": 0,
  "family_size_one": 1,
  "family_size_three_plus": 0,
  "housing_coop_apartment": 0,
  "housing_municipal_apartment": 0,
  "housing_office_apartment": 0,
  "housing_rented_apartment": 0,
  "housing_with_parents": 0,
  "education_higher_education": 1,
  "education_incomplete_higher": 0,
  "education_lower_secondary": 0,
  "marital_civil_marriage": 0,
  "marital_separated": 0,
  "marital_single_not_married": 0,
  "marital_widow": 0
}

inputs = [inputApproved, inputDenied]
inputIdxs = [0,1]
 
# Request a single approval/denial.
def getApproval(approvable):
    print(f"getApproval({approvable})...")
    if approvable:
        print(algo.pipe(inputApproved).result)
    else:
        print(algo.pipe(inputDenied).result)

    return

# Generate the specified approval rate by continously requesting
# approvals.
def genApprovalRate(approvalRate):
    print(f"genApprovalRate({approvalRate})...")
    inputSample = random.choices(inputIdxs, cum_weights=(approvalRate,100), k=100)
    print(f"Sample of input indexes [0=Approved, 1=Denied]: {inputSample}")
    for sampleIdx in inputSample:
        print(algo.pipe(inputs[sampleIdx]).result)
        
    return

# Command line entry point
if __name__ == "__main__":

    if len(sys.argv) == 1:
        print(usageMsg)
        sys.exit(1)
        
    paramDict = processCmdLine(sys.argv[1:])
    if 'approved' in paramDict.keys():
        getApproval(paramDict['approved'])
    elif 'approval_rate' in paramDict.keys():
        while True:
            genApprovalRate(paramDict['approval_rate'])

    exit(0)
