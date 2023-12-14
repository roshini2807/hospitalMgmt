<html>
<body>
<div style="text-align:center">
<hr/>
<form action="/update" method="post">
  <input type="hidden" name="id" value="{{str(patient.id)}}"/>
  <p>Name:<input name="name" value="{{patient.name}}"/></p>
  <p>Age:<input name="age" value="{{patient.age}}"/></p>
  <p>Doctor: </p>
  <select name="docID" value="{{docID}}">
  <option value="none">None</option>
  % for doctor in doctors:
    <option value="{{doctor.id}}">{{doctor.name}}</option>
  % end
  </select>
  <p><button type="submit">Submit</button></p>
<form>
<hr/>
</div>
<body>
</html>