import paramiko
from scp import SCPClient

ip = '192.168.1.20' 	# Ip do Rádio
usuario = 'ubnt'		# Usuário do Rádio
senha = 'ubnt'			# Senha do Rádio
diretorio = '/home/'	# Pasta onde o arquivo de backup será salvo

try:
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(ip, username=usuario, password=senha)
	try:
			scp = SCPClient(ssh.get_transport())
			scp.get('/tmp/system.cfg', diretorio)
	except:
			print 'Falha ao fazer download do arquivo em %s' % ip
	ssh.close()
except paramiko.AuthenticationException:
	print "Falha na autenticacao em %s" % ip
except:
	print "Nao foi possivel conectar em %s" % ip
