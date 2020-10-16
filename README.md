# MSc_LangTech_NKUA_DSP
Code for MSc_LangTech_NKUA_DSP courses.

0. If using windows, install git for windows. https://git-scm.com/download/win

1. Create a folder for all your repositories - make sure you know how to navigate there. E.g. create the directory "repos" in "Documents" - full path would be: Documents/repos (assuming you're in the home folder of the current user).

2. Only for the first time you need to get the files in a particular computer, use clone.
-- 2.1 If in windows, open the "Git Bash", else open a terminal and navigate to the repos folder (e.g. type "cd Documents/repos").
-- 2.2 Clone the repository as "git clone https://github.com/maximoskp/MSc_LangTech_NKUA_DSP.git".

3. Any time you want to refresh the content of the repository, navigate to its folder, created in "repos", and type "git pull".

- Basic UNIX commands - to be used in the Git console or in Terminal (if on Mac or Linux):
http://www.econ.ucla.edu/TApages/wan/basic_commands.html


- Install Anaconda

Download and install Anaconda in your machine (Windows / macOS / Linux):

https://www.anaconda.com/products/individual

Open Anaconda navigator and create a new environment *using the latest version of python*. Choose a name for your environment (e.g. name it "audio_dsp").

In the "created environment", install "Jupyter Notebook".

Open Jupyter Notebook - preferably from terminal.

auto open in chromium / or any other browser:

jupyter notebook --generate-config

code jupyter_notebook_config.py # or nano, or whatever browser

change the line 

\# c.NotebookApp.browser = '' 

to 

c.NotebookApp.browser = 'C:/path/to/your/chrome.exe %s' - Caution: backslashes, regardless of windows
Caution: %s at the end


Change color theme:

conda install -c conda-forge jupyterthemes

or 

pip install jupyterthemes

jt -t chesterish


Install interactive extension
pip install ipywidgets
pip install jupyterlab
jupyter labextension install @jupyter-widgets/jupyterlab-manager

You might also need to
conda install matplotlib

- Useful libraries

to install with pip install
numpy
matplotlib
librosa