<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
//use App\Models\TaskInterface;
use App\Models\Task;
use App\Models\TaskAddition;

class TaskController extends Controller
{

    // public function __construct()
    public function __construct(Task $task)
    {
        // $this->task = new Task();
        $this->task = $task;
    }

    // public function index(TaskInterface $task)
    // public function index(Task $task)
    public function index(TaskAddition $addition)
    {
        // $tasks = \DB::table('tasks')->get();
        // return $tasks;

        // $tasks = Task::select()->get();
        // foreach($tasks as $task){
        //     echo $task->name . "<br>";
        // }

        // $tasks = Task::select()->get();
        // return view('tasks', [
        //     'tasks' => $tasks,
        // ]);

        $tasks = $this->task->findAllTasks();
        // $tasks = $task->findAllTasks();
        $tasks = $addition->plusOne($tasks);

        return view('tasks', compact('tasks'));

    }

}
