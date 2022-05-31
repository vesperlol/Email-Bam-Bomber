import smtplib,os
from tkinter import *;from tkinter import messagebox;from pystyle import *
window = Tk()
window.title("Bam Bomber || vesper #0003 / #8757")
window.geometry("710x595")
window.maxsize(710, 595)
window.minsize(710, 595)
window.iconbitmap("assets/mylogo.ico")
window.config(background='#222222')
bg = PhotoImage(file='assets/background.png')
start = PhotoImage(file='assets/img0.png')
os.system("mode con cols=80 lines=40")
os.system("title " + "Bam Bomber Logs || vesper #0003 / #8757")
class Bam:
    def spam(self):
        count = 0
        for _ in range(int(self.amount.get())):
            try:
                self.SRV.sendmail(self.email.get(), self.dest.get(), self.MSG)
                count +=1
                print(f"{Col.white}[{Col.pink}+{Col.white}] {Col.green}Sent {Col.white}({Col.green}{count}{Col.white})")
            except:pass
        messagebox.showinfo("Bam Bomber || vesper #0003 / #8757","Process Finished.");Bam()
    def verify(self):
        yes = False
        while True:
            email1 = self.email.get()
            email2 = self.dest.get()
            password = self.password.get()
            subject = self.subject.get()
            msg = self.message.get()
            try:
                amount = int(self.amount.get())
                if amount > 0 and amount < 1000:
                    pass
                else:messagebox.showerror("Bam Bomber || vesper #0003 / #8757","Max amount is 1000 and minimum is 0.");break
            except:messagebox.showerror("Bam Bomber || vesper #0003 / #8757","Invalid Amount");break
            try:
                A = email1.split("@")[1].split(".")[0]
                B = email2.split("@")[1].split(".")[0]
                if A != B:messagebox.showerror("Bam Bomber || vesper #0003 / #8757","Servers not matching.");break
                if A and B == "gmail":self.server = "smtp.gmail.com"
                elif A and B == "yahoo":self.server = "smtp.mail.yahoo.com"
                elif A and B == "outlook":self.server = "smtp-mail.outlook.com"
                else:messagebox.showerror("Bam Bomber || vesper #0003 / #8757","Valid servers : gmail, yahoo, outlook");break
            except:messagebox.showerror("Bam Bomber || vesper #0003 / #8757","Invalid Email(s)");break
            if len(subject) > 1:pass
            else:messagebox.showerror("Bam Bomber || vesper #0003 / #8757","Invalid Subject");break
            if len(msg) > 1:pass
            else:messagebox.showerror("Bam Bomber || vesper #0003 / #8757","Invalid Message");break
            try:
                self.MSG = f"Subject: {subject}\n\n{msg}"
                self.SRV = smtplib.SMTP(self.server, 587)
                self.SRV.ehlo();self.SRV.starttls();self.SRV.ehlo()
                self.SRV.login(email1, password)
            except:messagebox.showerror("Bam Bomber || vesper #0003 / #8757",f"Couldn't Login to {email1}");break
            yes = True;break
        if yes:
            self.spam()
        else:pass
    def __init__(self):
        os.system('cls')
        A = f"{Col.pink}=";B = f"{Col.white}="
        print(f"""{Col.pink}
                                        ▄▄╥▄
                                   ▄█▓███▓▓██▀
                                  ▓██▌▓█▀▀▀▀▀
                                 █▓██▀
                                ██▓▓▌
                                ████▌
                                 ▓▓▓▓▓
                                  ▀████▄
                                    ▓▓▓█▓
                                     ▀████
                                       ▀▀▀░ 
                                     ▄▄▄▄▄▄  
                               ▄████████████████▄▄
                           ▄████████████████████████▄ 
                        ▄██████████████████████████████▄
                       ███████ ▓▓▓▓▓▓▓ ██████████████████▄
                     ▄█████ ▓▓▓▓▓▓▓▓▓▓▓▓ ██████████████████
                    ██████▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓ ████████████████ 
                   ██████▓▓▓▓▓▓▓▓▓▓▓▓█████▓▓▓███▓▓▓▓█████████
                  ▐██████▓▓▓▓▓▓▓▓▓▓▓▓████ ▓▓████▓▓▓▓██████████
                  █████████▓▓▓▓█████▓▓▓▓▓▓▓████▓▓▓████████████
                  ███████████▓▓█████▓▓██ ▓▓▓▓█ ▓▓█████ ▓▓ ████
                  ████████████▓▓▓▓▓▓█▓▓▓▓▓▓▓█ ▓▓███▓ ▓▓▓▓█████
                  ▐███████████████████▓▓▓███▓▓▓▓▓▓▓███████████
                   ████████████████████▓ ▓▓▓▓████████████████▌
                   ▐██████████▓▓▓▓▓▓▓▓███▓▓▓████████████████▌
                     ██████████▓▓▓██████▓▓▓████████████████▀
                      █████████████████ ▓▓████████████████▀
                       ▀████████████▓▓▓▓▓▓██████████████▀
                          ▀█████████▓▓████████████████▀
                             ▀████████████████████▀▀

{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}

{Col.white}[{Col.pink}+{Col.white}] {Col.white}Bam Bomber Logs..      
        """)
        bgg = Label(window, image=bg, borderwidth=0)
        bgg.place(x=0, y=0)
        self.email = Entry(window,font=('SeoulHangang',10),bg='#9B9B9B', fg='#D70038',width=32,borderwidth=0)
        self.email.place(x=88, y=220)
        self.password = Entry(window,font=('SeoulHangang',10),bg='#9B9B9B', fg='#D70038',width=35,show='*',borderwidth=0)
        self.password.place(x=389, y=220)
        self.subject = Entry(window,font=('SeoulHangang',10),bg='#9B9B9B', fg='#D70038',width=32,borderwidth=0)
        self.subject.place(x=88, y=299)
        self.message = Entry(window,font=('SeoulHangang',10),bg='#9B9B9B', fg='#D70038',width=35,borderwidth=0)
        self.message.place(x=389, y=299)
        self.amount = Entry(window,font=('SeoulHangang',10),bg='#9B9B9B', fg='#D70038',width=35,borderwidth=0)
        self.amount.place(x=389, y=383)
        self.dest = Entry(window,font=('SeoulHangang',10),bg='#9B9B9B', fg='#D70038',width=32,borderwidth=0)
        self.dest.place(x=88, y=383)
        startbu = Button(window, image=start,bg='#111111',borderwidth=0, activebackground="#111111",command=self.verify)
        startbu.place(x=254,y=471)
Bam()
window.mainloop()