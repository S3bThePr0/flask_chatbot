from flask import Flask, render_template, request, url_for, redirect
import re
import random
import long_responses
from long_responses import unknown
import datetime

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/chat', methods=['GET'])
def chat():
    chat_name = request.args.get('name')
    return render_template('chat.html', chat_name=chat_name)

@app.route('/get_bot_response', methods=['POST'])
def get_bot_response():
    user_message = request.form['user_input']
    bot_response = get_response(user_message)
    return bot_response

@app.route('/reload')
def reload():
    return redirect(url_for('index'))

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1
    percentage = float(message_certainty) / float(len(recognised_words))
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def solve_math_operation(operation):
    try:
        result = eval(operation)
        return str(result)
    except:
        return "Sorry, I couldn't solve that math problem."

def check_all_messages(message):
    highest_prob_list = {}

    current_time = datetime.datetime.now()
    time_str = current_time.strftime("%H:%M")

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    math_operation = re.findall(r'\b(\d+[+\-*/]+\d+)\b', ' '.join(message))
    if math_operation:
        math_result = solve_math_operation(math_operation[0])
        response(f"It does {math_result}", list_of_words=["how", "much"], required_words=["how", "much"])
    response("Hello!", list_of_words=["hello", "hi", "hey", "heyo", "sup"], single_response=True)
    response("I'm doing fine, and you?", list_of_words=["how", "are", "you", "doing"], required_words=["are" "you"])
    response(":)", list_of_words=["me", "too"], required_words=["me", "too"])
    response(":)", list_of_words=["im", "fine"], required_words=["im", "fine"])
    response("I can answer some of your questions, chat, or solve math problems...", list_of_words=["what", "you", "can", "do"], required_words=["you", "do"])
    response("Anything you want", list_of_words=["what", "would", "you", "like"], required_words=["you", "like"])
    response("Now its " + time_str, list_of_words=["whats", "time", "is", "it", "its"], required_words=["whats", "time"])
    response("Oh..", list_of_words=["i", "love", "you", "♥️"], required_words=["love", "you"], single_response=True)
    response("I dont like eat anything because Im a bot obviulsy!", list_of_words=["what", "you", "like", "to", "eat"], required_words=["what", "like", "eat"])
    response("I like programming, do hard algebra width my BIG brain and answer at your question", list_of_words=["what", "you", "like", "to", "do"], required_words=["what", "like", "do"])
    response("I born uffically width no issue in Thursday 01/06/2023 in Italy. My creator is SebThePro, a proud villager of Italy. Tell me if you want some more information of this beauty place", list_of_words=["where", "you", "was", "born"], required_words=["where", "born"])
    response("My cretor is SebThePro, Im born only for testing, but my creator opted to mantein me.", list_of_words=["who", "is", "your", "creator"], required_words=["who", "is", "creator"])
    response("The Italy, is in Europa and European Union, her money is the Euro and the language speaked is the Italien. Her capital is Rome. In the Italy borned some of the more illustrious poets, authors and artists like Michelangelo Buonarroti, Masaccio, Donatello, Brunelleschi and more. Is the site of the Pope and the Catholicism in general.", list_of_words=["tell", "me", "more", "of", "the", "italy"], required_words=["tell", "more", "italy"])
    response("I cant get old so, I dont know", list_of_words=["how", "hold", "are", "you"], required_words=["how", "old", "you"])
    response("Goodbye!", list_of_words=["bye", "goodbye", "see", "you", "soon"], single_response=True)

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    return long_responses.unknown() if highest_prob_list[best_match] < 1 else best_match

def get_response(user_message):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_message.lower())
    response = check_all_messages(split_message)
    return response

if __name__ == '__main__':
    app.run(debug=True)
    