FROM python:3.12

WORKDIR /app

RUN pip install uv 

COPY . .

RUN uv sync

CMD ["uv", "run", "python", "-m", "src.cli"]