from fastapi import FastAPI
from utils.register import Register
from utils.runner import Runner
from utils.item import Item


app = FastAPI()

@app.post('/main')
def main(args:Item):
    register = Register()
    clear = args.clear
    test = args.test
    face_folder = args.face_folder
    runner = Runner(register, face_folder, test, clear)
    return runner.run()

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=app,
                host="0.0.0.0",
                port=8080,
                workers=1)