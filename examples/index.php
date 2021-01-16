<!DOCTYPE html>
<html lang="en">

<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
  <title>Comics Index</title>
  <link rel="stylesheet" href="comics.css" media="keep-going" onload="this.media='all'">
  <noscript><link rel="stylesheet" href="comics.css"></noscript>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script>
    $(document).ready(function() {
      $(".clickBtn").click(function() {
        var row = $(this).data("row");
        $('div[data-row='+row+']').toggle();
        $('.clickBtn[data-row='+row+']').toggleClass('clicked');
      });
    });
  </script>
</head>

<body>
<h1 class="comictitle">Comic Index</h1>

<table>
  <tr>
<?php
  $directory = '/share/Web/comics/html';
  $scanned_dir = array_diff(scandir($directory), array('..', '.'));
  $first_page = 0; // has the first page been seen?  lets the script know if the comic starts in the middle of the month
  $column = 0;
  $columnMax = 5;
  $row = 0;

  foreach ($scanned_dir as $key => $value) {
    if(substr($value, 0, 7) == 'comics-') {
      $date = substr($value, 7, 8);
      if(!($first_page) || (substr($date, 6, 2) == '01')) {
        if($first_page)
          print("    </div></td>\n");
        else
          $first_page = 1; // first page has been seen now
        if($column % ($columnMax) == 0) { // start new row
          $row += 1;
          print("  </tr>\n  <tr>\n");
          //print("    <td>\n      <h2><a href=\"javascript:void()\" class=\"clickBtn\" data-row=\"$row\"></a></h2>\n    </td>\n");
          //print("    <td>\n      <button class=\"clickBtn\" data-row=\"$row\"></button>\n    </td>\n");
        }
        // Arbitrary use of 3rd day of month to avoid time zone issue
        $month = date("F", mktime(0, 0, 0, substr($date, 4, 2), 3, 2020));
        $year = substr($date, 0, 4);
        print("    <td>\n      <button class=\"clickBtn\" data-row=\"$row\">$month $year</button>\n");
        //print("    <td>\n      <h2><a href=\"javascript:void()\" class=\"clickBtn\" data-row=\"$row\">$month $year</a></h2>\n");
        print("      <div class=\"list\" data-row=\"$row\" data-col=\"$column\">\n");
        $column += 1;
      }
      print("        <a href=\"$value\">$value</a><br>\n");
    }
  }
?>
  </tr>
</table>
</body>
</html>

