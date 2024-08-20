from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd

def DRG(name,code):
    path = r'C:\Users\Muhammad.Hassan\Documents\Work\Feature Engine\FeatureEngine\Data\DRG_Extraction.csv'
    try:
        df = pd.read_csv(path, na_values=[], keep_default_na=False)
        data = df[df['Code'] == int(code)].to_dict(orient='records')[0]
        data['Coding System'] = str.upper(name)
        return data
    except Exception as e:
        return {'Error': f'No {name} Data Availaible for the code : {code}'}

def CPT(name,code):
    path = r'C:\Users\Muhammad.Hassan\Documents\Work\Feature Engine\FeatureEngine\Data\cpt-rvu-globdays.csv'
    try:
        df = pd.read_csv(path, na_values=[], keep_default_na=False)
        data = df[df['HCPCS'] == str.upper(code)].to_dict(orient='records')[0]
        data['Coding System'] = str.upper(name)
        return data
    except Exception as e:
        return {'Error': f'No {name} Data Availaible for the code : {code}'}
    

@api_view(['GET'])
def hello_world(request):
    name = request.GET.get('name', 'None')
    code = request.GET.get('code', 'None')

    if name == 'None' or code == 'None':
        return Response({'message':'Invalid Params'})
    elif str.lower(name) == 'drg':
        data = DRG(name,code)
        return Response(data)
    elif str.lower(name) == 'cpt':
        data = CPT(name,code)
        return Response(data)
    # elif str.lower(name) == 'icd':
    #     data = DRG(name,code)
    #     data['Coding System'] = name
    #     return Response(data)
    else:
        return Response({'error': 'No Data'})