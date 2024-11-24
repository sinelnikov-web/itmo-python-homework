# LaTeX generator

## Run

### .tex generator

```bash
python homework_2/generate_pdf.py
```

### .pdf generator

```bash
cd homework_2
docker build -t my_latex_image .
docker run --rm -v "$(pwd)/output":/app/output my_latex_image
```
