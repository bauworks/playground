<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Task extends Model implements TaskInterface
{
    use HasFactory;

    protected $table = 'tasks';

    protected $primaryKey = 'id';

    public function findAllTasks()
    {
        return Task::all();
    }

}
