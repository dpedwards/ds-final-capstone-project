from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

def wordcloud(text):
    wordcloud = WordCloud(
    width = 500,
    height = 250,
    max_words= 100,
    background_color = 'white',
    stopwords = STOPWORDS).generate(str(text))
    fig = plt.figure(
    figsize = (40, 30),
    facecolor = 'k',
    edgecolor = 'k')
    plt.imshow(wordcloud, interpolation = 'bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()
