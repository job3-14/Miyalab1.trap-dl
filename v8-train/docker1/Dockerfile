FROM python:3.8

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN apt update
RUN apt install -y libgl1-mesa-dev
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN pip install --no-cache-dir -r requirements.txt

COPY . .