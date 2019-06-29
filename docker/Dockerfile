#   Licensed to the Apache Software Foundation (ASF) under one or more
#   contributor license agreements.  See the NOTICE file distributed with
#   this work for additional information regarding copyright ownership.
#   The ASF licenses this file to You under the Apache License, Version 2.0
#   (the "License"); you may not use this file except in compliance with
#   the License.  You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

FROM java:8-jre-alpine

MAINTAINER Jouni Tuominen <jouni.tuominen@aalto.fi>

RUN apk add --update pwgen bash curl wget ca-certificates findutils coreutils ruby && rm -rf /var/cache/apk/*


# Update below according to https://jena.apache.org/download/
ENV FUSEKI_SHA512 2d5c4e245d0d03bc994248dd43f718b8467d5b81204e2894abba86ec20b66939c84134580618d91d9b15bd90d90b090ab4bc691ae8778eb060d06df117dda8bb 
ENV FUSEKI_VERSION 3.10.0
ENV JENA_SHA512 7dafe7aa28cb85a6da9f6f2b109372ec0d097d4f07d8cb5882dde814b55cdb60512ab9bc09c2593118aaf3fbbc1f65f1d3b921faca7bddefd3f6bf9d7f332998
ENV JENA_VERSION 3.10.0

ENV MIRROR http://www.eu.apache.org/dist/
ENV ARCHIVE http://archive.apache.org/dist/

# Config and data
ENV FUSEKI_BASE /fuseki-base

# Fuseki installation
ENV FUSEKI_HOME /jena-fuseki

ENV PORT 3030

ENV JENA_HOME /jena
ENV JENA_BIN $JENA_HOME/bin

WORKDIR /tmp
# sha512 checksum
RUN echo "$FUSEKI_SHA512  fuseki.tar.gz" > fuseki.tar.gz.sha512
# Download/check/unpack/move Fuseki in one go (to reduce image size)
RUN wget -O fuseki.tar.gz $MIRROR/jena/binaries/apache-jena-fuseki-$FUSEKI_VERSION.tar.gz || \
    wget -O fuseki.tar.gz $ARCHIVE/jena/binaries/apache-jena-fuseki-$FUSEKI_VERSION.tar.gz && \
    sha512sum -c fuseki.tar.gz.sha512 && \
    tar zxf fuseki.tar.gz && \
    mv apache-jena-fuseki* $FUSEKI_HOME && \
    rm fuseki.tar.gz* && \
    cd $FUSEKI_HOME && rm -rf fuseki.war


# As "localhost" is often inaccessible within Docker container,
# we'll enable basic-auth with a random admin password
# (which we'll generate on start-up)
COPY shiro.ini /jena-fuseki/shiro.ini

RUN mkdir -p $FUSEKI_HOME/rdf
COPY data/rdf /jena-fuseki/rdf
RUN curl -X GET "https://dados-ufma.herokuapp.com/api/v01/docente/?subunidade=1396" -H  "accept: application/xml" > /jena-fuseki/rdf/docente.rdf
RUN curl -X GET "https://dados-ufma.herokuapp.com/api/v01/subunidade" -H  "accept: application/xml" > /jena-fuseki/rdf/subunidade.rdf


COPY docker-entrypoint.sh /
RUN chmod 755 /docker-entrypoint.sh

# SeCo extensions
COPY spatial-arq-1.0.0-SNAPSHOT-with-dependencies.jar /javalibs/


# Fuseki config
#ENV ASSEMBLER $FUSEKI_BASE/configuration/assembler.ttl
#COPY assembler.ttl $ASSEMBLER
#COPY fuseki-config.ttl $FUSEKI_BASE/config.ttl
RUN mkdir -p $FUSEKI_BASE/databases



# Set permissions to allow fuseki to run as an arbitrary user
RUN chgrp -R 0 $FUSEKI_BASE \
    && chmod -R g+rwX $FUSEKI_BASE

# Tools for loading data
ENV JAVA_CMD java -cp "$FUSEKI_HOME/fuseki-server.jar:/javalibs/*"

COPY load.sh /jena-fuseki/
RUN chmod 755 /jena-fuseki/load.sh 
#RUN /jena-fuseki/load.sh

WORKDIR /jena-fuseki
EXPOSE $PORT
USER 9008

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["/jena-fuseki/fuseki-server"]
