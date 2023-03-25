# creates a file in the /tmp directory
file { '/tmp/school':
  content => 'i love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
 }
