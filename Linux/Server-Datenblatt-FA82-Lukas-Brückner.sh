now=$(date)
ip=$(hostname -i)
gateway=$(ip route | grep default | cut -d " " -f 3)
dns=$(grep "nameserver" /etc/resolv.conf | cut -d " " -f 2)
uid=$(id -u)
gid=$(id -g $USER)
disk=$(sudo lsblk)
name="Lukas Brückner"
fqdn=$(hostname --fqdn)
creationDate=$(date +'%d.%m.%Y')

printf "%-16s%s" "FA82" "$name"
printf "%-20s" " "
printf "%s\n\n\n\n\n\n\n" "$now"
printf "%-16s" " "
printf "%s\n" "Server-Datenblatt"
printf "%-16s" " "
printf "%s\n\n\n\n\n" "================="
printf "%s\n" "Netzwerk"
printf "%s\n\n" "--------"
printf "%s\t\t" "FQDN:"
printf "%s\n" "$fqdn"
printf "%s\t" "IP / Netmask:"
printf "%s\n" "$ip"
printf "%s\t" "Gateway:"
printf "%s\n" "$gateway"
printf "%s\t\t" "DNS:"
printf "%s\n\n\n\n" "$dns"
printf "%s\n" "Benutzer"
printf "%s\n\n" "--------"
printf "%s\t" "User-Name:"
printf "%s\n" "$USER"
printf "%s\t\t" "UID:"
printf "%s\n" "$uid"
printf "%s\t\t" "GID:"
printf "%s\n\n\n\n" "$gid"
printf "%s\n" "Festplatte(n)"
printf "%s\n\n" "-------------"
printf "%s\n" "Belegung:"
printf "%s\n\n\n\n\n\n\n" "$disk"
printf "%s" "Diese Info wurde von "
printf "%s" "$name"
printf "%s" " am "
printf "%s" "$creationDate"
printf "%s\n" " erstellt."
