FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y texlive-latex-base texlive-latex-recommended texlive-latex-extra \
    texlive-fonts-recommended texlive-lang-all && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    apt-get install -y ghostscript imagemagick && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


WORKDIR /app

COPY generate_pdf.py /app/generate_pdf.py
COPY image.png /app/image.png

RUN mkdir /app/output

RUN python -m venv /app/venv
RUN /app/venv/bin/pip install my-latex-lib

COPY run_app.sh /app/run_app.sh
RUN chmod +x /app/run_app.sh

CMD ["./run_app.sh"]
