from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=False, port=5054, host='127.0.0.1')