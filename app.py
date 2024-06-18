from flask import Flask,render_template,send_file
import matplotlib.pyplot as plt 
import pandas as pd 
app=Flask(__name__,template_folder='template')

def generateplot():
    data=pd.read_csv("data.csv")
    plt.switch_backend('Agg')
    plt.figure(figsize=(10,6))
    plt.bar(data['countries'],data['companies'],color='blue')
    plt.xlabel('country')
    plt.ylabel('companies')
    plt.title('bargraph')
    plt.savefig('static/companies.png')
@app.route('/')
def index():
    generateplot()
    fig='static/companies.png'
    return render_template('index.html',plot_fig=fig)
app.route('/static/<path:filename>')
def serve_static(filename):
    return send_file(f'static/{filename}')
if __name__=='__main__':
    app.run(debug=True)

