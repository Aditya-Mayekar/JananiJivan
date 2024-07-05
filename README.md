# JananiJivan🤰
<h2>JananiJivan is a dedicated platform designed by Sanjeevani Gupta and I to support pregnant women in rural India.</h2> 
<h3>The website offers vital services to ensure a healthy and informed pregnancy journey:</h3>
<ul>
  <li>Doctor Consultations🧑‍⚕️: <br>Connect with doctors via Google Meet for professional medical advice.</li><br>
  <li>Hospital Locator🏥: <br>Easily find nearby hospitals for emergency and routine check-ups.</li><br>
  <li>Dietary Guidance🥝: <br>Access a detailed table outlining essential nutrition and diet recommendations during pregnancy.</li><br>
  <li>Government Schemes📝: <br>Download a comprehensive PDF containing information on various government schemes available for pregnant women.</li><br>
</ul>
Empowering women💪 with the resources and support they need for a safe and healthy pregnancy.

# Installation Steps-
<ul>
  <li>
    Step 1: Install and configure <b>MySQL</b> first, as it is utilized in the backend database, on your device.
  </li>
  <br>
  <li>
    Step 2: Now create a database named as <b>collegedb.</b>
  </li>
  <br>
  <li>
    Step 3: Inside the <b>collegedb</b> database, create a table <b>scrapedemo.</b><br>
    The <b>scrapedemo</b> table should have the following <b>columns</b> with the mentioned datatypes-<br>
    WeekDays varchar(50)<br>
    PreBreakfast varchar(500)<br>
    Breakfast varchar(500)<br>
    MorningSnack varchar(500)<br>
    Lunch varchar(500)<br>
    EveningSnack varchar(500)<br>
    Dinner varchar(500)<br>
  </li>
  <br>
  <li>
    Step 4: Once the table is created with the above mentioned columns, open the <b>datascrape.py</b> file and run the server.<br>
    Paste the following text in URL - <b>"/scrape-and-insert"</b> and press Enter. You'll receive the message that the data has been successfully inserted in the database.
  </li>
  <br>
  <li>
    Step 5: Now install <b>Python along with Flask, bs4(BeautifulSoup), render_template, mysql.connector, request Libraries.</b>
  </li>
  <br>
  <li>
    Step 6: After installing the Libraries, open the <b>app.py file</b> and run the server.<br>
    Press Ctrl and Click on the address provided in the terminal, this will launch the website.
  </li>
</ul>
