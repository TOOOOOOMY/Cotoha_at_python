# 参考
# https://qiita.com/shonansurvivors/items/0fbcbfde129f2d26301c

from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# long_description(後述)に、GitHub用のREADME.mdを指定
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Cotoha_at_python', # パッケージ名(プロジェクト名)
    packages=['cotohacall'], # パッケージ内(プロジェクト内)のパッケージ名をリスト形式で指定
    version='1.0.0',
    license='MIT',
    install_requires=[], # pip installする際に同時にインストールされるパッケージ名をリスト形式で指定
    author='TOOOOOOMY',
    author_email='10talatgi@gmail.com',
    url='https://github.com/TOOOOOOMY/Cotoha_at_python', # パッケージに関連するサイトのURL(GitHubなど)

    description='Make it easy to use Japanese processing API, Cotoha.', # パッケージの簡単な説明
    long_description=long_description, # PyPIに'Project description'として表示されるパッケージの説明文
    long_description_content_type='text/markdown', # long_descriptionの形式を'text/plain', 'text/x-rst', 'text/markdown'のいずれかから指定
    keywords='cotoha cotohacall Cotoha', # PyPIでの検索用キーワードをスペース区切りで指定

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ], # パッケージ(プロジェクト)の分類。https://pypi.org/classifiers/に掲載されているものを指定可能。
)
