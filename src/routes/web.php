<?php

use Illuminate\Support\Facades\Route;
use Inertia\Inertia;
use \App\Models\Website;
use \App\Http\Controllers\ScanningController;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/

Route::get('/', function () {
    return Inertia::render('Home');
});

Route::get('/scanned', function () {
    return Inertia::render('Scanned', [
        'websites' => Website::all()->map(fn($website) => [
            'id' => $website->id,
            'title' => $website->title,
            'url' => $website->url,
            'screen_path' => $website->screen_path,
        ])
    ]);
});


Route::get('/scanning', function () {
    return Inertia::render('Scanning');
});

Route::post('/scanning', [ScanningController::class, 'handleForm']);
