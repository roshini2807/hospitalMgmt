<html>
<body>
<hr/>
<div style="text-align:center">
<h2>Patient Details: </h2>
<form action="/add" method="post">
  <p>Name:<input name="name"/></p>
  <p>Age:<input name="age"/></p>
  <p>Doctor: 
  <select name="docID">
  <option value="none">None</option>
  % for doctor in doctors:
    <option value="{{doctor.id}}">{{doctor.name}}</option>
  % end
  </select></p>
  <p><button type="submit">Submit</button></p>
<form>
</div>
<hr/>
<body>
</html>