from flask import Flask, render_template, request

app = Flask(__name__)

# Store licenses in a list for demonstration (replace this with a database in production)
licenses = []

@app.route('/')
def index():
    return render_template('index.html')

# Route for the license page
@app.route('/license', methods=['GET', 'POST'])
def license_page():
    if request.method == 'POST':
        email = request.form['email']
        unique_id = request.form['unique_id']
        valid_from = request.form['valid_from']
        expire_on = request.form['expire_on']
        
        # Generate a simple license key (for demonstration purposes)
        license_key = f"{unique_id}-{valid_from.replace('-', '')}-{expire_on.replace('-', '')}"
        
        # Store the license data
        licenses.append({
            'email': email,
            'unique_id': unique_id,
            'valid_from': valid_from,
            'expire_on': expire_on,
            'license_key': license_key,
        })
        
        return render_template('license.html', response={
            'license_key': license_key,
            'unique_id': unique_id,
            'valid_from': valid_from,
            'expire_on': expire_on
        })
    
    return render_template('license.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Change the port if necessary
