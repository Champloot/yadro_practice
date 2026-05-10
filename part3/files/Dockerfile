FROM ubuntu:22.04

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
	python3 \
	python3-pip \
	&& rm -rf /var/lib/apt/lists/* \
	&& apt-get clean

RUN useradd --create-home --shell /bin/bash checker

WORKDIR /app
RUN chown checker:checker /app

COPY --chown=checker:checker requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY --chown=checker:checker http_checker.py .

USER checker

CMD ["python3", "http_checker.py"]
