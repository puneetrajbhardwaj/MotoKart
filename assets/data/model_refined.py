
# SETUP FOR LIBRARIES AND TOOLS
##################################################################################
def setup():
    import os
    os.system('pip install --user tensorflow')
    os.system('pip install tflearn numpy nltk random json pickle')
    os.system('python -m nltk.downloader all')
##################################################################################


# IMPORT JSON DATABASE HERE
##################################################################################
import json
with open("intents.json") as file:
    data = json.load(file)
##################################################################################


# PROCESSING DATA HERE
##################################################################################
def process_data(load = True):
    import numpy
    import pickle
    import nltk
    from nltk.stem.lancaster import LancasterStemmer
    stemmer = LancasterStemmer()

    
    try:
        with open("data.pickle", "rb") as f:
            words, labels, training, output = pickle.load(f)
            return words, labels, training, output
    except:
        print("the data seems to be missing.... preparing one")
        words = []
        labels = []
        docs_x = []
        docs_y = []

        for intent in data["intents"]:
            for pattern in intent["patterns"]:
                wrds = nltk.word_tokenize(pattern)
                words.extend(wrds)
                docs_x.append(wrds)
                docs_y.append(intent["tag"])

            if intent["tag"] not in labels:
                labels.append(intent["tag"])

        words = [stemmer.stem(w.lower()) for w in words if w != "?"]
        words = sorted(list(set(words)))

        labels = sorted(labels)

        training = []
        output = []

        out_empty = [0 for _ in range(len(labels))]

        for x, doc in enumerate(docs_x):
            bag = []

            wrds = [stemmer.stem(w.lower()) for w in doc]

            for w in words:
                if w in wrds:
                    bag.append(1)
                else:
                    bag.append(0)

            output_row = out_empty[:]
            output_row[labels.index(docs_y[x])] = 1

            training.append(bag)
            output.append(output_row)


        training = numpy.array(training)
        output = numpy.array(output)

        with open("data.pickle", "wb") as f:
            pickle.dump((words, labels, training, output), f)

    return [words, labels, training, output]
##################################################################################

# MODEL
##################################################################################
def TF_model(predict = False, data=None):
    import tensorflow
    import tflearn

    training, output = process_data()[2], process_data()[3]

    tensorflow.compat.v1.reset_default_graph()

    net = tflearn.input_data(shape=[None, len(training[0])])
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
    net = tflearn.regression(net)

    model = tflearn.DNN(net)
    
    try:
        model.load("model/model.tflearn")

    except ValueError or FileNotFoundError:
        print('the file seems to be missing. please wait while I train')
        import os
        model = tflearn.DNN(net)
        model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
        os.system('mkdir model')
        model.save("model/model.tflearn")
    
    if predict == True:
        if data != None:
            # print("printing your respomse")
            # print(data)
            response = model.predict(data)
            return response
        else:
            print('The data seems to be missing')
##################################################################################


def bag_of_words(s, words):
    import numpy
    import nltk
    from nltk.stem.lancaster import LancasterStemmer
    stemmer = LancasterStemmer()

    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            
    return numpy.array(bag)


# CHATBOT MAIN FUNCTION
##################################################################################
def chat(inp):
    import random
    import numpy

    # print("Start talking with the bot (type quit to stop)!")
    # while True:
    # if inp.lower() == "quit":
    #     break

    words, labels = process_data()[0], process_data()[1]

    results = TF_model(data=[bag_of_words(inp, words)],  predict=True)
    results_index = numpy.argmax(results)
    # print(results_index)
    tag = labels[results_index]

    for tg in data["intents"]:
        if tg['tag'] == tag:
            responses = tg['responses']

    return random.choice(responses)
##################################################################################


# process_data()
# TF_model()

# while True:
#     inp = input("You > ")
#     if inp.lower() == "quit":
#         break
#     print("Bot: ", chat(inp))
