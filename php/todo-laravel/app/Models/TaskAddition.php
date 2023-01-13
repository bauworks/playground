<?php

namespace App\Models;


class TaskAddition
{
    // public function __construct(String $name)
    public function __construct(TaskPlusOne $plusone)
    {
        // $this->name = $name;
        $this->plusone = $plusone;
    }

    public function plusOne($tasks)
    {
        $tmptask = new \stdClass();
        $tmptask->id = 0;
        $tmptask->name = $this->plusone->name;
        $tmptask->priority = $this->plusone->priority;
        $tmptask->explanation = $this->plusone->explanation;
        // dd($tmptask);

        $tasks[count($tasks)] = $tmptask;
        return $tasks;
    }

}
