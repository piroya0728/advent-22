import cv2

# 画像ファイルを入力します
src = cv2.imread(input())

# 分類器の設定ファイルのパスを指定して、それをもとに分類器を作成します
face_cascade = cv2.CascadeClassifier('\\Users\\hi-pi\\Downloads\\opencv-master\\opencv-master\\data\\haarcascades\\haarcascade_frontalface_default.xml')

# 分類器はグレースケールの画像を要求するので、グレーに変換してあげます
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 分類器に通し、検出した各顔の位置と大きさを表す二次元配列を返します
faces = face_cascade.detectMultiScale(src_gray)

# 戻り値の情報をもとに、画像の中の顔を一つずつ□で囲んであげます
for x, y, w, h in faces:
    cv2.rectangle(src, (x, y), (x + w, y + h), (255, 0, 0), 2)

# 画像を表示します
cv2.imshow('img', src)
cv2.waitKey(0)
