from flask import Flask, render_template
from firebase import firebase
from FirePut import .forms




app = Flask(__name__)

firebase = firebase.FirebaseApplication('https://cs196-videos.firebaseio.com/', None)
#firebase.put('Category/Sports/baseball',"name", 'wilma')
#firebase.post('Category/Music/country', {'name': "Thomas Rhett", 'url': "kjdfjkd.com"})

print()

@app.route('/')

def hello():
    return render_template('SportsPage.html')

# count = 0
# def fireput():
#     form = firePut()
#     If form.validate_on_submit():
#         global count
#         count += 1
#         putData = {‘Title’ : form.title.data, ‘Field’ : form.field.data, ‘URL’ : form.url.data, 'Author' : form.author.data, 'Description' : form.description.data}
#         field = form.category.data
#         firebase.put(‘/category/field’, ‘video’ + str(count), putData)
#         return render_template(‘api-put-result.html’, form=form, putData=putData)
#     return render_template(‘My-Form.html’)



if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
