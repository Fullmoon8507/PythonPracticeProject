from util_mail import util_mail

if __name__ == "__main__":
    utilMail = util_mail(
            "fullmoon8507@gmail.com",
            "fullmoon_8507@yahoo.co.jp",
            "fullmoon8507@gmail.com",
            "rg020316",
            "こんにちはPython",
            "このメールはPythonで送信しています。");
            
    utilMail.do_mail()
