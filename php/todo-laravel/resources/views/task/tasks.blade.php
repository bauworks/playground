@extends('layouts.app')

@section('content')
<a href="{{ route('task.create') }}">タスクの新規登録</a>
<table border="1">
    <thead>
        <tr>
            <th>No</th>
            <th>タスク</th>
            <th>優先度</th>
            <th>削除</th>
        </tr>
    </thead>
    <tbody>
        <?php $loopcount = 0; ?>
        @foreach($tasks as $rec)
            <tr>
                <?php $loopcount++; ?>
                <td>{{ $loopcount }}</td>
                <td>{{ $rec->name }}</td>
                <td>{{ $rec->explanation }}</td>
                <td>
                    <?php if($rec->id != 0): ?>
                    <form action="{{ route('task.destroy', ['id'=>$rec->id]) }}" method="POST">
                        @csrf
                        <button type="submit">削除</button>
                    </form>
                    <?php endif; ?>
                </td>
            </tr>
        @endforeach
    </tbody>
</table>
@endsection