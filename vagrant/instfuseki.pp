
exec {
    'apt-update':
    command => '/usr/bin/apt-get update'
}

package {
    "default-jre":
    ensure => installed,
    require => Exec['apt-update']
}

package {
    "wget":
    ensure => installed,
    require => Exec['apt-update']
}

exec {"apps_wget":
            command => '/usr/bin/wget -P /usr/local https://www-eu.apache.org/dist/jena/binaries/apache-jena-fuseki-3.12.0.tar.gz',
            unless  => "/usr/bin/test -f /usr/local/apache-jena-fuseki-3.12.0.tar.gz",
            require => [ Package["wget"] ],
    }

exec {"fuseki_untar":
            command => "/bin/tar -xzvf /usr/local/apache-jena-fuseki-3.12.0.tar.gz -C /usr/local",
            unless  => "/usr/bin/test -f /usr/local/apache-jena-fuseki-3.12.0",
    }

file { 'cria_diretorio_rdf':
    ensure => directory,
    path   => '/usr/local/apache-jena-fuseki-3.12.0/rdf',
    require => Exec['fuseki_untar']  
  }


exec {"baixar_rdf":
            command => '/usr/bin/curl -X GET "https://dados-ufma.herokuapp.com/api/v01/docente/?subunidade=1396" -H  "accept: application/xml" > /usr/local/apache-jena-fuseki-3.12.0/rdf/docente.rdf',
            require => File['cria_diretorio_rdf'],
    }

file { 'cria_diretorio_base':
    ensure => directory,
    path   => '/usr/local/apache-jena-fuseki-3.12.0/run',
    require => Exec['fuseki_untar']  
  }


file { 'shiroini':
    ensure => file,
    path   => '/usr/local/apache-jena-fuseki-3.12.0/run/shiro.ini',
    source => "/vagrant/shiro.ini",
    require => Exec['fuseki_untar']  
}

exec {"permissao":
            command => '/bin/chown vagrant:vagrant run',
            require => File['cria_diretorio_base'],
    }

file { 'configttl':
    ensure => file,
    path   => '/usr/local/apache-jena-fuseki-3.12.0/run/config.ttl',
    source => "/vagrant/config.ttl",
    require => File['shiroini'] ,
}

service { "fuseki":
  ensure  => running,
  enable => true,
  hasrestart => true,
  start   => "/usr/local/apache-jena-fuseki-3.12.0/fuseki start",
  stop    => "/usr/local/apache-jena-fuseki-3.12.0/fuseki stop",
  restart =>  "/usr/local/apache-jena-fuseki-3.12.0fuseki restart",
  require => File['configttl'],
} ~>
exec {"import_rdf":
    command => "/usr/local/apache-jena-fuseki-3.12.0/bin/s-put http://localhost:3030/ds/data default /usr/local/apache-jena-fuseki-3.12.0/rdf/docente.rdf",
    require => Service["fuseki"]
}


#configurando

/*
exec {"app_ln":
    command => "/bin/ln -s /usr/local/apache-jena-fuseki-3.12.0/fuseki /etc/init.d/fuseki",
    unless => "/usr/bin/test -f /etc/init.d/fuseki"
}
*/

/*





exec {"fuseki_start":
    environment => [ "FUSEKI_HOME=/usr/local/apache-jena-fuseki-3.12.0/" ] ,
    command => "/usr/local/apache-jena-fuseki-3.12.0/fuseki-server --update --mem /ds &",
    #command =>  "/bin/bash -c 'cd /usr/local/apache-jena-fuseki-3.12.0/; ./fuseki-server --config=/vagrant/fuseki.ttl'"
    require => Exec['fuseki_untar']  
}




file { 'cria_diretorio_run':
    ensure => directory,
    path   => '/usr/local/apache-jena-fuseki-3.12.0/run',
    require => Exec['fuseki_untar']  
  }

exec {"criar_diretorio":
            command => "/bin/mkdir /usr/local/apache-jena-fuseki-3.12.0/rdf",
            require => [ Exec["fuseki_untar"] ],
    }

/usr/local/apache-jena-fuseki-3.12.0
#subscribe => File["/usr/local/apache-jena-fuseki-3.10.0/run/configuration/config.ttl","/usr/local/apache-jena-fuseki-3.10.0/run/shiro.ini"],

file { 'cria_diretorio_base':
    ensure => directory,
    path   => '/usr/local/apache-jena-fuseki-3.10.0/run',
    require => Exec['fuseki_untar']  
  }


file { 'cria_diretorio':
    ensure => directory,
    path   => '/usr/local/apache-jena-fuseki-3.10.0/run/configuration/',
    require => File['cria_diretorio_base']
  }

file { 'copia_configura':
    ensure => file,
    path   => '/usr/local/apache-jena-fuseki-3.10.0/run/configuration/config.ttl',
    source => "/vagrant/config.ttl",
    require => File['cria_diretorio'],
    notify => Service["fuseki"]
}

file { 'shiroini':
    ensure => file,
    path   => '/usr/local/apache-jena-fuseki-3.10.0/run/shiro.ini',
    source => "/vagrant/shiro.ini",
    require => File['cria_diretorio'],
    notify => Service["fuseki"]
}


*/

/*

#todo: fazer esse comando ser executado só apos o restart
exec {"import_rdf":
    command => "/usr/local/apache-jena-fuseki-3.10.0/bin/s-put http://localhost:3030/ds/data default /vagrant/rdf/cursos.rdf",
   # require => Exec['start_fuseki']
}


exec {"stop_fuseki":
    command => "/etc/init.d/fuseki stop",
    require => [Service["fuseki"], File[copia_configura]]
}

exec {"start_fuseki":
    command => "/etc/init.d/fuseki start",
    require => Exec["stop_fuseki"]
}


exec {"configura":
    command => "/bin/sed -i 's/\/$\/\*\* = localhostFilter/#\/$\/\*\* = localhostFilter/g' /usr/local/apache-jena-fuseki-3.10.0/run/shiro.ini",
    require => File['cria_diretorio'],
    unless => "/bin/grep  '#/\$/\*\* = localhostFilter' /usr/local/apache-jena-fuseki-3.10.0/run/shiro.ini",
    notify => Service["fuseki"]
}
*/


/*

exec {"fuseki_home":
    command => "/bin/bash -c \"export FUSEKI_HOME=/usr/local/apache-jena-fuseki-3.10.0\"",
    require => Exec['fuseki_untar'],
    notify => Service["fuseki"]
}
*/
