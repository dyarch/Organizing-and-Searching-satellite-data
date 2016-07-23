<head>
	<body>
		<?php
			$path = 'C:\xampp\htdocs\mncfc\Typetwo.txt';
			$myfile = fopen($path,"w") or die("Unable to open file.");
			$type = "2"."\n";
			fwrite($myfile, $type);
			$startdate = $_GET["startdate"]."\n";
			fwrite($myfile, $startdate);
			$enddate = $_GET["enddate"]."\n";
			fwrite($myfile, $enddate);
			$sensor = $_GET["sensor"]."\n";
			fwrite($myfile, $sensor);
			$ullat = $_GET["ullat"]."\n";
			fwrite($myfile,$ullat);
			$ullon = $_GET["ullon"]."\n";
			fwrite($myfile,$ullon);
			$lrlat = $_GET["lrlat"]."\n";
			fwrite($myfile,$lrlat);
			$lrlon = $_GET["lrlon"]."\n";
			fwrite($myfile,$lrlon);
			fclose($myfile);
			$execute_python = system('C:\Python27\python.exe C:\xampp\htdocs\mncfc\latandlon.py', $retval);
			echo '<pre>'.file_get_contents('C:\xampp\htdocs\mncfc\Querytwores.txt').'</pre>';
		?>
	</body>
</head>