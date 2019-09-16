# VIRTUAL MACHINE CONNECTION

-install openVPN

sudo openvpn --config LSB_ecc

ssh -i keys/um_ecc um87@m87.lsb.biocomp.unibo.it         or            **ssh lab2**

source /opt/conda/bin/activate

### .ssh/config

Host lab2
        HostName m87.lsb.biocom.unibo.it
        User um87                         
        IdentityFile /home/rambo/keys/um87_id_rsa



## move file

local to virtual

scp -i <key> <source> um87_ecc:<destination>

virtual to local

scp -i <key> um87_ecc:<source> <destination>

