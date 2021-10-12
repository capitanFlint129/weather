from weather_statistics.app import create_app

jenkins_test_line = 'a'

if __name__ == '__main__':
    app = create_app()
    app.run()
