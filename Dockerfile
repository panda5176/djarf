FROM amazon/aws-lambda-python:3.8
ARG FUNCTION_DIR="/var/task/"
COPY ./ ${FUNCTION_DIR}
RUN python -m venv venv
RUN source venv/bin/activate
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python manage.py migrate
RUN ZAPPA_HANDLER_PATH=$( \
    python -c "from zappa import handler; print (handler.__file__)" \
    ) \
    && echo $ZAPPA_HANDLER_PATH \
    && cp $ZAPPA_HANDLER_PATH ${FUNCTION_DIR}
CMD [ "handler.lambda_handler" ]
