<html>
<body>
<hr/>
<div style="text-align:center">
<form action="/doctor/update" method="post">
  <input type="hidden" name="id" value="{{str(doctor.id)}}"/>
  <p>Name:<input name="name" value="{{doctor.name}}"/></p>
  <p>Specialization:<input name="specialization" value="{{doctor.specialization}}"/></p>
  <p><button type="submit">Submit</button></p>
<form>
</div>
<hr/>
<body>
</html>