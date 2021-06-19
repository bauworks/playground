■ 初回は node_modules ができていないので、docker-compose.yaml の command が失敗するので一旦コメントアウトする。

   ＃ command: sh -c "cd reactapp && yarn start"


■ Docker起動後、コンテナに入って yarn install

  docker exec -it reactapp /bin/sh
  cd reactapp
  yarn install

■ コンテナを停止して、docker-compose.yaml を元に戻す。
  docker-compose stop

■ コンテナを起動して動作確認
  docker-compose up -d
