#here we using google chart for  data visualization 
#these are the code for visualization

import csv

top = """
<html>
  <head>
      <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://fonts.googleapis.com/css2?family=Galada&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@800&display=swap" rel="stylesheet">
    <link href="https://cdn.bootcss.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet"> 
    <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap" rel="stylesheet">
    <script src="https://cdn.bootcss.com/popper.js/1.12.9/umd/popper.min.js"></script>
    <script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://cdn.bootcss.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="https://www.w3schools.com/lib/w3.css">
    <link rel="icon" href="https://cdn3.iconfinder.com/data/icons/picons-social/57/43-twitter-512.png"
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@800&display=swap" rel="stylesheet">
    <link href="https://cdn.bootcss.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet">
    <link href="{{ url_for('static', filename='css/style.css') }}" rel="stylesheet">
    <style>
	.bg-dark {
		background-color: #42678c!important;
	}
	#result {
		color: #0a1c4ed1;
	}
	*{
  box-sizing: border-box;
    }
    .column {
          float: left;
          width: 25%;
          padding: 10px;
          height: 160px;
        }

    .row:after {
          content: "";
          display: table;
          clear: both;
        }
	</style>
    <title>Sentiment Analysis COVID-19</title>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['bar']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['Keyword', 'Positive', 'Negative', 'Neutral'],
""" 

bottom = """

   ]);
        var options = {
          chart: {
            
            
          }
        };

        var chart = new google.charts.Bar(document.getElementById('columnchart_material'));

        chart.draw(data, options);
      }
    </script>
  </head>
  <body>
  <div class="w3-top">
      <div class="w3-bar " >
        
        <span class="w3-right w3-mobile w3-red" style="border-radius: 12px;margin-right:30px">
          <a class="w3-bar-item w3-button w3-mobile w3-hover-aqua" href="#" style="padding-right:60px;border-radius: 12px;">Home</a>
          <a class="w3-bar-item w3-button w3-mobile w3-hover-aqua" href="#dashboard" style="padding-right:60px;border-radius: 12px;">Dashboard</a>
          <a class="w3-bar-item w3-button w3-mobile w3-hover-aqua" href="#about" style="padding-right:60px;border-radius: 12px;">About</a>
          <a class="w3-bar-item w3-button w3-mobile w3-hover-aqua" href="#contact" style="padding-right:60px;border-radius: 12px;">Contact</a>
        </span>
      </div>
    </div>
    

        <!-- SHOWCASE -->
    <section class="showcase" style="background-image:url('showcase.png'); width: 100%; height: 100%;  background-repeat: no-repeat;background-size: cover;padding-top:100px;">
      <div class="w3-container ">

  <img src="e1.png" style="height:250px;width:250px;position:absolute;bottom:8px;left: 16px;margin-bottom:20px;">
 <div class="w3-container ">
        <div id="content" style="margin-top:2em">
		<div class="container">
		  <div class="row">
			<div>
	
			<div>
				<div>
				
		</div>


			
			
			 
		  </div>
		</div>
		</div>
    </div>
    
    </section>
    <p id="dashboard">  </p>
    <p id>  </p>
    <br>
   
      <div class="w3-container w3-center w3-aqua">
       <h3>Dashboard</h3>
       
      </div>
      <br/>
    <div id="columnchart_material" style="width: 1280px; height: 500px;"></div>
    <!-- SECTION 1 -->
    <br/>
    <p id="about"></p>
    <section class="section w3-blue" >
      <div class="w3-container w3-center">
       
        
        <h2>About </h2>
      
           <p> Corona remains a major burden on global health, with million cases worldwide.
         Till now there is no Vaccination for corona.So that,we have to stay at home to prevent ourself.</p>
          <p>With this application we will be able to find if lockdown is extended what will be the People reaction.</p>
          <p>It may be positive or negative or neutral.</p>
          
         
      </div>
     
    </section>
    <!-- ABOUT -->
     <br/>
    <section  class="section">
      <div class="w3-container">
        <div class="w3-row-padding">
          <div class="w3-col m5">
            <img src="https://www.adexchanger.com/wp-content/uploads/2020/04/appsfightCOVID_WHO.gif" style="height:400px;width:500px;">
          </div>
          <div class="w3-col m7">
            <button onclick="accFunction('what')" class="w3-btn-block w3-left-align">
            <b>Causes</b>
            </button>

            <div id="what" class="w3-container">
              <p>When people with COVID-19 breathe out or cough, they expel tiny droplets that contain the virus. These droplets can enter the mouth or nose of someone without the virus, causing an infection to occur.</p>
            </div>

            <button onclick="accFunction('who')" class="w3-btn-block w3-left-align">
           <b> Symptoms </b></button>

            <div id="who" class="w3-container w3-hide">
             
              <p>  - Fever </p>
              <p>  - Cough</p>
              <p>  - Tiredness</p>
              <p>  - Difficulty in breathing</p>
              <p> - Sore throat</p>
              <p> - Runny nose</p>
           </div>

            <button onclick="accFunction('where')" class="w3-btn-block w3-left-align">
           <b> Prevention </b></button>

            <div id="where" class="w3-container w3-hide">
              <p>There is no vaccination till now . So some of the remedial measures are </p>

            <p> - Wash your hands often</p>
            <p>- Wear a face Mask</p>
            <p>- Avoid contact with sick people</p>
            <p>- Always cover your cough or sneez</p>
            </div>
          </div>
        </div>
      </div>
    </section>
    <br/>
   <!-- CONTACT HEADING -->
 

    <!-- CONTACT -->
    <section class="section" id="contact">
      <div class="w3-container">
        <div class="w3-card-4">
          <div class="w3-container w3-dark-grey">
            <h2>Contact Us</h2>
          </div>
            <form class="w3-container w3-padding-xlarge">
            <div class="row">
  <div class="column" style="background-color:#aaa;">
    <h3>Name : Sourav R </h3>
    <p>Mail : off.sourav@gmail.com </p>
     <p>Contact : 8248577262 </p>
  </div>
  <div class="column" style="background-color:#bbb;">
    <h3>Name : Jeeva K </h3>
    <p>Mail    : jeeva1212k@gmail.com </p>
    <p>Contact : 8608781628 </p>
  </div>
<div class="column" style="background-color:#ccc;">
    <h3>Name : Abinaya S </h3>
    <p>Mail : abinaya@gmail.com </p>
     <p>Contact : 8300375075 </p>
  </div><div class="column" style="background-color:#ddd;">
    <h3>Name : Dhivyabharathi S </h3>
    <p>Mail : dhivyakty6@gmail.com </p>
     <p>Contact : 9080192385 </p>
  </div>
</div>
            </form>
          </div>
      </div>
    </section>

    <script>
      function accFunction(id) {
          var x = document.getElementById(id);
          if (x.className.indexOf("w3-show") == -1) {
              x.className += " w3-show";
          } else {
              x.className = x.className.replace(" w3-show", "");
          }
      }
      </script>
  </body>
  <footer>
    <script src="{{ url_for('static', filename='js/main.js') }}" type="text/javascript"></script>    
</footer>
</html>
"""

# open the results file

csv_f =  csv.reader(open("Final.csv", "r",encoding='utf8'))
# create a chart file, open it in write mode and add the top html section
with  open('chart.html','w') as myfile:
    myfile.write(top)

# write contents of the results file to the chart
with  open('chart.html','a') as myfile:
    for row in csv_f:
        if(len(row)!=0):
            myfile.write('[\''  + row[0] + '\', ' + row[2] + ', ' + row[3] + ', ' + row[4] + '],\n')

            # write the bottom html section to the file
with open("chart.html", "a") as myfile:
    myfile.write(bottom)

print ('\'chart.html\' created')