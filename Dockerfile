FROM tensorflow/tensorflow
WORKDIR /bot
COPY requirements-deploy.txt /bot/
RUN pip install --upgrade pip
RUN pip install -r requirements-deploy.txt
COPY . /bot
CMD python chat-discord.py