import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
import json


def lambda_handler(event, context):
    try:
        # Parse the input data from the JSON body
        input_data = json.loads(event['body'])
        
        data = CustomData(
            gender=input_data.get('gender'),
            race_ethnicity=input_data.get('ethnicity'),
            parental_level_of_education=input_data.get('parental_level_of_education'),
            lunch=input_data.get('lunch'),
            test_preparation_course=input_data.get('test_preparation_course'),
            reading_score=int(input_data.get('reading_score')),
            writing_score=int(input_data.get('writing_score'))
        )
        
        data_df = data.get_data_as_df()

        # Initialize the prediction pipeline
        predict_pipeline = PredictPipeline()
        prediction = predict_pipeline.predict(data_df)

        # Return prediction as response
        return {
            "statusCode": 200,
            "body": json.dumps({"prediction": prediction.tolist()})
        }
    
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

class PredictPipeline:
    def __init__(self):
        pass
    
    def predict(self, features):
        try:
            model = load_object("artifacts/model.pkl")
            preprocessor = load_object("artifacts/preprocessor.pkl")
            data_scaled = preprocessor.transform(features)
            prediction = model.predict(data_scaled)
            
            return prediction
        
        except Exception as e:
            raise CustomException(e, sys)
    
class CustomData:
    def __init__(self, 
                 gender:str, 
                 race_ethnicity:str,
                 parental_level_of_education,
                 lunch: str,
                 test_preparation_course: str,
                 reading_score: int,
                 writing_score: int):
        
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score
        
    def get_data_as_df(self):
        
        try:
            custom_data_input_dict={
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score]
            }
            
            custom_data_df=pd.DataFrame(custom_data_input_dict)
            
            return custom_data_df
        
        except Exception as e:
            raise CustomException(e, sys)