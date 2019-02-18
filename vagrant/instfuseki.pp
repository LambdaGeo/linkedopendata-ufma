
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
            command => '/usr/bin/wget https://www-eu.apache.org/dist/jena/binaries/apache-jena-fuseki-3.10.0.tar.gz -O /tmp/apache-jena-fuseki.tar.gz',
            unless  => "/usr/bin/test -f /tmp/apache-jena-fuseki.tar.gz",
            require => [ Package["wget"] ],
    }

exec {"app_tar":
            command => "/bin/tar -xzvf /tmp/apache-jena-fuseki.tar.gz -C /usr/local",
            unless  => "/usr/bin/test -f /usr/local/apache-jena-fuseki",
    }
    
exec {"app_ln":
    command => "/bin/ln -s /usr/local/apache-jena-fuseki-3.10.0/fuseki /etc/init.d/fuseki",
    unless => "/usr/bin/test -f /etc/init.d/fuseki"
}

service { "fuseki":
  ensure  => running,
  start   => "/etc/init.d/fuseki start",
  stop    => "/etc/init.d/fuseki stop",
  require => Exec['app_ln']
}
