<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Task extends Model implements TaskInterface
{
    use HasFactory;

    // モデルに関連付けるテーブル
    protected $table = 'tasks';

    // プライマリキー
    protected $primaryKey = 'id';

    // 登録・更新可能カラムの指定
    protected $fillable = [
        'id',
        'name',
        'priority',
        'is_done',
        'created_at',
        'updated_at'
    ];

    // 全件データ取得
    public function findAllTasks()
    {
        return Task::all();
    }

    // 優先順位付きで全件データ取得
    public function findAllTasksWithPriority()
    {
        return Task::select("tasks.id",
                            "tasks.name",
                            "tasks.priority",
                            "tasks.is_done",
                            "tasks.created_at",
                            "tasks.updated_at",
                            "priorities.priority",
                            "priorities.explanation",
                            "priorities.rank"
                            )
                ->join('priorities', 'priorities.priority', '=', 'tasks.priority')
                ->orderBy('priorities.rank', 'ASC')
                ->orderBy('tasks.id', 'ASC')
                ->get();
    }

    // タスク登録
    public function InsertTask($request)
    {
        return $this->create([
            'name'  => $request->task_name,
            'priority' => $request->priority,
            'is_done' => 0,
            'created_at' => date('Y-m-d H:i:s'),
            'updated_at' => date('Y-m-d H:i:s'),
        ]);
    }

    // タスク削除
    public function deleteTaskById($id)
    {
        return $this->destroy($id);
    }

}
