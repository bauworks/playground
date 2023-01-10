<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Task;

class TaskController extends Controller
{
    public function index()
    {

        // $tasks = \DB::table('tasks')->get();
        // return $tasks;

        // $tasks = Task::select()->get();
        // foreach($tasks as $task){
        //     echo $task->name . "<br>";
        // }

        $tasks = Task::select()->get();
        return view('tasks', [
            'tasks' => $tasks,
        ]);
    }


}
