@extends('layouts.test-app')
@include('layouts.test-header')
@include('layouts.test-sidebar')

@section('main')
<main class="col-md-9 ml-sm-auto col-lg-10 px-md-4 py-4">
    <nav aria-label="breadcrumb">
        <ol class="breadcrumb">
        <li class="breadcrumb-item"><a href="#">Home</a></li>
        <li class="breadcrumb-item active" aria-current="page">Overview</li>
        </ol>
    </nav>
    <h1 class="h2">Dashboard</h1>
    <p>This is the homepage of a simple admin interface which is part of a tutorial written on Themesberg</p>
</main>
@endsection
