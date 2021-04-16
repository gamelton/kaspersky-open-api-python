# Kaspersky Open API
Kaspersky Security Center has Open API that understands web requests. By default it's running on port `13299`  
This is exemple to get used license on specific license key  

Notes to command  
- Replace `username` and `password` with your Kaspersky user  
   You could use local admin user on the Kasperky server  
- `username` and `password` are base64 encoded  
- Replace `kaspersky-server-address` with your Kaspersky server addresss  
- You run script with argument key id. That argument then used in `licenseid` variable  
   You could gey key number from Kaspersky Security Center MMC
- Output number of licenses used on the key  
