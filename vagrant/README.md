# ludufma-server
criação do servidor para os dados conectados da ufma

sudo apt-get install openjdk-11-jdk

sudo apt-get install openjdk-11-jre

***


sudo apt-get install default-jre

wget https://www-eu.apache.org/dist/jena/binaries/apache-jena-fuseki-3.10.0.tar.gz

tar -xzvf apache-jena-fuseki-3.10.0.tar.gz
cd apache-jena-fuseki-3.10.0

./fuseki start


/usr/local/apache-jena-fuseki-3.10.0/fuseki-server --update --mem /ds
/usr/local/apache-jena-fuseki-3.10.0/bin/s-put http://localhost:3030/ds/data default /vagrant/rdf/cursos.rdf


vagrant reload

 sudo puppet apply instfuseki.pp

 https://www.puppetcookbook.com/posts/install-package.html

 https://puppet.com/docs/puppet/5.3/lang_relationships.html

 https://forge.puppet.com/puppet/archive

 puppet module install lwf-remote_file --version 1.1.3
 
 
 erro com /dev/vboxdrv does not exist
 dpkg-reconfigure virtualbox-dkms
