
import os.path


from .mdict_query import IndexBuilder


def init_mdict(mdict_dir):
    mdicts = {}
    for root, dirs, files in os.walk(mdict_dir):
        for fname in files:
            if fname.endswith('.mdx'):
                print('Initialize MDICT "%s", please wait...' % fname)
                mdx_file = os.path.join(root, fname)
                idx = IndexBuilder(mdx_file)
                mdicts[fname] = idx
    return mdicts


def lookup(mdict, word):
    return mdict.mdx_lookup(word)
