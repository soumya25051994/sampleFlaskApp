from logging import debug
from api import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True) # Make sure this line is enabled when you are pushing the code
    # app.run(debug=True) # Use this line when you are making code changes
