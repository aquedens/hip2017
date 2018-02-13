<?php
 error_log("Logging some data");
error_log($_REQUEST["direction"]);
$direction = $_REQUEST["direction"];
switch ($direction){
case "buttonforward":
	error_log("forward");
	$rip = shell_exec("ls");
	error_log($rip);
	break;
case "buttonbackward":
	error_log("backward");
	break;
case "buttonright":
	error_log("right");
	break;
case "buttonleft":
	error_log("left");
	break;
default:
	error_log("unknown direction");
}



 exit("$direction");
?>
