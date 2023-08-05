# pystu
Python library for Studuino

■テスト<br />
１．setup.pyのバージョンを変更する<br />
　　ex) version='0.9.3',<br />
２．コマンドプロンプトなどでpystuディレクトに移動し、以下を実行<br />
    > python setup.py sdist bdist_wheel<br />
    > twine upload --repository-url https://test.pypi.org/legacy/ dist/*<br />
５．下記で登録したパッケージを確認できます。<br />
　　https://test.pypi.org/manage/projects/<br />

■PyPiへの登録方法<br />
１．setup.pyのバージョンを変更する<br />
　　ex) version='0.9.3',<br />
２．コマンドプロンプトなどでpystuディレクトに移動し、以下を実行<br />
    > python setup.py sdist bdist_wheel<br />
    > twine upload --repository pypi dist/*<br />
５．下記で登録したパッケージを確認できます。<br />
　　https://pypi.org/manage/projects/<br />
