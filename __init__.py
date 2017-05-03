from flask import Flask, render_template, request
import sqlite3, datetime


app = Flask(__name__)
conn = sqlite3.connect('database.db')

#conn.execute('CREATE TABLE videos (name TEXT, url TEXT, category TEXT, comment TEXT, image TEXT, dateT TEXT, uniqueID TEXT, title TEXT)')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/goHome')
def goHome():
    return render_template('index.html')

#when user presses submit on the form, this retrieves all of the info about the video and puts it in the database table
@app.route('/getNewVideo', methods = ['POST', 'GET'])
def getNewVideo():
    conn = sqlite3.connect('database.db')
    if request.method == 'POST':
        # try:
        nm = request.form['nm']
        URL = request.form['URL']
        categ = request.form['cat']
        com = request.form['comment']
        titleText = request.form['title']

        unique = ""
        for i in range (len(URL)):
            if(URL[i] == '='):
                unique = URL[i+1:]
                break

        imageURL = "https://img.youtube.com/vi/" + unique + "/maxresdefault.jpg"

        currentDateTime = datetime.datetime.now()
        # print(currentDateTime.year())
        currentDate = str(currentDateTime.year) + "-" + str(currentDateTime.month) + "-" + str(currentDateTime.day)

        with sqlite3.connect('database.db') as conn:
            print("Hello")

            cur = conn.cursor()
            cur.execute("INSERT INTO videos (name, url, category, comment, image, dateT, uniqueID, title) VALUES(?, ?, ?, ?, ?, ?,?,?)",(nm, URL, categ, com, imageURL,currentDate, unique, titleText))
            conn.commit()
            msg = "Successfully added"
        # except:
        #     conn.rollback()
        #     msg = "error in insert"
        #
        # finally:
        return render_template('index.html')
        conn.close()

#used for testing purposes to list everything currently in the database table
@app.route('/listVideos')
def listVideos():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()
    cur.execute('select * from videos ')

    row = cur.fetchall()

    return render_template("list.html", row = row)

#when a user clicks on a video, this retrieves the specific video parameters encoded in the URL and sends them to the template
@app.route('/getParams')
def getParams():
    description = request.args.get('description')
    user = request.args.get('name')
    unique = request.args.get('uniqueID')
    title = request.args.get('title')
    dateT = request.args.get('dateT')

    return render_template('indivVideo.html', description = description, name = user,  uniqueID = unique,
                           title = title, dateT = dateT)

@app.route('/listVideosFootball')
def listVideosFootball():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()
    cur.execute('select * from videos WHERE category = "Football"')

    rows = cur.fetchall()

    return render_template("soccer.html", row = rows)

@app.route('/listVideosSoccer')
def listVideosSoccer():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()
    cur.execute('select * from videos WHERE category = "Soccer"')

    rows = cur.fetchall()

    return render_template("soccer.html", row = rows)

@app.route('/listVideosBasketball')
def listVideosBasketball():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()
    cur.execute('select * from videos WHERE category = "Basketball"')

    rows = cur.fetchall()

    return render_template("soccer.html", row = rows)

@app.route('/listVideosOSports')
def listVideosOSports():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()
    cur.execute('select * from videos WHERE category = "Other Sports"')

    rows = cur.fetchall()

    return render_template("soccer.html", row = rows)

@app.route('/listVideosClassical')
def listVideosClassical():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()
    cur.execute('select * from videos WHERE category = "Classical"')

    rows = cur.fetchall()

    return render_template("soccer.html", row = rows)


@app.route('/listVideosPop')
def listVideosPop():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()
    cur.execute('select * from videos WHERE category = "Pop"')

    rows = cur.fetchall()

    return render_template("soccer.html", row = rows)

@app.route('/listVideosInstrumental')
def listVideosInstrumental():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()
    cur.execute('select * from videos WHERE category = "Instrumental"')

    rows = cur.fetchall()

    return render_template("soccer.html", row = rows)

@app.route('/listVideosOMusic')
def listVideosOMusic():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()
    cur.execute('select * from videos WHERE category = "Other Music"')

    rows = cur.fetchall()

    return render_template("soccer.html", row = rows)

@app.route('/listVideosAction')
def listVideosAction():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()
    cur.execute('select * from videos WHERE category = "Action"')

    rows = cur.fetchall()

    return render_template("soccer.html", row = rows)

@app.route('/listVideosComedy')
def listVideosComedy():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()
    cur.execute('select * from videos WHERE category = "Comedy"')

    rows = cur.fetchall()

    return render_template("soccer.html", row = rows)


@app.route('/listVideosDocumentary')
def listVideosDocumentary():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()
    cur.execute('select * from videos WHERE category = "Documentary"')

    rows = cur.fetchall()

    return render_template("soccer.html", row = rows)

@app.route('/listVideosOMovies')
def listVideosOMovies():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()
    cur.execute('select * from videos WHERE category = "Other Movies"')

    rows = cur.fetchall()

    return render_template("soccer.html", row = rows)


@app.route('/listVideosO')
def listVideosO():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()
    cur.execute('select * from videos WHERE category = "Others"')

    rows = cur.fetchall()

    return render_template("soccer.html", row = rows)


if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=80)