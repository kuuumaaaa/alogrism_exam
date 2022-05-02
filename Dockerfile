FROM continuumio/anaconda3:latest

# reproject の pip install に gcc が必要だったので
# apt install しておきます
RUN apt update && \
    apt install -y build-essential

# ホスト PC の data フォルダへ繋ぐ入口です
RUN mkdir /work

# jupyter の起動パラメータを設定します
EXPOSE 8888
# CMD ["jupyter", "notebook", \
#      "--port=8888", \
#      "--ip=0.0.0.0", \
#      "--allow-root", \
#      "--no-browser", \
#      "--NotebookApp.token=''", \
#      "--NotebookApp.notebook_dir='/work'"]