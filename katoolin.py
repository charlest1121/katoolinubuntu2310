#!/usr/bin/python

import os
import subprocess
import sys, traceback


if os.getuid() != 0:
    print("Sorry. This script requires sudo privledges")
    sys.exit()
def main():
    try:
        print ('''

 $$\   $$\             $$\                         $$\ $$\           
 $$ | $$  |            $$ |                        $$ |\__|          
 $$ |$$  /  $$$$$$\  $$$$$$\    $$$$$$\   $$$$$$\  $$ |$$\ $$$$$$$\  
 $$$$$  /   \____$$\ \_$$  _|  $$  __$$\ $$  __$$\ $$ |$$ |$$  __$$\ 
 $$  $$<    $$$$$$$ |  \033[1;36mKali linux tools installer\033[1;m |$$ |$$ |$$ |  $$ |
 \033[1;36m$$ |\$$\  $$  __$$ |  $$ |$$\ $$ |  $$ |$$ |  $$ |$$ |$$ |$$ |  $$ |
 $$ | \$$\ \$$$$$$$ |  \$$$$  |\$$$$$$  |\$$$$$$  |$$ |$$ |$$ |  $$ |
 \__|  \__| \_______|   \____/  \______/  \______/ \__|\__|\__|  \__| V2.0 \033[1;m


 \033[1;32m+ -- -- +=[ Original Author: LionSec, Charles Thompson | Homepage: www.neodrix.com | charles.social\033[1;m
 \033[1;32m+ -- -- +=[ 331 Tools \033[1;m


\033[1;91m[W] Before updating your system , please remove all Kali-linux repositories to avoid any kind of problem .\033[1;m
        ''')
        def inicio1():
            while True:
                print ('''
1) Add Kali repositories & Update 
2) View Categories
3) Install classicmenu indicator
4) Install Kali menu
5) Help

            ''')

                opcion0 = input("\033[1;36mkat > \033[1;m")
            
                while opcion0 == "1":
                    print ('''
1) Add kali linux repositories
2) Update
3) Remove all kali linux repositories
4) View the contents of sources.list file

                    ''')
                    repo = input("\033[1;32mWhat do you want to do ?> \033[1;m")
                    if repo == "1":
                        cmd1 = subprocess.run("gpg --keyserver keyserver.ubuntu.com --recv-keys ED444FF07D8D0BF6")
                        cmd2 = subprocess.run("echo '# Kali linux repositories | Added by Katoolin\ndeb http://http.kali.org/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list")
                    elif repo == "2":
                        cmd3 = subprocess.run("apt update -m")
                    elif repo == "3":
                        infile = "/etc/apt/sources.list"
                        outfile = "/etc/apt/sources.list"

                        delete_list = ["# Kali linux repositories | Added by Katoolin\n", "deb http://http.kali.org/kali kali-rolling main contrib non-free\n"]
                        fin = open(infile)
                        os.remove("/etc/apt/sources.list")
                        fout = open(outfile, "w+")
                        for line in fin:
                            for word in delete_list:
                                line = line.replace(word, "")
                        fout.write(line)
                        fin.close()
                        fout.close()
                        print ("\033[1;31m\nAll kali linux repositories have been deleted !\n\033[1;m")
                    elif repo == "back":
                        inicio1()
                    elif repo == "gohome":
                        inicio1()
                    elif repo == "4":
                        file = open('/etc/apt/sources.list', 'r')

                        print (file.read())

                    else:
                        print ("\033[1;31mSorry, that was an invalid command!\033[1;m")                     
                        

                if opcion0 == "3":
                    print (''' 
ClassicMenu Indicator is a notification area applet (application indicator) for the top panel of Ubuntu's Unity desktop environment.

It provides a simple way to get a classic GNOME-style application menu for those who prefer this over the Unity dash menu.

Like the classic GNOME menu, it includes Wine games and applications if you have those installed.

For more information , please visit : http://www.florian-diesch.de/software/classicmenu-indicator/

''')
                    repo = input("\033[1;32mDo you want to install classicmenu indicator ? [y/n]> \033[1;m")
                    if repo == "y":
                        cmd1 = subprocess.run("add-apt-repository ppa:diesch/testing && apt update")
                        cmd = subprocess.run("sudo apt install classicmenu-indicator")

                elif opcion0 == "4"    :
                    repo = input("\033[1;32mDo you want to install Kali menu ? [y/n]> \033[1;m")
                    if repo == "y":
                        cmd1 = subprocess.run("apt install kali-menu")
                elif opcion0 == "5":
                    print (''' 
****************** +Commands+ ******************


\033[1;32mback\033[1;m     \033[1;33mGo back\033[1;m

\033[1;32mgohome\033[1;m    \033[1;33mGo to the main menu\033[1;m

        ''')


                def inicio():
                    while opcion0 == "2":
                        print ('''
\033[1;36m**************************** All Categories *****************************\033[1;m

1) Information Gathering            8) Exploitation Tools
2) Vulnerability Analysis            9) Forensics Tools
3) Wireless Attacks                10) Stress Testing
4) Web Applications                11) Password Attacks
5) Sniffing & Spoofing                12) Reverse Engineering
6) Maintaining Access                13) Hardware Hacking
7) Reporting Tools                 14) Extra
                                    
0) All

             ''')
                        print ("\033[1;32mSelect a category or press (0) to install all Kali linux tools .\n\033[1;m")

                        opcion1 = input("\033[1;36mkat > \033[1;m")
                        if opcion1 == "back":
                            inicio1()
                        elif opcion1 == "gohome":
                            inicio1()
                        elif opcion1 == "0":
                            cmd = subprocess.run("apt -f install acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega w3af webscarab websploit wfuzz wpscan xsser zaproxy burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy apktool dex2jar python-distorm3 edb-debugger jad javasnoop jd ollydbg smali valgrind yara android-sdk apktool arduino dex2jar sakis3g smali && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")    
                        while opcion1 == "1":
                            print ('''
\033[1;36m=+[ Information Gathering\033[1;m

 1) acccheck                    30) lbd
 2) ace-voip                    31) Maltego Teeth
 3) Amap                    32) masscan
 4) Automater                    33) Metagoofil
 5) bing-ip2hosts                34) Miranda
 6) braa                    35) Nmap
 7) CaseFile                    36) ntop
 8) CDPSnarf                    37) p0f
 9) cisco-torch                    38) Parsero
10) Cookie Cadger                39) Recon-ng
11) copy-router-config                40) SET
12) DMitry                    41) smtp-user-enum
13) dnmap                    42) snmpcheck
14) dnsenum                    43) sslcaudit
15) dnsmap                    44) SSLsplit
16) DNSRecon                    45) sslstrip
17) dnstracer                    46) SSLyze
18) dnswalk                    47) THC-IPV6
19) DotDotPwn                    48) theHarvester
20) enum4linux                    49) TLSSLed
21) enumIAX                    50) twofi
22) exploitdb                    51) URLCrazy
23) Fierce                    52) Wireshark
24) Firewalk                    53) WOL-E
25) fragroute                    54) Xplico
26) fragrouter                    55) iSMTP
27) Ghost Phisher                56) InTrace
28) GoLismero                    57) hping3
29) goofile

0) Install all Information Gathering tools
                 
                        ''')
                            print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
                            opcion2 = input("\033[1;36mkat > \033[1;m")
                            if opcion2 == "1":
                                cmd = subprocess.run("apt install acccheck")

                            elif opcion2 == "2":
                                cmd = subprocess.run("apt install ace-voip")

                            elif opcion2 == "3":
                                cmd = subprocess.run("apt install amap")
                            elif opcion2 == "4":
                                cmd = subprocess.run("apt install automater")
                            elif opcion2 == "5":
                                cmd = subprocess.run("wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")
                            elif opcion2 == "6":
                                cmd = subprocess.run("apt install braa")
                            elif opcion2 == "7":
                                cmd = subprocess.run("apt install casefile")
                            elif opcion2 == "8":
                                cmd = subprocess.run("apt install cdpsnarf")
                            elif opcion2 == "9":
                                cmd = subprocess.run("apt install cisco-torch")
                            elif opcion2 == "10":
                                cmd = subprocess.run("apt install cookie-cadger")
                            elif opcion2 == "11":
                                cmd = subprocess.run("apt install copy-router-config")
                            elif opcion2 == "12":
                                cmd = subprocess.run("apt install dmitry")
                            elif opcion2 == "13":
                                cmd = subprocess.run("apt install dnmap")
                            elif opcion2 == "14":
                                cmd = subprocess.run("apt install dnsenum")
                            elif opcion2 == "15":
                                cmd = subprocess.run("apt install dnsmap")
                            elif opcion2 == "16":
                                cmd = subprocess.run("apt install dnsrecon")
                            elif opcion2 == "17":
                                cmd = subprocess.run("apt install dnstracer")
                            elif opcion2 == "18":
                                cmd = subprocess.run("apt install dnswalk")
                            elif opcion2 == "19":
                                cmd = subprocess.run("apt install dotdotpwn")
                            elif opcion2 == "20":
                                cmd = subprocess.run("apt install enum4linux")
                            elif opcion2 == "21":
                                cmd = subprocess.run("apt install enumiax")
                            elif opcion2 == "22":
                                cmd = subprocess.run("apt install exploitdb")
                            elif opcion2 == "23":
                                cmd = subprocess.run("apt install fierce")
                            elif opcion2 == "24":
                                cmd = subprocess.run("apt install firewalk")
                            elif opcion2 == "25":
                                cmd = subprocess.run("apt install fragroute")
                            elif opcion2 == "26":
                                cmd = subprocess.run("apt install fragrouter")
                            elif opcion2 == "27":
                                cmd = subprocess.run("apt install ghost-phisher")
                            elif opcion2 == "28":
                                cmd = subprocess.run("apt install golismero")
                            elif opcion2 == "29":
                                cmd = subprocess.run("apt install goofile")
                            elif opcion2 == "30":
                                cmd = subprocess.run("apt install lbd")
                            elif opcion2 == "31":
                                cmd = subprocess.run("apt install maltego-teeth")
                            elif opcion2 == "32":
                                cmd = subprocess.run("apt install masscan")
                            elif opcion2 == "33":
                                cmd = subprocess.run("apt install metagoofil")
                            elif opcion2 == "34":
                                cmd = subprocess.run("apt install miranda")
                            elif opcion2 == "35":
                                cmd = subprocess.run("apt install nmap")
                            elif opcion2 == "36":
                                print ('ntop is unavailable')
                            elif opcion2 == "37":
                                cmd = subprocess.run("apt install p0f")
                            elif opcion2 == "38":
                                cmd = subprocess.run("apt install parsero")
                            elif opcion2 == "39":
                                cmd = subprocess.run("apt install recon-ng")
                            elif opcion2 == "40":
                                cmd = subprocess.run("apt install set")
                            elif opcion2 == "41":
                                cmd = subprocess.run("apt install smtp-user-enum")
                            elif opcion2 == "42":
                                cmd = subprocess.run("apt install snmpcheck")
                            elif opcion2 == "43":
                                cmd = subprocess.run("apt install sslcaudit")
                            elif opcion2 == "44":
                                cmd = subprocess.run("apt install sslsplit")
                            elif opcion2 == "45":
                                cmd = subprocess.run("apt install sslstrip")
                            elif opcion2 == "46":
                                cmd = subprocess.run("apt install sslyze")
                            elif opcion2 == "47":
                                cmd = subprocess.run("apt install thc-ipv6")
                            elif opcion2 == "48":
                                cmd = subprocess.run("apt install theharvester")
                            elif opcion2 == "49":
                                cmd = subprocess.run("apt install tlssled")
                            elif opcion2 == "50":
                                cmd = subprocess.run("apt install twofi")
                            elif opcion2 == "51":
                                cmd = subprocess.run("apt install urlcrazy")
                            elif opcion2 == "52":
                                cmd = subprocess.run("apt install wireshark")
                            elif opcion2 == "53":
                                cmd = subprocess.run("apt install wol-e")
                            elif opcion2 == "54":
                                cmd = subprocess.run("apt install xplico")
                            elif opcion2 == "55":
                                cmd = subprocess.run("apt install ismtp")
                            elif opcion2 == "56":
                                cmd = subprocess.run("apt install intrace")
                            elif opcion2 == "57":
                                cmd = subprocess.run("apt install hping3")
                            elif opcion2 == "back":
                                inicio()
                            elif opcion2 == "gohome":
                                inicio1()        
                            elif opcion2 == "0":
                                cmd = subprocess.run("apt install -y acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")                
                            else:
                                print ("\033[1;31mSorry, that was an invalid command!\033[1;m")



                        while opcion1 == "2":
                            print ('''
\033[1;36m=+[ Vulnerability Analysis\033[1;m

 1) BBQSQL                18) Nmap
 2) BED                    19)ohrwurm
 3) cisco-auditing-tool            20) openvas-administrator
 4) cisco-global-exploiter        21) openvas-cli
 5) cisco-ocs                22) openvas-manager
 6) cisco-torch                23) openvas-scanner
 7) copy-router-config            24) Oscanner
 8) commix                25) Powerfuzzer
 9) DBPwAudit                26) sfuzz
10) DoonaDot                27) SidGuesser
11) DotPwn                28) SIPArmyKnife
12) Greenbone Security Assistant     29) sqlmap
13) GSD                    30) Sqlninja
14) HexorBase                31) sqlsus
15) Inguma                32) THC-IPV6
16) jSQL                33) tnscmd10g
17) Lynis                34) unix-privesc-check
                    35) Yersinia

0) Install all Vulnerability Analysis tools
                 
                        ''')
                            print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
                            opcion2 = input("\033[1;36mkat > \033[1;m")
                            if opcion2 == "1":
                                cmd = subprocess.run("apt install bbqsql")

                            elif opcion2 == "2":
                                cmd = subprocess.run("apt install bed")

                            elif opcion2 == "3":
                                cmd = subprocess.run("apt install cisco-auditing-tool")
                            elif opcion2 == "4":
                                cmd = subprocess.run("apt install cisco-global-exploiter")
                            elif opcion2 == "5":
                                cmd = subprocess.run("apt install cisco-ocs")
                            elif opcion2 == "6":
                                cmd = subprocess.run("apt install cisco-torch")
                            elif opcion2 == "7":
                                cmd = subprocess.run("apt install copy-router-config")
                            elif opcion2 == "8":
                                cmd = subprocess.run("apt install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install")
                            elif opcion2 == "9":
                                cmd = subprocess.run("echo 'download page : http://www.cqure.net/wp/tools/database/dbpwaudit/'")
                            elif opcion2 == "10":
                                cmd = subprocess.run("apt install doona")
                            elif opcion2 == "11":
                                cmd = subprocess.run("apt install dotdotpwn")
                            elif opcion2 == "12":
                                cmd = subprocess.run("apt install greenbone-security-assistant")
                            elif opcion2 == "13":
                                cmd = subprocess.run("apt install git && git clone git://git.kali.org/packages/gsd.git")
                            elif opcion2 == "14":
                                cmd = subprocess.run("apt install hexorbase")
                            elif opcion2 == "15":
                                print ("Please download inguma from : http://inguma.sourceforge.net")
                            elif opcion2 == "16":
                                cmd = subprocess.run("apt install jsql")
                            elif opcion2 == "17":
                                cmd = subprocess.run("apt install lynis")
                            elif opcion2 == "18":
                                cmd = subprocess.run("apt install nmap")
                            elif opcion2 == "19":
                                cmd = subprocess.run("apt install ohrwurm")
                            elif opcion2 == "20":
                                cmd = subprocess.run("apt install openvas-administrator")
                            elif opcion2 == "21":
                                cmd = subprocess.run("apt install openvas-cli")
                            elif opcion2 == "22":
                                cmd = subprocess.run("apt install openvas-manager")
                            elif opcion2 == "23":
                                cmd = subprocess.run("apt install openvas-scanner")
                            elif opcion2 == "24":
                                cmd = subprocess.run("apt install oscanner")
                            elif opcion2 == "25":
                                cmd = subprocess.run("apt install powerfuzzer")
                            elif opcion2 == "26":
                                cmd = subprocess.run("apt install sfuzz")
                            elif opcion2 == "27":
                                cmd = subprocess.run("apt install sidguesser")
                            elif opcion2 == "28":
                                cmd = subprocess.run("apt install siparmyknife")
                            elif opcion2 == "29":
                                cmd = subprocess.run("apt install sqlmap")
                            elif opcion2 == "30":
                                cmd = subprocess.run("apt install sqlninja")
                            elif opcion2 == "31":
                                cmd = subprocess.run("apt install sqlsus")
                            elif opcion2 == "32":
                                cmd = subprocess.run("apt install thc-ipv6")
                            elif opcion2 == "33":
                                cmd = subprocess.run("apt install tnscmd10g")
                            elif opcion2 == "34":
                                cmd = subprocess.run("apt install unix-privesc-check")
                            elif opcion2 == "35":
                                cmd = subprocess.run("apt install yersinia")
                            elif opcion2 == "back":
                                inicio()
                            elif opcion2 == "gohome":
                                inicio1()                        
                            elif opcion2 == "0":
                                cmd = subprocess.run("apt install -y bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia")                        
                            else:
                                print ("\033[1;31mSorry, that was an invalid command!\033[1;m")

                        while opcion1 == "3":
                            print ('''
        \033[1;36m=+[ Wireless Attacks\033[1;m

 1) Aircrack-ng                17) kalibrate-rtl
 2) Asleap                18) KillerBee
 3) Bluelog                19) Kismet
 4) BlueMaho                20) mdk3
 5) Bluepot                21) mfcuk
 6) BlueRanger                22) mfoc
 7) Bluesnarfer                23) mfterm
 8) Bully                24) Multimon-NG
 9) coWPAtty                25) PixieWPS
10) crackle                26) Reaver
11) eapmd5pass                27) redfang
12) Fern Wifi Cracker            28) RTLSDR Scanner
13) Ghost Phisher            29) Spooftooph
14) GISKismet                30) Wifi Honey                31) Wifitap
16) gr-scan                32) Wifite 

0) Install all Wireless Attacks tools
                 
                        ''')
                            print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
                            opcion2 = input("\033[1;36mkat > \033[1;m")
                            if opcion2 == "1":
                                cmd = subprocess.run("apt install aircrack-ng")

                            elif opcion2 == "2":
                                cmd = subprocess.run("apt install asleap")

                            elif opcion2 == "3":
                                cmd = subprocess.run("apt install bluelog")
                            elif opcion2 == "4":
                                cmd = subprocess.run("apt install git && git clone git://git.kali.org/packages/bluemaho.git")
                            elif opcion2 == "5":
                                cmd = subprocess.run("apt install git && git clone git://git.kali.org/packages/bluepot.git")
                            elif opcion2 == "6":
                                cmd = subprocess.run("apt install blueranger")
                            elif opcion2 == "7":
                                cmd = subprocess.run("apt install bluesnarfer")
                            elif opcion2 == "8":
                                cmd = subprocess.run("apt install bully")
                            elif opcion2 == "9":
                                cmd = subprocess.run("apt install cowpatty")
                            elif opcion2 == "10":
                                cmd = subprocess.run("apt install crackle")
                            elif opcion2 == "11":
                                cmd = subprocess.run("apt install eapmd5pass")
                            elif opcion2 == "12":
                                cmd = subprocess.run("apt install fern-wifi-cracker")
                            elif opcion2 == "13":
                                cmd = subprocess.run("apt install ghost-phisher")
                            elif opcion2 == "14":
                                cmd = subprocess.run("apt install giskismet")
                            elif opcion2 == "16":
                                cmd = subprocess.run("apt install git && git clone git://git.kali.org/packages/gr-scan.git")
                            elif opcion2 == "17":
                                cmd = subprocess.run("apt install kalibrate-rtl")
                            elif opcion2 == "18":
                                cmd = subprocess.run("apt install killerbee")
                            elif opcion2 == "19":
                                cmd = subprocess.run("apt install kismet")
                            elif opcion2 == "20":
                                cmd = subprocess.run("apt install mdk3")
                            elif opcion2 == "21":
                                cmd = subprocess.run("apt install mfcuk")
                            elif opcion2 == "22":
                                cmd = subprocess.run("apt install mfoc")
                            elif opcion2 == "23":
                                cmd = subprocess.run("apt install mfterm")
                            elif opcion2 == "24":
                                cmd = subprocess.run("apt install multimon-ng")
                            elif opcion2 == "25":
                                cmd = subprocess.run("apt install pixiewps")
                            elif opcion2 == "26":
                                cmd = subprocess.run("apt install reaver")
                            elif opcion2 == "27":
                                cmd = subprocess.run("apt install redfang")
                            elif opcion2 == "28":
                                cmd = subprocess.run("apt install rtlsdr-scanner")
                            elif opcion2 == "29":
                                cmd = subprocess.run("apt install spooftooph")
                            elif opcion2 == "30":
                                cmd = subprocess.run("apt install wifi-honey")
                            elif opcion2 == "31":
                                cmd = subprocess.run("apt install wifitap")
                            elif opcion2 == "32":
                                cmd = subprocess.run("apt install wifite")
                            elif opcion2 == "0":
                                cmd = subprocess.run("apt install -y aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite")
                            elif opcion2 == "back":
                                inicio()
                            elif opcion2 == "gohome":
                                inicio1()                        
                            else:
                                print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
                        while opcion1 == "4":
                            print ('''
\033[1;36m=+[ Web Applications\033[1;m

 1) apache-users            21) Parsero
 2) Arachni                22) plecost
 3) BBQSQL                23) Powerfuzzer
 4) BlindElephant            24) ProxyStrike
 5) Burp Suite                25) Recon-ng
 6) commix                26) Skipfish
 7) CutyCapt                27) sqlmap
 8) DAVTest                28) Sqlninja
 9) deblaze                29) sqlsus
10) DIRB                30) ua-tester
11) DirBuster                31) Uniscan
12) fimap                32) Vega
13) FunkLoad                33) w3af
14) Grabber                34) WebScarab
15) jboss-autopwn            35) Webshag
16) joomscan                36) WebSlayer
17) jSQL                37) WebSploit
18) Maltego Teeth            38) Wfuzz
19) PadBuster                39) WPScan
20) Paros                40) XSSer
                    41) zaproxy

0) Install all Web Applications tools
                 
                        ''')
                            print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")

                            
                            opcion2 = input("\033[1;36mkat > \033[1;m")
                            if opcion2 == "1":
                                cmd = subprocess.run("apt install apache-users")

                            elif opcion2 == "2":
                                cmd = subprocess.run("apt install arachni")

                            elif opcion2 == "3":
                                cmd = subprocess.run("apt install bbqsql")
                            elif opcion2 == "4":
                                cmd = subprocess.run("apt install blindelephant")
                            elif opcion2 == "5":
                                cmd = subprocess.run("apt install burpsuite")
                            elif opcion2 == "6":
                                cmd = subprocess.run("apt install cutycapt")
                            elif opcion2 == "7":
                                cmd = subprocess.run("apt install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install")
                            elif opcion2 == "8":
                                cmd = subprocess.run("apt install davtest")
                            elif opcion2 == "9":
                                cmd = subprocess.run("apt install deblaze")
                            elif opcion2 == "10":
                                cmd = subprocess.run("apt install dirb")
                            elif opcion2 == "11":
                                cmd = subprocess.run("apt install dirbuster")
                            elif opcion2 == "12":
                                cmd = subprocess.run("apt install fimap")
                            elif opcion2 == "13":
                                cmd = subprocess.run("apt install funkload")
                            elif opcion2 == "14":
                                cmd = subprocess.run("apt install grabber")
                            elif opcion2 == "15":
                                cmd = subprocess.run("apt install jboss-autopwn")
                            elif opcion2 == "16":
                                cmd = subprocess.run("apt install joomscan")
                            elif opcion2 == "17":
                                cmd = subprocess.run("apt install jsql")
                            elif opcion2 == "18":
                                cmd = subprocess.run("apt install maltego-teeth")
                            elif opcion2 == "19":
                                cmd = subprocess.run("apt install padbuster")
                            elif opcion2 == "20":
                                cmd = subprocess.run("apt install paros")
                            elif opcion2 == "21":
                                cmd = subprocess.run("apt install parsero")
                            elif opcion2 == "22":
                                cmd = subprocess.run("apt install plecost")
                            elif opcion2 == "23":
                                cmd = subprocess.run("apt install powerfuzzer")
                            elif opcion2 == "24":
                                cmd = subprocess.run("apt install proxystrike")
                            elif opcion2 == "25":
                                cmd = subprocess.run("apt install recon-ng")
                            elif opcion2 == "26":
                                cmd = subprocess.run("apt install skipfish")
                            elif opcion2 == "27":
                                cmd = subprocess.run("apt install sqlmap")
                            elif opcion2 == "28":
                                cmd = subprocess.run("apt install sqlninja")
                            elif opcion2 == "29":
                                cmd = subprocess.run("apt install sqlsus")
                            elif opcion2 == "30":
                                cmd = subprocess.run("apt install ua-tester")
                            elif opcion2 == "31":
                                cmd = subprocess.run("apt install uniscan")
                            elif opcion2 == "32":
                                cmd = subprocess.run("apt install vega")
                            elif opcion2 == "33":
                                cmd = subprocess.run("apt install w3af")
                            elif opcion2 == "34":
                                cmd = subprocess.run("apt install webscarab")
                            elif opcion2 == "35":
                                print ("Webshag is unavailable")
                            elif opcion2 == "36":
                                cmd = subprocess.run("apt install git && git clone git://git.kali.org/packages/webslayer.git")
                            elif opcion2 == "37":
                                cmd = subprocess.run("apt install websploit")
                            elif opcion2 == "38":
                                cmd = subprocess.run("apt install wfuzz")
                            elif opcion2 == "39":
                                cmd = subprocess.run("apt install wpscan")
                            elif opcion2 == "40":
                                cmd = subprocess.run("apt install xsser")
                            elif opcion2 == "41":
                                cmd = subprocess.run("apt install zaproxy")                                        
                            elif opcion2 == "back":
                                inicio()
                            elif opcion2 == "gohome":
                                inicio1()    
                            elif opcion2 == "0":
                                cmd = subprocess.run("apt install -y apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega w3af webscarab websploit wfuzz wpscan xsser zaproxy")                                                
                            else:
                                print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
                        while opcion1 == "5":
                            print ('''
\033[1;36m=+[ Sniffing & Spoofing\033[1;m

 1) Burp Suite                17) rtpmixsound
 2) DNSChef                18) sctpscan
 3) fiked                19) SIPArmyKnife
 4) hamster-sidejack            20) SIPp
 5) HexInject                21) SIPVicious
 6) iaxflood                22) SniffJoke
 7) inviteflood                23) SSLsplit
 8) iSMTP                24) sslstrip
 9) isr-evilgrade            25) THC-IPV6
10) mitmproxy                26) VoIPHopper
11) ohrwurm                27) WebScarab
12) protos-sip                28) Wifi Honey
13) rebind                29) Wireshark
14) responder                30) xspy
15) rtpbreak                31) Yersinia
16) rtpinsertsound            32) zaproxy 

0) Install all Sniffing & Spoofing tools
                 
                        ''')
                            print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
                            opcion2 = input("\033[1;36mkat > \033[1;m")
                            if opcion2 == "1":
                                cmd = subprocess.run("apt install burpsuite")

                            elif opcion2 == "2":
                                cmd = subprocess.run("apt install dnschef")

                            elif opcion2 == "3":
                                cmd = subprocess.run("apt install fiked")
                            elif opcion2 == "4":
                                cmd = subprocess.run("apt install hamster-sidejack")
                            elif opcion2 == "5":
                                cmd = subprocess.run("apt install hexinject")
                            elif opcion2 == "6":
                                cmd = subprocess.run("apt install iaxflood")
                            elif opcion2 == "7":
                                cmd = subprocess.run("apt install inviteflood")
                            elif opcion2 == "8":
                                cmd = subprocess.run("apt install ismtp")
                            elif opcion2 == "9":
                                cmd = subprocess.run("apt install git && git clone git://git.kali.org/packages/isr-evilgrade.git")
                            elif opcion2 == "10":
                                cmd = subprocess.run("apt install mitmproxy")
                            elif opcion2 == "11":
                                cmd = subprocess.run("apt install ohrwurm")
                            elif opcion2 == "12":
                                cmd = subprocess.run("apt install protos-sip")
                            elif opcion2 == "13":
                                cmd = subprocess.run("apt install rebind")
                            elif opcion2 == "14":
                                cmd = subprocess.run("apt install responder")
                            elif opcion2 == "15":
                                cmd = subprocess.run("apt install rtpbreak")
                            elif opcion2 == "16":
                                cmd = subprocess.run("apt install rtpinsertsound")
                            elif opcion2 == "17":
                                cmd = subprocess.run("apt install rtpmixsound")
                            elif opcion2 == "18":
                                cmd = subprocess.run("apt install sctpscan")
                            elif opcion2 == "19":
                                cmd = subprocess.run("apt install siparmyknife")
                            elif opcion2 == "20":
                                cmd = subprocess.run("apt install sipp")
                            elif opcion2 == "21":
                                cmd = subprocess.run("apt install sipvicious")
                            elif opcion2 == "22":
                                cmd = subprocess.run("apt install sniffjoke")
                            elif opcion2 == "23":
                                cmd = subprocess.run("apt install sslsplit")
                            elif opcion2 == "24":
                                cmd = subprocess.run("apt install sslstrip")
                            elif opcion2 == "25":
                                cmd = subprocess.run("apt install thc-ipv6")
                            elif opcion2 == "26":
                                cmd = subprocess.run("apt install voiphopper")
                            elif opcion2 == "27":
                                cmd = subprocess.run("apt install webscarab")
                            elif opcion2 == "28":
                                cmd = subprocess.run("apt install wifi-honey")
                            elif opcion2 == "29":
                                cmd = subprocess.run("apt install wireshark")
                            elif opcion2 == "30":
                                cmd = subprocess.run("apt install xspy")
                            elif opcion2 == "31":
                                cmd = subprocess.run("apt install yersinia")
                            elif opcion2 == "32":
                                cmd = subprocess.run("apt install zaproxy")
                            elif opcion2 == "back":
                                inicio()
                            elif opcion2 == "gohome":
                                inicio1()


                            elif opcion2 == "0":
                                cmd = subprocess.run("apt install -y burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy")  
                            else:
                                print ("\033[1;31mSorry, that was an invalid command!\033[1;m")

                        while opcion1 == "6":
                            print ('''
\033[1;36m=+[ Maintaining Access\033[1;m

 1) CryptCat
 2) Cymothoa
 3) dbd
 4) dns2tcp
 5) http-tunnel    
 6) HTTPTunnel
 7) Intersect
 8) Nishang
 9) polenum
10) PowerSploit
11) pwnat
12) RidEnum
13) sbd
14) U3-Pwn
15) Webshells
16) Weevely

0) Install all Maintaining Access tools
                 
                        ''')
                            print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
                            opcion2 = input("\033[1;36mkat > \033[1;m")
                            if opcion2 == "1":
                                cmd = subprocess.run("apt install cryptcat")

                            elif opcion2 == "2":
                                cmd = subprocess.run("apt install cymothoa")

                            elif opcion2 == "3":
                                cmd = subprocess.run("apt install dbd")
                            elif opcion2 == "4":
                                cmd = subprocess.run("apt install dns2tcp")
                            elif opcion2 == "5":
                                cmd = subprocess.run("apt install http-tunnel")
                            elif opcion2 == "6":
                                cmd = subprocess.run("apt install httptunnel")
                            elif opcion2 == "7":
                                cmd = subprocess.run("apt install intersect")
                            elif opcion2 == "8":
                                cmd = subprocess.run("apt install nishang")
                            elif opcion2 == "9":
                                cmd = subprocess.run("apt install polenum")
                            elif opcion2 == "10":
                                cmd = subprocess.run("apt install powersploit")
                            elif opcion2 == "11":
                                cmd = subprocess.run("apt install pwnat")
                            elif opcion2 == "12":
                                cmd = subprocess.run("apt install ridenum")
                            elif opcion2 == "13":
                                cmd = subprocess.run("apt install sbd")
                            elif opcion2 == "14":
                                cmd = subprocess.run("apt install u3-pwn")
                            elif opcion2 == "15":
                                cmd = subprocess.run("apt install webshells")
                            elif opcion2 == "16":
                                cmd = subprocess.run("apt install weevely")
                            elif opcion2 == "back":
                                inicio()
                            elif opcion2 == "gohome":
                                inicio1()   
                            elif opcion2 == "0":
                                cmd = subprocess.run("apt install -y cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely")
                            else:
                                print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
                        while opcion1 == "7":
                            print ('''
\033[1;36m=+[ Reporting Tools\033[1;m

1) CaseFile
2) CutyCapt
3) dos2unix
4) Dradis
5) KeepNote    
6) MagicTree
7) Metagoofil
8) Nipper-ng
9) pipal

0) Install all Reporting Tools
                 
                        ''')
                            print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
                            opcion2 = input("\033[1;36mkat > \033[1;m")
                            if opcion2 == "1":
                                cmd = subprocess.run("apt install casefile")

                            elif opcion2 == "2":
                                cmd = subprocess.run("apt install cutycapt")

                            elif opcion2 == "3":
                                cmd = subprocess.run("apt install dos2unix")
                            elif opcion2 == "4":
                                cmd = subprocess.run("apt install dradis")
                            elif opcion2 == "5":
                                cmd = subprocess.run("apt install keepnote")
                            elif opcion2 == "6":
                                cmd = subprocess.run("apt install magictree")
                            elif opcion2 == "7":
                                cmd = subprocess.run("apt install metagoofil")
                            elif opcion2 == "8":
                                cmd = subprocess.run("apt install nipper-ng")
                            elif opcion2 == "9":
                                cmd = subprocess.run("apt install pipal")
                            elif opcion2 == "back":
                                inicio()
                            elif opcion2 == "gohome":
                                inicio1()   
                            elif opcion2 == "0":
                                cmd = subprocess.run("apt install -y casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal")  
                            else:
                                print ("\033[1;31mSorry, that was an invalid command!\033[1;m")

                        while opcion1 == "8":
                            print ('''
\033[1;36m=+[ Exploitation Tools\033[1;m

 1) Armitage
 2) Backdoor Factory
 3) BeEF
 4) cisco-auditing-tool
 5) cisco-global-exploiter    
 6) cisco-ocs
 7) cisco-torch
 8) commix
 9) crackle
10) jboss-autopwn
11) Linux Exploit Suggester
12) Maltego Teeth
13) SET
14) ShellNoob
15) sqlmap
16) THC-IPV6
17) Yersinia

0) Install all Exploitation Tools
                 
                        ''')
                            print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
                            opcion2 = input("\033[1;36mkat > \033[1;m")
                            if opcion2 == "1":
                                cmd = subprocess.run("apt install armitage")

                            elif opcion2 == "2":
                                cmd = subprocess.run("apt install backdoor-factory")

                            elif opcion2 == "3":
                                cmd = subprocess.run("apt install beef-xss")
                            elif opcion2 == "4":
                                cmd = subprocess.run("apt install cisco-auditing-tool")
                            elif opcion2 == "5":
                                cmd = subprocess.run("apt install cisco-global-exploiter")
                            elif opcion2 == "6":
                                cmd = subprocess.run("apt install cisco-ocs")
                            elif opcion2 == "7":
                                cmd = subprocess.run("apt install cisco-torch")
                            elif opcion2 == "8":
                                cmd = subprocess.run("apt install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install")
                            elif opcion2 == "9":
                                cmd = subprocess.run("apt install crackle")
                            elif opcion2 == "10":
                                cmd = subprocess.run("apt install jboss-autopwn")
                            elif opcion2 == "11":
                                cmd = subprocess.run("apt install linux-exploit-suggester")
                            elif opcion2 == "12":
                                cmd = subprocess.run("apt install maltego-teeth")
                            elif opcion2 == "13":
                                cmd = subprocess.run("apt install set")
                            elif opcion2 == "14":
                                cmd = subprocess.run("apt install shellnoob")
                            elif opcion2 == "15":
                                cmd = subprocess.run("apt install sqlmap")
                            elif opcion2 == "16":
                                cmd = subprocess.run("apt install thc-ipv6")
                            elif opcion2 == "17":
                                cmd = subprocess.run("apt install yersinia")
                            elif opcion2 == "back":
                                inicio()
                            elif opcion2 == "gohome":
                                inicio1()   
                            elif opcion2 == "0":
                                cmd = subprocess.run("apt install -y armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss")                          
                            else:
                                print ("\033[1;31mSorry, that was an invalid command!\033[1;m")

                        while opcion1 == "9":
                            print ('''
\033[1;36m=+[ Forensics Tools\033[1;m

 1) Binwalk                11) extundelete
 2) bulk-extractor            12) Foremost
 3) Capstone                13) Galleta
 4) chntpw                14) Guymager
 5) Cuckoo                15) iPhone Backup Analyzer
 6) dc3dd                16) p0f
 7) ddrescue                17) pdf-parser
 8) DFF                    18) pdfid
 9) diStorm3                19) pdgmail
10) Dumpzilla                20) peepdf
                    21) RegRipper
                    22) Volatility
                    23) Xplico

0) Install all Forensics Tools
                 
                        ''')
                            print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
                            opcion2 = input("\033[1;36mkat > \033[1;m")
                            if opcion2 == "1":
                                cmd = subprocess.run("apt install binwalk")

                            elif opcion2 == "2":
                                cmd = subprocess.run("apt install bulk-extractor")

                            elif opcion2 == "3":
                                cmd = subprocess.run("apt install git && git clone git://git.kali.org/packages/capstone.git")
                            elif opcion2 == "4":
                                cmd = subprocess.run("apt install chntpw")
                            elif opcion2 == "5":
                                cmd = subprocess.run("apt install cuckoo")
                            elif opcion2 == "6":
                                cmd = subprocess.run("apt install dc3dd")
                            elif opcion2 == "7":
                                cmd = subprocess.run("apt install ddrescue")
                            elif opcion2 == "8":
                                print ('dff is unavailable')
                            elif opcion2 == "9":
                                cmd = subprocess.run("apt install git && git clone git://git.kali.org/packages/distorm3.git")
                            elif opcion2 == "10":
                                cmd = subprocess.run("apt install dumpzilla")
                            elif opcion2 == "11":
                                cmd = subprocess.run("apt install extundelete")
                            elif opcion2 == "12":
                                cmd = subprocess.run("apt install foremost")
                            elif opcion2 == "13":
                                cmd = subprocess.run("apt install galleta")
                            elif opcion2 == "14":
                                cmd = subprocess.run("apt install guymager")
                            elif opcion2 == "15":
                                cmd = subprocess.run("apt install iphone-backup-analyzer")
                            elif opcion2 == "16":
                                cmd = subprocess.run("apt install p0f")
                            elif opcion2 == "17":
                                cmd = subprocess.run("apt install pdf-parser")
                            elif opcion2 == "18":
                                cmd = subprocess.run("apt install pdfid")
                            elif opcion2 == "19":
                                cmd = subprocess.run("apt install pdgmail")
                            elif opcion2 == "20":
                                cmd = subprocess.run("apt install peepdf")
                            elif opcion2 == "21":
                                print ("Regripper is unavailable")
                            elif opcion2 == "22":
                                cmd = subprocess.run("apt install volatility")
                            elif opcion2 == "23":
                                cmd = subprocess.run("apt install xplico")
                            elif opcion2 == "back":
                                inicio()
                            elif opcion2 == "gohome":
                                inicio1()   
                            elif opcion2 == "0":
                                cmd = subprocess.run("apt install -y binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico")                        
                            else:
                                print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
                        while opcion1 == "10":
                            print ('''
\033[1;36m=+[ Stress Testing\033[1;m

 1) DHCPig
 2) FunkLoad
 3) iaxflood
 4) Inundator
 5) inviteflood    
 6) ipv6-toolkit
 7) mdk3
 8) Reaver
 9) rtpflood
10) SlowHTTPTest
11) t50
12) Termineter
13) THC-IPV6
14) THC-SSL-DOS         

0) Install all Stress Testing tools
                 
                        ''')
                            print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
                            opcion2 = input("\033[1;36mkat > \033[1;m")
                            if opcion2 == "1":
                                cmd = subprocess.run("apt install dhcpig")

                            elif opcion2 == "2":
                                cmd = subprocess.run("apt install funkload")

                            elif opcion2 == "3":
                                cmd = subprocess.run("apt install iaxflood")
                            elif opcion2 == "4":
                                cmd = subprocess.run("apt install git && git clone git://git.kali.org/packages/inundator.git")
                            elif opcion2 == "5":
                                cmd = subprocess.run("apt install inviteflood")
                            elif opcion2 == "6":
                                cmd = subprocess.run("apt install ipv6-toolkit")
                            elif opcion2 == "7":
                                cmd = subprocess.run("apt install mdk3")
                            elif opcion2 == "8":
                                cmd = subprocess.run("apt install reaver")
                            elif opcion2 == "9":
                                cmd = subprocess.run("apt install rtpflood")
                            elif opcion2 == "10":
                                cmd = subprocess.run("apt install slowhttptest")
                            elif opcion2 == "11":
                                cmd = subprocess.run("apt install t50")
                            elif opcion2 == "12":
                                cmd = subprocess.run("apt install termineter")
                            elif opcion2 == "13":
                                cmd = subprocess.run("apt install thc-ipv6")
                            elif opcion2 == "14":
                                cmd = subprocess.run("apt install thc-ssl-dos ")                                                                         
                            elif opcion2 == "back":
                                inicio()
                            elif opcion2 == "gohome":
                                inicio1()   
                            elif opcion2 == "0":
                                cmd = subprocess.run("apt install -y dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos")
                            else:
                                print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
                        while opcion1 == "11":
                            print ('''
\033[1;36m=+[ Password Attacks\033[1;m

 1) acccheck                19) Maskprocessor
 2) Burp Suite                20) multiforcer
 3) CeWL                21) Ncrack
 4) chntpw                22) oclgausscrack
 5) cisco-auditing-tool            23) PACK
 6) CmosPwd                24) patator
 7) creddump                25) phrasendrescher
 8) crunch                26) polenum
 9) DBPwAudit                27) RainbowCrack
10) findmyhash                28) rcracki-mt
11) gpp-decrypt                29) RSMangler
12) hash-identifier            30) SQLdict
13) HexorBase                31) Statsprocessor
14) THC-Hydra                32) THC-pptp-bruter
15) John the Ripper            33) TrueCrack
16) Johnny                34) WebScarab 
17) keimpx                35) wordlists 
18) Maltego Teeth            36) zaproxy 

0) Install all Password Attacks tools
                 
                        ''')
                            print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
                            opcion2 = input("\033[1;36mkat > \033[1;m")
                            if opcion2 == "1":
                                cmd = subprocess.run("apt install acccheck")

                            elif opcion2 == "2":
                                cmd = subprocess.run("apt install burpsuite")

                            elif opcion2 == "3":
                                cmd = subprocess.run("apt install cewl")
                            elif opcion2 == "4":
                                cmd = subprocess.run("apt install chntpw")
                            elif opcion2 == "5":
                                cmd = subprocess.run("apt install cisco-auditing-tool")
                            elif opcion2 == "6":
                                cmd = subprocess.run("apt install cmospwd")
                            elif opcion2 == "7":
                                cmd = subprocess.run("apt install creddump")
                            elif opcion2 == "8":
                                cmd = subprocess.run("apt install crunch")
                            elif opcion2 == "9":
                                cmd = subprocess.run("apt install git && git clone git://git.kali.org/packages/dbpwaudit.git")
                            elif opcion2 == "10":
                                cmd = subprocess.run("apt install findmyhash")
                            elif opcion2 == "11":
                                cmd = subprocess.run("apt install gpp-decrypt")
                            elif opcion2 == "12":
                                cmd = subprocess.run("apt install hash-identifier")
                            elif opcion2 == "13":
                                cmd = subprocess.run("apt install hexorbase")
                            elif opcion2 == "14":
                                cmd = subprocess.run("echo 'please visit : https://www.thc.org/thc-hydra/' ")
                            elif opcion2 == "15":
                                cmd = subprocess.run("apt install john")
                            elif opcion2 == "16":
                                cmd = subprocess.run("apt install johnny")
                            elif opcion2 == "17":
                                cmd = subprocess.run("apt install keimpx")
                            elif opcion2 == "18":
                                cmd = subprocess.run("apt install maltego-teeth")
                            elif opcion2 == "19":
                                cmd = subprocess.run("apt install maskprocessor")
                            elif opcion2 == "20":
                                cmd = subprocess.run("apt install multiforcer")
                            elif opcion2 == "21":
                                cmd = subprocess.run("apt install ncrack")
                            elif opcion2 == "22":
                                cmd = subprocess.run("apt install oclgausscrack")
                            elif opcion2 == "23":
                                cmd = subprocess.run("apt install pack")
                            elif opcion2 == "24":
                                cmd = subprocess.run("apt install patator")
                            elif opcion2 == "25":
                                cmd = subprocess.run("echo 'please visit : http://www.leidecker.info/projects/phrasendrescher/index.shtml' ")
                            elif opcion2 == "26":
                                cmd = subprocess.run("apt install polenum")
                            elif opcion2 == "27":
                                cmd = subprocess.run("apt install rainbowcrack")
                            elif opcion2 == "28":
                                cmd = subprocess.run("apt install rcracki-mt")
                            elif opcion2 == "29":
                                cmd = subprocess.run("apt install rsmangler")
                            elif opcion2 == "30":
                                print ("Sqldict is unavailable")
                            elif opcion2 == "31":
                                cmd = subprocess.run("apt install statsprocessor")
                            elif opcion2 == "32":
                                cmd = subprocess.run("apt install thc-pptp-bruter")
                            elif opcion2 == "33":
                                cmd = subprocess.run("apt install truecrack")
                            elif opcion2 == "34":
                                cmd = subprocess.run("apt install webscarab")
                            elif opcion2 == "35":
                                cmd = subprocess.run("apt install wordlists")
                            elif opcion2 == "36":
                                cmd = subprocess.run("apt install zaproxy")
                            elif opcion2 == "back":
                                inicio()
                            elif opcion2 == "gohome":
                                inicio1()   
                            elif opcion2 == "0":
                                cmd = subprocess.run("apt install -y acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy")
                            else:
                                print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
                        while opcion1 == "12" :
                            print ('''
\033[1;36m=+[ Reverse Engineering\033[1;m

 1) apktool
 2) dex2jar
 3) diStorm3
 4) edb-debugger
 5) jad    
 6) javasnoop
 7) JD-GUI
 8) OllyDbg
 9) smali
10) Valgrind
11) YARA

0) Install all Reverse Engineering tools
                 
                        ''')
                            print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
                            opcion2 = input("\033[1;36mkat > \033[1;m")
                            if opcion2 == "1":
                                cmd = subprocess.run("apt install apktool")

                            elif opcion2 == "2":
                                cmd = subprocess.run("apt install dex2jar")

                            elif opcion2 == "3":
                                cmd = subprocess.run("apt install python-diStorm3")
                            elif opcion2 == "4":
                                cmd = subprocess.run("apt install edb-debugger")
                            elif opcion2 == "5":
                                cmd = subprocess.run("apt install jad")
                            elif opcion2 == "6":
                                cmd = subprocess.run("apt install javasnoop")
                            elif opcion2 == "7":
                                cmd = subprocess.run("apt install JD")
                            elif opcion2 == "8":
                                cmd = subprocess.run("apt install OllyDbg")
                            elif opcion2 == "9":
                                cmd = subprocess.run("apt install smali")
                            elif opcion2 == "10":
                                cmd = subprocess.run("apt install Valgrind")
                            elif opcion2 == "11":
                                cmd = subprocess.run("apt install YARA")
                            elif opcion2 == "back":
                                inicio()
                            elif opcion2 == "gohome":
                                inicio1()   
                            elif opcion2 == "0":
                                cmd = subprocess.run("apt install -y apktool dex2jar python-diStorm3 edb-debugger jad javasnoop JD OllyDbg smali Valgrind YARA")
                            else:
                                print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
                        while opcion1 == "13" :
                            print ('''
\033[1;36m=+[ Hardware Hacking\033[1;m

 1) android-sdk
 2) apktool
 3) Arduino
 4) dex2jar
 5) Sakis3G    
 6) smali

0) Install all Hardware Hacking tools
                 
                        ''')
                            print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
                            opcion2 = input("\033[1;36mkat > \033[1;m")
                            if opcion2 == "1":
                                cmd = subprocess.run("apt install android-sdk")

                            elif opcion2 == "2":
                                cmd = subprocess.run("apt install apktool")

                            elif opcion2 == "3":
                                cmd = subprocess.run("apt install arduino")
                            elif opcion2 == "4":
                                cmd = subprocess.run("apt install dex2jar")
                            elif opcion2 == "5":
                                cmd = subprocess.run("apt install sakis3g")
                            elif opcion2 == "6":
                                cmd = subprocess.run("apt install smali")

                            elif opcion2 == "back":
                                inicio()
                            elif opcion2 == "gohome":
                                inicio1()   
                            elif opcion2 == "0":
                                cmd = subprocess.run("apt install -y android-sdk apktool arduino dex2jar sakis3g smali")
                            else:
                                print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
                        while opcion1 == "14" :
                            print ('''
\033[1;36m=+[ Extra\033[1;m

1) Wifresti
2) Squid3
                ''')
                            print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
                            opcion2 = input("\033[1;36mkat > \033[1;m")
                            if opcion2 == "1":
                                cmd = subprocess.run("git clone https://github.com/LionSec/wifresti.git && cp wifresti/wifresti.py /usr/bin/wifresti && chmod +x /usr/bin/wifresti && wifresti")
                                print (" ")
                            elif opcion2 == "2":
                                cmd = subprocess.run("apt install squid3")
                                print (" ")
                            elif opcion2 == "back":
                                inicio()
                            elif opcion2 == "gohome":
                                inicio1()

                inicio()
        inicio1()
    except KeyboardInterrupt:
        print ("Shutdown requested...Goodbye...")
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)

if __name__ == "__main__":
    main()