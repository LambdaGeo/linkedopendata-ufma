#!/bin/bash
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

set -e

if [ ! -f "$FUSEKI_BASE/shiro.ini" ] ; then
  # First time
  echo "###################################"
  echo "Initializing Apache Jena Fuseki"
  echo ""
  cp "$FUSEKI_HOME/shiro.ini" "$FUSEKI_BASE/shiro.ini"
  if [ -z "$ADMIN_PASSWORD" ] ; then
    ADMIN_PASSWORD=$(pwgen -s 15)
    echo "Randomly generated admin password:"
    echo ""
    echo "admin=$ADMIN_PASSWORD"
  fi
  echo ""
  echo "###################################"
fi

# $ADMIN_PASSWORD can always override
if [ -n "$ADMIN_PASSWORD" ] ; then
  sed -i "s/^admin=.*/admin=$ADMIN_PASSWORD/" "$FUSEKI_BASE/shiro.ini"
fi
ls
echo "$@"

exec "$@" --port=$PORT  --update --mem /ds &

# Wait until server is up


while [[ $(curl -I http://localhost:$PORT 2>/dev/null | head -n 1 | cut -d$' ' -f2) != '200' ]] ; do   
   echo  "waiting"
   sleep 1s
done



echo "importando"
ls /jena-fuseki/rdf/
/jena-fuseki/bin/s-post http://localhost:$PORT/ds/  default /jena-fuseki/rdf/subunidades.rdf
/jena-fuseki/bin/s-post http://localhost:$PORT/ds/ default  /jena-fuseki/rdf/docentes.rdf
/jena-fuseki/bin/s-post http://localhost:$PORT/ds/ default  /jena-fuseki/rdf/discentes.rdf
/jena-fuseki/bin/s-post http://localhost:$PORT/ds/ default  /jena-fuseki/rdf/cursos.rdf
/jena-fuseki/bin/s-post http://localhost:$PORT/ds/ default  /jena-fuseki/rdf/monografias.rdf
echo "importado"



while : ; do sleep 1s; done
