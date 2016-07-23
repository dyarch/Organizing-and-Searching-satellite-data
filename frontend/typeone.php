<head>
	<body>
		<?php
			$path = 'C:\xampp\htdocs\mncfc\Typeone.txt';
			$myfile = fopen($path,"w") or die("Unable to open file.");
			$type = "1"."\n";
			fwrite($myfile, $type);
			$startdate = $_GET["startdate"]."\n";
			fwrite($myfile, $startdate);
			$enddate = $_GET["enddate"]."\n";
			fwrite($myfile, $enddate);
			$sensor = $_GET["sensor"]."\n";
			fwrite($myfile, $sensor);
			$startpath = $_GET["startpath"]."\n";
			fwrite($myfile, $startpath);
			$startrow = $_GET["startrow"]."\n";
			fwrite($myfile, $startrow);
			$endpath = $_GET["endpath"]."\n";
			fwrite($myfile, $endpath);
			$endrow = $_GET["endrow"]."\n";
			fwrite($myfile, $endrow);
			fclose($myfile);
			$execute_python = system('C:\Python27\python.exe C:\xampp\htdocs\mncfc\pathandrow.py', $retval);
			echo '<pre>'.file_get_contents('C:\xampp\htdocs\mncfc\Queryoneres.txt').'</pre>';

		?>
	</body>
</head>