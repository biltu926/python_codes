import json
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

def plot_histogram(scores):
    num_bins = 20
    n, bins, patches = plt.hist(scores, num_bins,facecolor='blue')
    plt.ylabel('Frequency')
    plt.xlabel('Scores assigned')
    plt.title('Document Filtering; Threshold: 0.05')
    plt.style.use('ggplot')
    plt.show()

def doc_vs_ctx_plot(ctx_list, ctx_doc_map):
    ''' Plot document numbers vs contexts '''
    ctx_scores = [len(ctx_doc_map[c]) for c in ctx_doc_map]
    plt.bar(ctx_list, ctx_scores, align='center', alpha=0.5)
    plt.title('Context wise document frequency')
    plt.ylabel('document frequency')
    plt.show()

def doc_vs_score():
    ''' Plot documents vs scores '''

def main():
    score_file='C:\\data\\work\\supratim\\corpus_generator\\others\\document_scores'
    with open(score_file, 'r') as fp:
        scores = fp.read()
    scores = json.loads(scores)
    all_ctx = []
    ctx_doc_map = {}
    score_list = []
    more_files = []

    print(scores)

    for doc_name, value in scores.items():
        ctx_name = list(value.keys())[0]
        if ctx_name not in all_ctx:
            all_ctx.append(ctx_name)
        score_list.append(value[ctx_name])
        if value[ctx_name] <= 0.02:
            more_files.append(value[ctx_name])
        if ctx_name not in ctx_doc_map:
            ctx_doc_map[ctx_name] = [doc_name]
        else:
            ctx_doc_map[ctx_name].append(doc_name)

    #plot_histogram(score_list)
    #doc_vs_ctx_plot(all_ctx, ctx_doc_map)
    plot_histogram(more_files)

if __name__=='__main__':
    main()