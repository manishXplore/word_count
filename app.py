from flask import Flask, render_template, request

app = Flask(__name__)

def process_paragraph(paragraph):
    words = paragraph.split()
    word_counts = []
    for i, word in enumerate(words):
        count = words.count(word)
        if (word, i, count) not in word_counts:
            word_counts.append((word, i, count))
    total_words = len(words)
    return total_words, word_counts

@app.route('/textanalyzerold', methods=['GET', 'POST'])
def word_counter():
    if request.method == 'POST':
        paragraph = request.form['paragraph']
        total_words, word_counts = process_paragraph(paragraph)
        return render_template('index.html', paragraph=paragraph, total_words=total_words, word_counts=word_counts)
    return render_template('index.html')

def process_paragraph1(paragraph):
    words1 = paragraph.split()
    word_details = []
    word_details = [(v, i, words1.index(v), words1.count(v)) for i, v in enumerate(words1)]
    
    return(word_details)

@app.route('/textanalyzernew', methods=['GET', 'POST'])
def word_counter1():
    if request.method == 'POST':
        paragraph = request.form['paragraph']
        word_details = process_paragraph1(paragraph)
        return render_template('index.html', paragraph=paragraph, word_details=word_details)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
