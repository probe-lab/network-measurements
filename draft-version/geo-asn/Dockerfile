FROM vgiotsas/p2p-observatory-base
LABEL stage=builder
WORKDIR /app
ADD . .
RUN make build
RUN python3 -m pip install -r requirements.txt
WORKDIR /app
ADD . .
ENV SHELL /bin/bash
RUN chmod +x ./start_crawl
RUN chmod +x ./plan_executable.sh
RUN chmod +x ./aws_sync
CMD ["./plan_executable.sh"]