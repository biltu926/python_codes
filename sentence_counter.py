import os
import time
import logging
import cProfile
import threading
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.INFO,
                    filename='sentence_counter_log.log',
                    format='%(asctime)s : %(levelname)s : %(message)s',
                    filemode='w')
logger = logging.getLogger('sentence_counter')
config = {
          'conll_dirs': '/home/parabole/automation/learning/conll_files',
          'output_dir': '/home/parabole/automation/learning',
          'stat_file': '/home/parabole/automation/learning'
         }
number_of_sentences = 0
files_processed = 0

def count_sentence(file_path):
    global number_of_sentences
    global files_processed

    logger.info(f'THREAD {threading.current_thread().name} FOR {os.path.basename(file_path)} STARTED AT: {time.ctime()}')
    with open(file_path, 'r', encoding='utf-8') as fp:
        conll_content = fp.read()
        number_of_sentences += len(conll_content.split('\n\n'))
    files_processed += 1
    logger.info(f'THREAD {threading.current_thread().name} FOR {os.path.basename(file_path)} ENDED AT: {time.ctime()}')
    logger.info(f'FILES PROCESSED SO FAR: {files_processed}')
def main():
    global number_of_sentences
    global files_processed
    start = time.ctime()
    thread = ThreadPoolExecutor(max_workers=8)
    conll_files = os.listdir(config.get('conll_dirs'))
    threads = []
    for file in conll_files:
        future = thread.submit(count_sentence, os.path.join(config.get('conll_dirs'), file))
        threads.append(future)

    for t in threads:
        logger.info(t.result())
    end = time.ctime()
    with open(os.path.join(config.get('output_dir'), 'sent_count'), 'w') as fp:
        fp.writelines('\n'.join([f'Total files traversed: {files_processed}',
                                 f'Total sentences: {number_of_sentences},'
                                 f'Started: {start}',
                                 f'Ended: {end}']))

if __name__=='__main__':
    #main()
    cProfile.run('main', os.path.join(config.get('stat_file'), 'sent_count_profile'))

    #while True:
    #    time.sleep(3)