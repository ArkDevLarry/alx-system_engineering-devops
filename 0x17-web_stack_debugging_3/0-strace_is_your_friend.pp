# Fixes bad `phpp` extensions to `php` in the WordPress file `wp-settings.php`.

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/',
  notify  => Service['apache2'],  # Debian/Ubuntu (use 'httpd' for CentOS/RHEL)
}

service { 'apache2':  # Use 'httpd' if on CentOS/RHEL
  ensure => running,
  enable => true,
  require => Exec['fix-wordpress'],
}
