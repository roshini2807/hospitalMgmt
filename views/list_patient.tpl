<html>
<body>
<div style="text-align:center">
<h2>Patients</h2>
<hr/>
<table>
% for patient in patients:
  <tr>
    <td>{{str(patient.name)}}</td>
    <td>{{str(patient.age)}}</td>
    % if(patient.docID):
      <td>{{patient.docID.name}}</td>
    % end
    <td><a href="/update/{{str(patient.id)}}">update</a></td>
    <td><a href="/delete/{{str(patient.id)}}">delete</a></td>
  </tr>
% end
</table>
<hr/>
<a href="/add">Add a new entity</a>
<hr/>
</div>
</body>
</html>