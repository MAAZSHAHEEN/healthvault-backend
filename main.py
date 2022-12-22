from fastapi import FastAPI
app=FastAPI()

@app.get( '/' )

def index():
    return {'data':{'name':'maaz'}}

@app.get('/about')
def about():
    return 'maaz'
