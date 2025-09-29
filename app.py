from flask import Flask

import iam.application.services
from health.interfaces.services import health_api
from iam.interfaces.services import iam_api
from shared.infrastructure.database import init_db

app = Flask(__name__)
app.register_blueprint(iam_api)
app.register_blueprint(health_api)

first_request = True

def setup():
    global first_request
    if first_request:
        first_request = False
        init_db()
        auth_application_service = iam.application.services.AuthApplicationService()
        auth_application_service.get_or_create_test_device()


@app.route('/')
def about_edge_service():  # put application's code here
    return 'Smart Band Edge Service. Visit /api/v1/health-monitoring/data-records to POST health data.'

if __name__ == '__main__':
    app.run(debug=True)
