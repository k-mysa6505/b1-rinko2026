FROM python:3.11.17-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    HF_HUB_OFFLINE=1 \
    TRANSFORMERS_OFFLINE=1 \
    WEIGHTS_DIR=/weights

RUN apt-get update \
    && apt-get install -y --no-install-recommends libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install \
    torch==2.14.1+cpu \
    torchvision==0.29.1+cpu \
    --index-url https://download.pytorch.org/whl/cpu

RUN pip install \
    transformers==5.19.0 \
    timm==1.0.30 \
    scipy==1.17.1 \
    numpy==2.4.6 \
    pillow==12.3.0 \
    matplotlib==3.11.2 \
    opencv-python-headless==5.0.0.93 \
    jupyterlab==4.6.4

WORKDIR /workspace
EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", \
     "--ServerApp.root_dir=/workspace", "--IdentityProvider.token=lecture"]
