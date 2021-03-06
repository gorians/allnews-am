import argparse
import os
import logging

import gensim.models

logging.basicConfig(
        format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
file_dir = os.path.dirname(os.path.realpath(__file__))


def main(args):
    model = gensim.models.Word2Vec.load(
        os.path.join(file_dir, '../allnews_am/models/', args.model_name))

    logging.info('Evaluating YerevaNN-Analogies')
    model.wv.evaluate_word_analogies(
        os.path.join(file_dir,
                     '../allnews_am/data/yerevann_analogies.txt'))

    logging.info('Evaluating Avetisyan-Ghukasyan-Analogies')
    model.wv.evaluate_word_analogies(
          os.path.join(file_dir,
                       '../allnews_am/data/avetisyan_ghukasyan_analogies.txt'))

    print(f'Vocabulary size: {len(model.wv.vocab)}')
    print('Most common words: ', [
          (model.wv.index2word[i], model.wv.vocab[model.wv.index2word[i]].count)
          for i in range(10)
    ])
    similar_words_to = 'Փաշինյան'
    print(f'Most similar to "{similar_words_to}"',
          model.wv.most_similar(similar_words_to))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
            '--model_name', default='word2vec.model',
            help='The name of the model file in the models folder.')
    word2vec_args = parser.parse_args()
    main(word2vec_args)
