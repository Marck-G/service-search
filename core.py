import json
import socket


def odoo_port_pscan(s, port, target):
    try:
        con = s.connect((target,port))
        return True
    except:
        return False

def odoo_host_search(host_conf, host_port, barra, update, startIP = 0, ipText = False):
    print (f"Configuracion\n host:{host_conf}\n port: {host_port}")
    TOP = 254
    # s.settimeout(20)
    for ip in range(startIP, TOP + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)
        host = host_conf.replace("X", f"{ip}")
        if ipText:
            ipText.config(text=f"IP:{host}")
        print("Host a probar ", host)
        barra["value"] = int(((ip-startIP) / (TOP - startIP))*100)
        update()
        if odoo_port_pscan(s, host_port, host):
            print("Odoo está en ", host)
            s.close()
            return host
        s.close()

def core_load_conf():

    try:
        file = open("odoo-search.conf")
        conf = json.loads("\n".join(file.readlines()))
        return conf
    except:
        conf = {
            "core": {
                "hostMask" : "192.168.0.X",
                "defaultPort" : 8069,
                "startIP": 0,
                "searchApp": "odoo"
            }
        }
        f = open("odoo-search.conf", "xt")
        f.writelines(json.dumps(conf, indent=2))
    file = open("odoo-search.conf")
    conf = json.loads("\n".join(file.readlines()))
    return conf
