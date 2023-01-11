<?php

namespace App\Providers;

use Illuminate\Support\ServiceProvider;

class DbModelProvider extends ServiceProvider
{
    /**
     * Register any application services.
     *
     * @return void
     */
    public function register()
    {
        // タスクテーブル
        // $this->app->bind(\App\Models\TaskInterface::class, \App\Models\Task::class);
        $this->app->bind(\App\Models\Task::class, \App\Models\Task::class);
        $this->app->bind(\App\Models\TaskAddition::class, \App\Models\TaskAddition::class);
        $this->app->bind(\App\Models\TaskPlusOne::class, \App\Models\TaskPlusOne::class);

    }

    /**
     * Bootstrap any application services.
     *
     * @return void
     */
    public function boot()
    {
        //
    }
}
