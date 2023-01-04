
import json as j
import requests
import numpy as np
from flask import current_app

def preprocess(text, tokenizer, length=64):
    token_data = tokenizer.batch_encode_plus(
                [text],
                max_length=length,
                pad_to_max_length=True
                )
    input_ids = np.array(token_data['input_ids'])
    attention_masks = np.array(token_data['attention_mask'])
    token_type_ids = np.array(token_data['token_type_ids'])

    return [input_ids, attention_masks, token_type_ids]


def predict(data, items):
    params = {
        "instances": [data]
        }
    
    res = requests.post(current_app.config['INTENT_URL'], data=j.dumps(params))
    predict = j.dumps(res.text)
    result = np.argmax(predict['predictions'][0])

    return items[str(result)]

def serving(text, tokenizer, items):

    try:
        data = preprocess(text, tokenizer)

        result = {
            'status': 'success',
            'intent': predict(data, items)
        }

    except Exception as e:
        result = {
            'status': 'fail',
            'intent': -1
        }
    
    return result
