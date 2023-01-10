from fastapi import FastAPI

import action

app = FastAPI()

@app.get("/mycarService")
async def mycar(regnum, owner):
    return await action.inquiry(regnum, owner)
   
if __name__=="__main__":
    import uvicorn
    import config
    uvicorn.run(app, host=config.env["service_host"], port=config.env["service_port"], log_config=config.env["logging_config"])
