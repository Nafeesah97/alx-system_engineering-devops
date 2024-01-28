# Enable the user holberton to login and open files without error.

# Increase hard file limit for Holberton user.
exec { 'increase-hard-file-limit-for-holberton-user':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# Restart nginx
exec { 'restart-nginx':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d/'
}
