# Create a file in /tmp

file { 'school':
  ensure  => present,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet\n',
  path    => '/tmp/school',
}
