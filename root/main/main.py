from root.main.dependency_injection_init import injector
from root.main.flask_initializer import FlaskInitializer


if __name__ == "__main__":
    injector.get(FlaskInitializer).app_instance.run(debug=False)
