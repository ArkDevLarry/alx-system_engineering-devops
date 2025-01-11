# Using Puppet, install flask from pip3
exec { 'install_flask_and_werkzeug':
  command => '/usr/bin/pip3 install flask==2.1.0 werkzeug==2.0.3',
  unless  => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
  path    => ['/usr/bin', '/usr/sbin', '/bin', '/sbin'],
  require => Package['python3-pip'],
}
