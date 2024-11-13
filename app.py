from app import create_app

app = create_app()

if __name__ == '__main__':
    # Development mode.
    app.run(debug=True)
    # app.run()