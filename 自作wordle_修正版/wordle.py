import random

ck='''アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホ
マミムメモヤユヨラリルレロワヲンガギグゲゴザジズゼゾダヂヅデドパピプペポ
バビブベボャュョッーェィォZ2２♂♀'''

words = '''
フシギダネ	フシギソウ	フシギバナ
リザードン	カメックス	キャタピー
トランセル	バタフリー	ピジョット
オニスズメ	オニドリル	アーボック
ピカチュウ	ライチュウ	サンドパン
ニドラン♂	ニドラン♀	ニドリーナ
ニドクイン	ニドリーノ	ニドキング
キュウコン	ゴルバット	ナゾノクサ
クサイハナ	ラフレシア	パラセクト
モルフォン	ダグトリオ	ペルシアン
ゴルダック	オコリザル	ウインディ
ニョロボン	ユンゲラー	フーディン
ワンリキー	ゴーリキー	カイリキー
マダツボミ	ウツボット	メノクラゲ
ドククラゲ	イシツブテ	ゴローニャ
ギャロップ	レアコイル	ベトベター
ドードリオ	ベトベトン	シェルダー
パルシェン	スリーパー	キングラー
ビリリダマ	マルマイン	サワムラー
エビワラー	ベロリンガ	マタドガス
サイホーン	モンジャラ	トサキント
アズマオウ	ヒトデマン	スターミー
バリヤード	ストライク	ルージュラ
ケンタロス	コイキング	ギャラドス
シャワーズ	サンダース	ブースター
オムナイト	オムスター	カブトプス
フリーザー	ファイヤー	ミニリュウ
ハクリュー	カイリュー	ミュウツー
チコリータ	ベイリーフ	メガニウム
ヒノアラシ	マグマラシ	バクフーン
アリゲイツ	オーダイル	ヨルノズク
レディアン	アリアドス	クロバット
チョンチー	ランターン	トゲチック
ネイティオ	デンリュウ	キレイハナ
ニョロトノ	ヒマナッツ	ヤンヤンマ
ヤミカラス	ヤドキング	アンノーン
ソーナンス	キリンリキ	クヌギダマ
フォレトス	ハガネール	グランブル
ハリーセン	ヘラクロス	マグマッグ
マグカルゴ	デリバード	マンタイン
エアームド	キングドラ	ドンファン
カポエラー	ムチュール	エレキッド
ミルタンク	ヨーギラス	サナギラス
バンギラス	テッポウオ	ブラッキー
ウソッキー	ポリゴン２	グライガー
ジュプトル	ジュカイン	ワカシャモ
バシャーモ	ミズゴロウ	ヌマクロー
ラグラージ	ジグザグマ	マッスグマ
カラサリス	アゲハント	ドクケイル
ハスブレロ	ルンパッパ	オオスバメ
ペリッパー	サーナイト	アメモース
キノガッサ	ヤルキモノ	ケッキング
テッカニン	ゴニョニョ	バクオング
マクノシタ	ハリテヤマ	エネコロロ
ボスゴドラ	チャーレム	ライボルト
バルビート	イルミーゼ	マルノーム
サメハダー	ホエルオー	ブーピッグ
パッチール	ビブラーバ	ナックラー
フライゴン	チルタリス	ザングース
ハブネーク	ルナトーン	ソルロック
ドジョッチ	シザリガー	ネンドール
ユレイドル	アーマルド	ミロカロス
カクレオン	カゲボウズ	ジュペッタ
サマヨール	トロピウス	ユキワラシ
オニゴーリ	タマザラシ	トドグラー
トドゼルガ	ハンテール	サクラビス
ジーランス	ボーマンダ	メタグロス
レジロック	レジアイス	レジスチル
ラティアス	ラティオス	カイオーガ
グラードン	レックウザ	デオキシス
ダーテング
ハヤシガメ	ドダイトス	モウカザル
ゴウカザル	ポッチャマ	エンペルト
ムクバード	ムクホーク	コロボーシ
コロトック	レントラー	ロズレイド
ズガイドス	ラムパルド	タテトプス
トリデプス	ミノムッチ	ミノマダム
ガーメイル	ミツハニー	ビークイン
フローゼル	チェリンボ	カラナクシ
トリトドン	エテボース	フワライド
ミミロップ	ムウマージ	ドンカラス
ニャルマー	ブニャット	リーシャン
スカンプー	スカタンク	ドーミラー
ドータクン	ガブリアス	ヒポポタス
カバルドン	ドラピオン	グレッグル
ドクロッグ	マスキッパ	ケイコウオ
ネオラント	ユキカブリ	ユキノオー
マニューラ	ジバコイル	べロベルト
ドサイドン	モジャンボ	エレキブル
ブーバーン	トゲキッス	メガヤンマ
リーフィア	グレイシア	グライオン
エルレイド	ダイノーズ	ヨノワール
ユキメノコ	エムリット	ディアルガ
ヒードラン	レジギガス	ギラティナ
クレセリア	ダークライ	アルセウス
ポリゴンZ	    ポッタイシ
'''.split()





#ランダムでリストを抽出する関数

def getRandomWord(wordlist):

    Index=random.randint(0,len(words)-1)
    return wordlist[Index]

#画面上に状況を表示する関数

def display(guess,secretword):
    print()

    for i in range(len(al_list)):#リストの要素を一行ずつ表示する関数
        for a in range(len(al_list[i])):
            print(al_list[i][a],end=' ')
        print()



    blank= '_' * len(secretword)

    if len(guess) == 5:
        for i in range(len(secretword)):
            if guess[i] == secretword[i]:
                blank = blank[:i] + secretword[i] + blank[i+1:]

    for i in range(len(blank)):
        if blank[i] != '_':
            stack[i]=blank[i]
    answer=stack

    print()
    print('name:',end=' ')
    for letter in answer:
        print(letter,end=' ')
    print()



#文字を記入する、文字列、カタカナ以外の記入、既出文字の排他処理

def getinput(alreadyGuessed):
    print()
    print('入力回数:{}'.format(guess_count))
    print('ポケモン名を記入してください')

    al_guess=alreadyGuessed.split()

    while True:
        print('入力:',end=' ')
        guess=input()
        flag=0

        for i in range(len(guess)):
            if guess[i] not in ck:
                flag = i
        if len(guess) != 5:
            print('5文字のポケモンを入力してください')
        elif guess not in words:
            print('ポケモン名ではありません')
        elif guess in al_guess:
            print('既にその文字を入力済みです')
        elif flag != 0:
            print('カタカナではありません')
        else:
            return guess

#ゲームコンティニュー関数
def playAgain():
    #startswitchでtrue,falseを判断
    print('もう一度プレイしますか？(y or n)')
    return input().lower().startswith('y')




#初期変数の代入
print('Pokemon_wordle')
print('入力数は10回までです')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
secret_ck=list(secretWord)
gameIsDone = False
guess=''
#print(secretWord)
al_list= ((('_' * 5)+' ')*10).split() #index9
guess_count=0
guess_al=''
answer=''
stack = '_ _ _ _ _'.split()

#whileによるゲームループ

while True:
    display(guess,secretWord)

    guess = getinput(missedLetters)
    guess_al=guess
    ins=0


    if guess == secretWord:
        gameIsDone = True
        print('you win')
    else:
        missedLetters= missedLetters + ' ' + guess



    for i in range(len(guess)):  # 文字列一致の代入
        if guess[i] in secret_ck:
            guess_al = guess_al[:ins] + '[' + guess_al[ins:ins + 1] + ']' + guess_al[ins + 1:]
            ins= ins + 3
        else:
            guess_al = guess_al[:ins] + ' ' + guess_al[ins:ins + 1] + ' ' + guess_al[ins + 1:]
            ins = ins + 3
    al_list[guess_count]=guess_al

    guess_count = guess_count + 1

    if guess_count == len(al_list):
        display(guess, secretWord)
        gameIsDone = True
        print('あなたの負けです。',end='　')
        print('答えは'+ secretWord+ 'です')



#ゲームの初期化

    if gameIsDone:
        if playAgain():
            missedLetters=''
            correctLetters=''
            gameIsDone=False
            secretWord=getRandomWord(words)
            print('Pokemon')
            secret_ck = list(secretWord)
            guess = ''
            #print(secretWord)
            al_list = ((('_' * 5) + ' ') * 10).split()  # index9
            guess_count = 0
            guess_al = ''
            answer = ''
            stack = '_ _ _ _ _'.split()
        else:
            break