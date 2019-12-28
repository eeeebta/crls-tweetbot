# Until I make my own markov generator I will be using a library for testing
# https://github.com/jsvine/markovify#installation
# Grabbed quotes from here:
# https://github.com/alvations/Quotables/blob/master/author-quote.txt

import markovify

# Get raw text as string.
with open("Macbeth.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)

# Print five randomly-generated sentences
# for i in range(5):
#     print(text_model.make_sentence())

# Print three randomly-generated sentences of no more than 280 characters
for i in range(128):
    with open("mercberth.txt", "a+") as f:
        f.write(f"{text_model.make_short_sentence(160)}\n")
        text = f.readlines()

