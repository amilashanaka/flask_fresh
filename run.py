
from app import app

@app.route('/start',methods=['POST'])
def start():
  return "start"

 
if __name__ == "__main__":
    app.run()