import smtplib
from email.mime.text import MIMEText
from email.header import Header

class util_mail:

    def __init__(
            self,
            fromAddress,
            toAddress,
            loginID,
            loginPW,
            title,
            message):
        self.fromAddress = fromAddress
        self.toAddress = toAddress
        self.loginID = loginID
        self.loginPW = loginPW
        self.title = title
        self.message = message

    def do_mail(self):
        
        #日本語でメールを送信するために、メールの文字コードを変数jpに代入
        jp='iso-2022-jp'
        
        #Gメールを指定して、インスタンス化
        gm=smtplib.SMTP('smtp.gmail.com', 587)

        #ESMTPサーバーに身元を明かす
        gm.ehlo()

        #TLSモードで通信する
        gm.starttls()

        #ehlo()は、再度呼ばなければならない
        gm.ehlo()

        #送信に使うGメールアドレスとパスワードを指定し、SMTPサーバーに接続
        gm.login(self.loginID, self.loginPW)
        
        #MIMEメッセージオブジェクトを生成
        #引数１：エンコード済みの本文を指定
        #引数２：プレーンテキストメールを指定
        #引数３：文字コードを指定
        message=MIMEText(
            self.message.encode(jp),
            'plain',
            jp,
        )
        
        #ヘッダー情報を指定
        message['Subject']=str(Header(self.title, jp))

        #送信元のアドレスを指定
        message['From']=self.fromAddress

        #送信先のアドレスを指定
        message['To']=self.toAddress
        
        #sendmailメソッドでメールを送信
        gm.sendmail(
            self.fromAddress,
            [self.toAddress],
            message.as_string(),
        )
        
        #SMTPサーバーから切断
        gm.close()

