import os
import json
import requests
import pandas as pd

# URL-адрес, на который отправляется запрос
url = "http://0.0.0.0:8080/"

queies_df = pd.read_csv(os.path.join("data", "queries_for_testing.csv"), sep="\t")
queies_dicts = queies_df.to_dict(orient="records")


queries_with_answers = []
for d in queies_dicts:
    query = str(d["Query"])
    print(query)
    
    try:
        payload = {
            "query": d["Query"],
            "alias": "bss.vip"
        }
    
        response = requests.post(url, data=json.dumps(payload))
        print("status_code:", response.status_code)
        print("json:", response.json())
        answer = response.json().get("answer", "No answer found")
        print("answer:", answer)
        # d["Answer"] = ans_json["answer"]
        d["Answer"] = answer
        
        queries_with_answers.append(d)
    except:
        d["Answer"] = "Error"
        queries_with_answers.append(d)

    queries_with_answers_df = pd.DataFrame(queries_with_answers)
    queries_with_answers_df.to_csv(os.path.join("data", "queries_with_answers_2.csv"), index=False, sep="\t")