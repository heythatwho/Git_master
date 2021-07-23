import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

def summarize():
   
    url=utext.get("1.0","end").strip()

    article = Article(url)

    article.download()
    article.parse()

    article.nlp()

    title.config(state="normal")
    author.config(state="normal")
    publication.config(state="normal")
    summary.config(state="normal")
    tag.config(state="normal")
    sentiment.config(state="normal")

    title.delete("1.0","end")
    title.insert("1.0", article.title)

    aut = article.authors or 'NA'
    author.delete("1.0",'end')
    author.insert("1.0",str(f"{aut}"))

    pub = article.publish_date or "NA"
    publication.delete("1.0","end")
    publication.insert("1.0", str(f"{pub}"))

    summary.delete("1.0","end")
    summary.insert("1.0", article.summary)

    tag.delete("1.0","end")
    tag.insert("1.0", article.keywords)

    analysis= TextBlob(article.text)
    sentiment.delete("1.0","end")
    #print(analysis.sentiment)
    sentiment.insert("1.0", f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')


    title.config(state="disabled")
    author.config(state="disabled")
    publication.config(state="disabled")
    summary.config(state="disabled")
    tag.config(state="disabled")
    sentiment.config(state="disabled")
    #print(f"Title: {article.title}")
    #print(f"Authors: {article.authors}")
    #print(f"Publication Date: {article.publish_date}")
    #print(f"Summary: {article.summary}")


root=tk.Tk()
root.title("article summary automation -by IssacM")
root.geometry("1200x600")

tlabel=tk.Label(root, text="Title")
tlabel.pack()

title=tk.Text(root, height=1, width=140)
title.config(state="disabled", bg="#dddddd")
title.pack()

alabel=tk.Label(root, text="Author")
alabel.pack()

author=tk.Text(root, height=1, width=140)
author.config(state="disabled", bg="#dddddd")
author.pack()

plabel=tk.Label(root, text="Publishing Date")
plabel.pack()

publication=tk.Text(root, height=1, width=140)
publication.config(state="disabled", bg="#dddddd")
publication.pack()

slabel=tk.Label(root, text="Summary")
slabel.pack()

summary=tk.Text(root, height=20, width=140)
summary.config(state="disabled", bg="#dddddd")
summary.pack()

klabel=tk.Label(root, text="Tags")
klabel.pack()

tag=tk.Text(root, height=2, width=140)
tag.config(state="disabled", bg="#dddddd")
tag.pack()


selabel=tk.Label(root, text="Sentiment Analysis")
selabel.pack()

sentiment=tk.Text(root, height=1, width=140)
sentiment.config(state="disabled", bg="#dddddd")
sentiment.pack()

ulabel=tk.Label(root, text="URL")
ulabel.pack()

utext=tk.Text(root, height=1, width=140)
utext.pack()

btn=tk.Button(root, text="Summarize it", command=summarize)
btn.pack()

root.mainloop()
