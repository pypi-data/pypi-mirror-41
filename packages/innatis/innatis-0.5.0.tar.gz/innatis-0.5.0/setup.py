from setuptools import setup
setup(
  name='innatis',
  install_requires=['scikit-learn',
                    'scipy',
                    'sklearn-crfsuite',
                    'tensorflow',
                    'word2number',
                    'rasa_nlu==0.13.8',
                    'tensorflow-hub',
                    'spacy'],
  packages=['innatis', 'innatis.featurizers', 'innatis.extractors'],
  version='0.5.0',
  description='A library of useful custom Rasa components',
  author='CarLabs',
  author_email='blake@carlabs.com',
  url='https://github.com/Revmaker/innatis',
  download_url='https://github.com/Revmaker/innatis/tarball/0.1',
  keywords=['rasa', 'nlu', 'components'],
  classifiers=[]
)
