<!DOCTYPE html>
<html lang="en">

<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
  <title>Comics Index</title>
  <link rel="stylesheet" href="comics.css" media="keep-going" onload="this.media='all'">
  <noscript><link rel="stylesheet" href="comics.css"></noscript>
</head>

<body>
<h1 class="comictitle">Comic Index</h1>

<table>
  <tr>
<?php
  $directory = '/share/Web/comics/html'; //Set this to your comic html folder
  $scanned_dir = array_diff(scandir($directory), array('..', '.'));
  $first_page = 0;
  $column = 0;
  $columnMax = 5; //Sets the table width (one month per column)

  foreach ($scanned_dir as $key => $value) {
    if(substr($value, 0, 7) == 'comics-') {
      $date = substr($value, 7, 8);
      if(!($first_page) || (substr($date, 6, 2) == '01')) {
        $column += 1;
        if($first_page)
          print("    </td>\n");
        else
          $first_page = 1;
        if($column % ($columnMax + 1) == 0) {
          print("  </tr>\n  <tr>\n");
        }
        // Arbitrary use of 3rd day of month to avoid time zone issue
        $month = date("F", mktime(0, 0, 0, substr($date, 4, 2), 3, 2020));
        $year = substr($date, 0, 4);
        print("    <td>\n      <h2>$month $year</h2>\n");
      }
      print("      <a href=\"$value\">$value</a><br>\n");
    }
  }
?>
  </tr>
</table>
</body>
</html>

