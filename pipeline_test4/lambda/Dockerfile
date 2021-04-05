# Define base Docker image
ARG DEPLOY_BASE_IMAGE="public.ecr.aws/lambda/python:3.8" 

# Define custom directories 
ARG LAYER_DIR="/opt"

# Build output image
FROM ${DEPLOY_BASE_IMAGE}
ARG LAYER_DIR

WORKDIR ${LAYER_DIR}

# Copy in handler.py
# See https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html
COPY handler.py ${LAMBDA_TASK_ROOT}

RUN python -m compileall .

CMD [ "handler.handler" ]