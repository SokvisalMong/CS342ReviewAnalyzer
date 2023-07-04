import tkinter as tk
from analyze import predict_sentiment

def analyze_text():
    text_input = input_text.get("1.0", "end-1c")
    predicted_sentiment = predict_sentiment(text_input)
    sentiment_label.config(text=predicted_sentiment)

# Create the main window
window = tk.Tk()
window.title("Sentiment Analysis")

# Create the input text field
input_text = tk.Text(window, height=10, width=50, padx= 50, pady=50)
input_text.pack()

# Create the analyze button
analyze_button = tk.Button(window, text="Analyze", command=analyze_text)
analyze_button.pack()

# Create the label for displaying the sentiment
sentiment_label = tk.Label(window, text="")
sentiment_label.pack()

# Start the main event loop
window.mainloop()
