from fastapi import FastAPI
myapp=FastAPI()

@myapp.get( '/' )

def index():
    return {'data':'blog list'}

@myapp.get('/blog/unpublished')
def unpublished():
    return{'data':'all unpublished blog'}

@myapp.get('/blog/{id}')
def show(id:int):
    return {'data': id}

@myapp.get('/blog/{id}/comment')
def comment(id):
    return{'data':{'1','2'}}
    

