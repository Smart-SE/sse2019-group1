# botの開発準備

## botから呼び出す親functionは下記に従ってlambda_function.pyに書いてください
## `lambda_function`から別の`lambda_function`を呼び出す場合はboto3で呼び出す必要あり。
## とりあえずの子functionはlibrary的にディレクトリ切って作ると良いです。

1. `git pull origin master`して最新化し、`git checkout -b "branch名"`でbranchを切る。
1. 右側のAWS Resourcesからcreate lambdaする
1. smartse-team-1の直下に作成されたら、sse2019-group1/Bot/src下にディレクトリを移動する
1. Terminalで上記のディレクトリにcdし、 `pip-3.6 install -t line-bot-sdk`を実行する
1. `.gitignore`をrepeatYourWordのファイルを参考に修正する
1. gitをcommitして、remoteにpushする
1. repeatYourWordの`lambda_function.py`の中身を、自分の`lambda_function.py`にコピーする
1. `ここに実装`の部分に処理を追記する
 