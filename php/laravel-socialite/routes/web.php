<?php

use App\Http\Controllers\ProfileController;
use Illuminate\Support\Facades\Route;
use Laravel\Socialite\Facades\Socialite;
use App\Models\User;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/dashboard', function () {
    return view('dashboard');
})->middleware(['auth', 'verified'])->name('dashboard');

Route::middleware('auth')->group(function () {
    Route::get('/profile', [ProfileController::class, 'edit'])->name('profile.edit');
    Route::patch('/profile', [ProfileController::class, 'update'])->name('profile.update');
    Route::delete('/profile', [ProfileController::class, 'destroy'])->name('profile.destroy');
});


Route::get('/auth/redirect', function () {
    return Socialite::driver('github')->redirect();
});

Route::get('/auth/callback', function () {

    $socialiteUser = Socialite::driver('github')->user();
    // dd($socialiteUser);

    $user = User::updateOrCreate([
        'email' => $socialiteUser->email,
    ], [
        'name' => $socialiteUser->name,
        'provider_id' => $socialiteUser->id,
        'provider' => 'github',
        'password' => $socialiteUser->token,
    ]);
 
    Auth::login($user);

    return redirect('/dashboard');

});



Route::get('/auth/redirect-google', function () {
    return Socialite::driver('google')->redirect();
});

Route::get('/auth/callback-google', function () {

    $socialiteUser = Socialite::driver('google')->stateless()->user();
    // dd($socialiteUser);

    $user = User::updateOrCreate([
        'email' => $socialiteUser->email,
    ], [
        'name' => $socialiteUser->name,
        'provider_id' => $socialiteUser->id,
        'provider' => 'google',
        'password' => $socialiteUser->token,
    ]);
 
    Auth::login($user);

    return redirect('/dashboard');

});

require __DIR__.'/auth.php';
