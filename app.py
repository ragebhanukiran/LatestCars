from flask import Flask, render_template, request
import os
import requests

app = Flask(__name__)

@app.route('/')
def home():
    api_key = 'https://www.cardekho.com/api/v1/model/latest?_format=json&cityId=&connectoid=5e61cbfe-3233-3872-4b65-897f43112ed3&sessionid=bf5a036a6cfb6b2f926a5635ecc1ff7c&lang_code=en&regionId=0&page=1&pageSize=30&otherinfo=all&brandId=&styleslug=&noofmonths=&widgets=items%2Cbcd%2Csd%2Cdtl%2Csrt%2Cvt%2Cusc%2Cpopularcb%2Cpt'
    url = f"https://www.cardekho.com/api/v1/model/latest?_format=json&api_key={api_key}&other_parameters_here"
    headers = {
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        actualData = data.get('data')
        vehicles = actualData.get('items')

        for vehicle in vehicles:
            print(vehicle.get('name', 'no name found'))

        return render_template('index.html', cars=vehicles)
    else:
        return f"Error fetching data: {response.status_code}", response.status_code
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

# if __name__ == '__main__':
#     app.run(debug=True)
