import numpy as np
import pickle5 as pickle
import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential

model = keras.models.load_model('./models/review_anal_model_v2.h5')
with open('./src/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

def predict_sentiment(text):
    # Tokenize and pad the input text
    text_sequence = tokenizer.texts_to_sequences([text])
    text_sequence = pad_sequences(text_sequence, maxlen=100)

    # Make a prediction using the trained model
    predicted_rating = model.predict(text_sequence)[0]

    negative_threshold = 0.4
    positive_threshold = 0.6

    if predicted_rating[0] >= negative_threshold and predicted_rating[1] <= positive_threshold:
        return 'Neutral' + str(predicted_rating)
    elif np.argmax(predicted_rating) == 0:
        return 'Negative' + str(predicted_rating)
    else:
        return 'Positive' + str(predicted_rating)
    
if __name__ == "__main__":
    ## Replace this string here
    text_input = "It was amazing"
    
    predicted_sentiment = predict_sentiment(text_input)
    print(predicted_sentiment)