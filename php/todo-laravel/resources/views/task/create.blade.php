@extends('layouts.app')

@section('content')
<h1>タスクの新規登録</h1>
<form action="{{ route('task.store') }}" method="POST">
@csrf
    <p>
        <label for="task_name">{{ __('タスク') }}</label>
        <input type="text" name="task_name" id="task_name">
        <br>
        <label for="priority">{{ __('優先度') }}</label>
        <select id="priority" name="priority">
            @foreach ($priorities as $priority)
                <option value="{{ $priority->priority }}" {{ $priority->priority === 'NORMAL' ? 'selected' : ''}}>{{ $priority->explanation }}</option>
            @endforeach
        </select>
    </p>

    <button type="submit" >{{ __('登録') }}</button>
</form>
<a href="{{ route('task.tasks') }}" type="button">{{ __('一覧画面へ') }}</a>
@endsection