<!doctype html>
<html lang="ja">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <link href="{{ asset('css/grid.css') }}" rel="stylesheet">

    <title>MISORA-FIXED</title>
  </head>
  <body>
    <!-- Grid Container -->
    <div class='grid-container'>

      <!-- Grid Header -->
      <div class='grid-header'>
        @yield('header')
      </div>

      <!-- Grid Sidebar -->
      <div class='grid-sidebar'>
        @yield('sidebar')
      </div>

      <!-- Grid Main -->
      <div class='grid-main'>
        @yield('main')
      </div>

    </div>

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
  </body>
</html>

<!--
サイドバー参考サイト
https://coliss.com/articles/build-websites/operation/work/bootstrap-5-dashboard-tutorial.html
-->