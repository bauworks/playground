<table border="1">
    <thead>
        <tr>
            <th>タスク</th>
        </tr>
    </thead>
    <tbody>
        @foreach($tasks as $rec)
            <tr>
                <td>{{$rec->name}}</td>
            </tr>
        @endforeach
    </tbody>
</table>
