from flask import Flask,render_template
from datetime import datetime
import platform
import subprocess

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    sys_data = {"current_time": '',"machine_name": ''}
    try:
        sys_data['current_time'] = datetime.now().strftime("%d-%b-%Y , %I : %M : %S %p")
        sys_data['machine_name'] = platform.node()

    except Exception as ex:
        print(ex)

    finally:
        return render_template("index.html",title='Raspberry Pi - System Information',
                               sys_data = sys_data)

if __name__ == "__main__":
    app.run(debug=True)