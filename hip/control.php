<!DOCTYPE html>
<html lang="en">
            <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="js/jquery-3.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script>window.jQuery || document.write('<script src="../../../../assets/js/vendor/jquery.min.js"><\/script>')</script>
    <script src="js/bootstrap.js"></script>

    <head>
        <meta http-equiv="content-type" content="text/html; charset=UTF-8">
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <meta name="description" content="The Controller For An RC Car Drone">
        <meta name="author" content="Alex Quedens">
        <link rel="icon" href="/var/www/html/imgs/icon.png">

        <title>RC Car Drone Controller - Home</title>

        <!-- Bootstrap core CSS -->
        <link href="css/bootstrap.css" rel="stylesheet">
	<link href="/css/control.css" rel="stylesheet">
        
    </head>
    <body alink="white" vlink="whtie">
        
        
            <header>
      <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
        <a class="navbar-brand" href="index.php">RC Camera Car</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarCollapse">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item active">
              <a class="nav-link" href="index.php">Home</a>
            </li>
            <li class="nav-item active">
              <a class="nav-link" href="control.php">Control</a>
            </li>
            <li class="nav-item active">
              <a class="nav-link" href="details.php">Details</a>
            </li>
          </ul>
        
        </div>
      </nav>
    </header>
        <br><br><br>
        <div id="paragraph-welcome">
	<table style="width:100%">
		<tr>
			<td valign="top">
				<h1>Action Log</h1>
				<div class="floatleft">
					<span id="actionlog"></span>
				</div>
			</td>
			<td>
        			<div class="floatcenter">
					<iframe src="http://localhost:9090/stream/webrtc"></iframe></th>
				</div>
			</td>
			<td valign="top">
				<div id="directionbutton" class="floatright">
					<button id="buttonforward">forward</button>
					<button id="buttonbackward">backwards</button>
					<button id="buttonleft">left</button>
					<button id="buttonright">right</button>
				</div>
			</td>
		</tr>
        </div>

	<!-- Placed at the end of the document so the pages load faster -->
    	<!-- <script src="js/jquery-3.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    	<script>window.jQuery || document.write('<script src="../../../../assets/js/vendor/jquery.min.js"><\/script>')</script>
        -->
	<script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    	<script src="js/bootstrap.js"></script>

	<script src="/js/control.js">
		
		
	</script>


    </body>

</html>