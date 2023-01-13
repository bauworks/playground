<?php

use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/default', function () {
    return view('welcome');
});

Route::get('/hello',
    [App\Http\Controllers\HelloController::class, 'index']
);


/**
 * タスクダッシュボード表示
 */
Route::get('/',
    [App\Http\Controllers\TaskController::class, 'index']
)->name('task.tasks');

/**
 * 新タスク追加
 */
Route::get('/create',
    [App\Http\Controllers\TaskController::class, 'create']
)->name('task.create');

Route::post('/store',
    [App\Http\Controllers\TaskController::class, 'store']
)->name('task.store');


/**
 * タスク削除
 */
Route::post('/destroy{id}',
    [App\Http\Controllers\TaskController::class, 'destroy']
)->name('task.destroy');

