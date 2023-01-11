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
        $tmptask = clone $tasks[0];
        $tmptask->name = $this->plusone->name;
        $tasks[count($tasks)] = $tmptask;
        return $tasks;
    }

}
