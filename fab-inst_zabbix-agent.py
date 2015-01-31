def install_zabbix_ag():
    run('rpm -ivh http://repo.zabbix.com/zabbix/2.4/rhel/6/x86_64/zabbix-release-2.4-1.el6.noarch.rpm')
    run('yum -y install zabbix-agent')
    run('chkconfig zabbix-agent on')
    run('mv /etc/zabbix/zabbix_agentd.conf /etc/zabbix/zabbix_agentd.conf.org1')
    put('/root/zabbix_agentd.conf','/etc/zabbix/')
    run("echo Hostname = '%s' >> /etc/zabbix/zabbix_agentd.conf" %(env.host))
    run('echo "#null" >> /etc/zabbix/zabbix_agentd.conf')
    run('service zabbix-agent restart')
