from flask import Flask
from flask_restful import Resource, abort,reqparse,Api
import pandas as pd

app = Flask(__name__)
api = Api(app)

file_path = pd.ExcelFile("file\KnowledgeBaseReplica.xlsx") 
Questions = []
Answers = []

class report(Resource): 
    def get(self):
        data = pd.read_excel(file_path)

        for i in range(len(data)):
            Questions.append(data.iloc[i][0])
            Answers.append(data.iloc[i][1])

        que_ans = {"data":[]}
        for i in range(len(Questions)):
            que_ans["data"].append({"Question":Questions[i],"Answer":Answers[i]})
        return que_ans

    
        
api.add_resource(report,'/')

if __name__=="__main__":
    app.run(debug=True)