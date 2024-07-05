from flask import Flask, render_template
import mysql.connector


app = Flask(__name__)

# Function to retrieve data from the database
def get_data_from_database():
    data = []
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='collegedb'
        )
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM scrapedemo")
        data = cursor.fetchall()
        
    except mysql.connector.Error as error:
        print("Error retrieving data from MySQL table:", error)
        
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

    return data
        
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dietplanner.html')
def dietplanner():
    data = get_data_from_database()
    return render_template('dietplanner.html', data = data)

@app.route('/telemedicine.html')
def telemedicine():
    return render_template('telemedicine.html')

if __name__ == '__main__':
    app.run(debug=True)