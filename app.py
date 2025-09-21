from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Serve the main CI/CD test page"""
    return render_template('index.html')

@app.route('/health')
def health():
    """Health check endpoint for monitoring"""
    return {
        'status': 'healthy', 
        'message': 'Chiedozie CI/CD Pipeline is running',
        'version': '1.0.0'
    }

@app.route('/tesa')
def tesa():
    """TESA project endpoint"""
    return {
        'project': 'TESA',
        'status': 'Active Development',
        'description': 'Technical Excellence and System Architecture platform'
    }

@app.route('/qucoon')
def qucoon():
    """Qucoon project endpoint"""
    return {
        'project': 'Qucoon',
        'status': 'Beta Testing',
        'description': 'Quick User Communication and Operations Network'
    }

@app.route('/pipeline')
def pipeline():
    """Pipeline status endpoint"""
    return {
        'project': 'Pipeline Core',
        'status': 'Production Ready',
        'description': 'Advanced CI/CD pipeline orchestration system'
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)