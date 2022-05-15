import requests


TOKEN = "Line 權杖"


class LineNotify:

    def __init__(self, token):
        self.__TOKEN = token
        self.__LINE_NOTIFY_URL = "https://notify-api.line.me/api/notify"


    def _getHeader(self):
        # HTTP 1.1 TLS下去定義的 Token
        # 傳輸層安全性協定（英語：Transport Layer Security，縮寫：TLS）
        # TSL 是更新、更安全的 SSL 版本。
        header = {
            "Authorization": f"Bearer {self.__TOKEN}",
            # "Content-Type" : "application/x-www-form-urlencoded" # 可省略
        }
        return header

    # 傳訊息
    def postMessage(self, message:str) -> int:
        message = {"message": message}
        rep = requests.post(
            self.__LINE_NOTIFY_URL,
            params = message,
            headers = self._getHeader()
        )
        return rep.status_code

    # 傳照片
    def postMessageAndWebImage(self, message:str, imageUrl:str) -> int:
        message = {"message": message}
        files = {"imageFile": open(imageUrl, "rb")}
        rep = requests.post(
            self.__LINE_NOTIFY_URL,
            params = message,
            headers = self._getHeader(),
            files = files
        )
        return rep.status_code

    # 傳貼圖
    def postMessageAndStickerThumbnail(self, message:str, stickerPackageId:int, stickerId:int) -> int:
        message = {
            'message': message,
            'stickerPackageId': stickerPackageId,
            'stickerId': stickerId,
        }
        rep = requests.post(
            self.__LINE_NOTIFY_URL,
            params = message,
            headers = self._getHeader(),
        )
        return rep.status_code


if __name__ == "__main__":
    service = LineNotify(TOKEN)
    # result = service.postMessage("Hello Line Notify in Python")
    # result = service.postMessageAndWebImage("Hello Line Notify in Python", "./憤怒鳥.jpg") # 只能 jpg png
    result = service.postMessageAndStickerThumbnail("Hello Line Notify in Python", 1, 113)
    print(result)
