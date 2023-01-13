<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
//use App\Models\TaskInterface;
use App\Models\Task;
use App\Models\TaskAddition;
use App\Models\Priority;

class TaskController extends Controller
{

    // public function __construct()
    public function __construct(Task $task, priority $priority)
    {
        // $this->task = new Task();
        $this->task = $task;
        $this->priority = $priority;
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

        // $tasks = $this->task->findAllTasks();
        // $tasks = $task->findAllTasks();
        
        // すべてのタスクをDBから取得
        $tasks = $this->task->findAllTasksWithPriority();
        // dd($tasks);

        // // 優先度、登録順（ID）でソート
        // foreach($tasks as $key => $value)
        // {
        //     $sort_keys[$key] = $value['rank'];
        // }
        // //dd($sort_keys);
        // array_multisort($sort_keys, SORT_ASC, $tasks);

        // タスクの末尾にダミータスクを追加（DI検証用）
        $tasks = $addition->plusOne($tasks);

        return view('task.tasks', compact('tasks'));

    }


    /**
     * 登録画面表示
     * @param Request $request
     * @return \Illuminate\Contracts\View\Factory|\Illuminate\Contracts\View\View
     */
    public function create(Request $request)
    {
        //優先順位取得
        $priorities = $this->priority->findAllPriority();
        return view('task.create', compact('priorities'));
    }

    /**
     * 登録処理
     */
    public function store(Request $request)
    {
        // dd("request : " . $request);
        $registerTask = $this->task->InsertTask($request);
        return redirect()->route('task.tasks');
    }

    /**
     * 削除処理
     */
    // public function destroy($id)
    public function destroy(Request $request)
    {
        $id = $request->id;
        // dd('id : ' . $id);
        $this->task->destroy($id);
        return redirect()->route('task.tasks');
    }
}
