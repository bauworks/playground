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
);

// /**
//  * 新タスク追加
//  */
// Route::post('/task',
//     [App\Http\Controllers\TaskController::class, 'store']
// );

// /**
//  * タスク削除
//  */
// Route::delete('/task/{task}',
//     [App\Http\Controllers\TaskController::class, 'destroy']
// );

