# Puppet manifest for setting up the web static content

# Ensure the /data directory exists
file { '/data':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

# Ensure the /data/web_static directory exists
file { '/data/web_static':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
  require => File['/data'],
}

# Ensure the /data/web_static/releases directory exists
file { '/data/web_static/releases':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
  mode   => '0755',
  require => File['/data/web_static'],
}

# Ensure the /data/web_static/shared directory exists
file { '/data/web_static/shared':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
  mode   => '0755',
  require => File['/data/web_static'],
}

# Ensure the /data/web_static/releases/test directory exists
file { '/data/web_static/releases/test':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
  mode   => '0755',
  require => File['/data/web_static/releases'],
}

# Create a simple index.html file in the test directory
file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => "<html>\n  <head>\n  </head>\n  <body>\n    ALX\n  </body>\n</html>\n",
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  require => File['/data/web_static/releases/test'],
}

# Create a symbolic link to the current release
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  force  => true,
  require => File['/data/web_static/releases/test'],
}

# Ensure the Nginx server block is configured
file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

# Ensure Nginx is running and enabled
service { 'nginx':
  ensure => 'running',
  enable => true,
}

