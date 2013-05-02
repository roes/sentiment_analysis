# -*- coding: utf-8 -*-
<!DOCTYPE html>
<html>
<head>

  <meta charset="utf-8">
  <title>Online Reputation Management</title>
  <link rel="stylesheet" href="/static/style.css">
  <script src="//ajax.googleapis.com/ajax/libs/jquery/2.0.0/jquery.min.js"></script>
  <script type="text/javascript" src="https://www.google.com/jsapi"></script>
  <script type="text/javascript">
  google.load('visualization', '1.0', {'packages':['corechart']});

  function drawGraph(rawdata){
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Date');
    data.addColumn('number', 'Reputation');
    data.addRows(rawdata.reputation);

    var options = {'title':'Reputation change over time'};
    var chart = new google.visualization.LineChart($("#graph_div")[0]);
    chart.draw(data, options);
  }
  </script>

</head>

<body>

  <div id="header">
    <div class="wrap">
      <h1>Online Reputation Management</h1>
    </div>
  </div>

  <div id="page">
    <ul id="companies">
    % if companies:
      % for company in companies:
      <li>
        <span class="company">
          <a href="#">${company}</a>
        </span>
      </li>
      % endfor
    % else:
      <li>There are no companies to track</li>
    % endif
    </ul>
  </div>

  <div id="graph_div"></div>

  <script>
    $("span.company a").click(function(){
      var company = $(this).text();
      $.ajax({
        type: "GET",
        url: "/graph/"+company,
        success: drawGraph
      });
      return false;
    });
  </script>

</body>
</html>
