import shutil
import os
if os.path.exists('chat_model'):
    print('deleting old data')
    shutil.rmtree('chat_model')
if os.path.exists('tokenizer.pickle'):
    print('deleting tokenizer')
    os.unlink('tokenizer.pickle')
if os.path.exists('label_encoder.pickle'):
    print('deleting encoder')
    os.unlink('label_encoder.pickle')