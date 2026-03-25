import pyshark

file_name = "capture.pcapng"
out_zip_name = "out.zip"

capture = pyshark.FileCapture(file_name)

dns_hostnames = []

for packet in capture:
    if "dns" in packet and packet.dns.flags_response == 'True' and "local" not in packet.dns.qry_name:
        dns_hostnames.append(packet.dns.qry_name)

sect_hex = []
for host in dns_hostnames:
    sect_hex.append(host.split(".")[1])

decod = []

for sect in sect_hex:
    try:
        decod.append(bytes.fromhex(sect))
    except:
        pass

full = b"".join(decod)
with open(out_zip_name, "wb") as file:
    file.write(full)