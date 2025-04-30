FROM python:3.12

ARG UV_INDEX_RDC_REGISTRY_PASSWORD
ARG UV_INDEX_RDC_REGISTRY_USERNAME

RUN apt-get update \
    && apt-get install -y --no-install-recommends -y \
        build-essential

ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
ENV PATH="/root/.local/bin/:$PATH"

ENV UV_PROJECT_ENVIRONMENT="/usr/local/"

RUN mkdir /app
WORKDIR /app

COPY pyproject.toml /app

RUN if [ ! -f /app/uv.lock ]; then uv sync; else echo "Using existing uv.lock"; fi

RUN uv sync

CMD ["python", "-m", "bot.main"]