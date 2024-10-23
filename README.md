# Rule-Engine-with-Ast
Backend (Python): Handles rule evaluation using AST and exposes an API for the frontend to interact with. Frontend (HTML, CSS, JavaScript): A simple interface that allows users to input rules, see their evaluation results, and interact with the rule engine.

Backend (Python using Flask) The backend will be a Python Flask API where we implement the Rule Engine using AST to evaluate rules.
Install Flask You can install Flask by running:

cmd

pip install Flask Backend Code (Flask + AST Rule Engine)

Backend Explanation: Flask: A lightweight framework to handle the API. RuleEngine: Similar to the previous rule engine using AST, this class takes a context and evaluates rules securely. API Endpoint /evaluate-rule: Accepts a POST request containing the rule and context in JSON format. It evaluates the rule and returns the result.

Frontend (HTML, CSS, JavaScript) This will be a simple frontend that allows users to input rules and context, sends them to the backend, and displays the result.
Frontend Explanation: HTML Form: Contains two inputs, one for entering the context (as JSON) and another for entering the rule. JavaScript: Fetches the API /evaluate-rule, sends the rule and context as JSON, and displays the result on the page. Styling: Basic styling to make the form look clean and functional. Running the Full Stack Application Backend Setup:

Save the Python code to a file (e.g., app.py). Run the Flask application: cmd python ruleEngine.py Frontend Setup:

Create an index.html file with the HTML code provided above. Ensure the index.html is served by the Flask backend or use any simple HTTP server (e.g., python -m http.server) to serve the frontend if it’s separate from the Flask app. Test the Application:

Open the frontend (e.g., http://localhost:5000 if served by Flask) in your browser. Enter some context in JSON format, input a rule, and click the "Evaluate Rule" button to see the result. Example Usage: Context:

json

{ "age": 25, "salary": 50000, "location": "USA", "is_employed": true } Rule age > 18 and salary > 30000 Result:

Result: true
