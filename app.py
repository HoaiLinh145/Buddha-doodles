from flask import Flask,render_template

app = Flask(__name__)
class Doodle:
    def __init__(self,title,img):
        self.title=title
        self.img=img
doodles= [
    Doodle("First step","http://images.huffingtonpost.com/2013-05-17-BuddhaDoodles_Breathe_text_web.jpg"),
    Doodle("next","http://cdn.shopify.com/s/files/1/0235/6341/files/Buddha_Doodles_lifeisart_MollyHahn_grande.jpg?4865"),
    Doodle ("shining","https://thegooglesutra.files.wordpress.com/2015/11/buddha-doodles-paris-2.jpg"),
    Doodle("live","http://data.whicdn.com/images/195903489/large.jpg"),

]


@app.route('/')
def Welcome_page():
    return 'Good to see you, buddy!'

@app.route('/doodles')
def get_doodles():
    return render_template('content.html',
                           doodle_list=doodles,
                           )

if __name__ == '__main__':
    app.run()
