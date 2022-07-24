from website import create_app

app = create_app()

if __name__ == "__main__": # this wont run if we import this, we have to run this file
    app.run(debug=True)