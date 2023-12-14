<html>
<body>
<div style="text-align:center">
<h2>Doctors</h2>
<hr/>
<form action="/doctor" method="get">
  <label for="search">Search Doctor</label>
  <input type="text" id="search" name="query" value="{{query}}"></input>
  <button type="submit">Search</button>
</form>
<table>
% for doctor in doctors:
  <tr>
  <td>{{str(doctor.name)}}</td>
  <td>{{str(doctor.specialization)}}</td>
  <td><a href="/doctor/update/{{str(doctor.id)}}">update</a></td>
  <td><a href="/doctor/delete/{{str(doctor.id)}}">delete</a></td>
  </tr>
% end
</table>
<hr/>
<a href="/doctor/add">Add a new entity</a>
<hr/>
</div>
</body>
</html>