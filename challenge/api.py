import fastapi
from challenge.model import DelayModel
import pandas as pd
import uvicorn
from typing import List, Dict


app = fastapi.FastAPI()
model = DelayModel()


@app.get("/health", status_code=200)
async def get_health() -> dict:
    return {
        "status": "OK"
    }



@app.post("/predict", status_code=200)
async def post_predict(input_data: Dict) -> dict:
    try:
        flights = input_data["flights"]
        # print(input_data["flights"])
        # print(input_data)
        for flight in flights:
            if "MES" in flight and flight["MES"] > 12:
                raise ValueError("MES must be less than 12 and greater than 0") 
            if "TIPOVUELO" in flight and flight["TIPOVUELO"].upper() not in ["I", "N"]:
                raise ValueError("TIPOVUELO must be I or N")
            new_data = pd.DataFrame(flight,index=[0])
        print(new_data)
        features = model.preprocess(new_data)
        print(features)
        predictions = model.predict(features)
        print(predictions)
        return {"predict": predictions}
    except ValueError as e:
        raise fastapi.HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        print(e)
        raise fastapi.HTTPException(status_code=400, detail=f'Internal Server Error {e}')


if __name__=='__main__':
    uvicorn.run("api:app",port=8000, reload=True,host="localhost")
