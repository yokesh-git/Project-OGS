from tkinter import *
import tkinter.ttk as ttk
from tkinter import font
from Package import Login
from Package import CreateUser
from Package import View_Data
import requests.exceptions
import tkinter.messagebox
from Package import Validate_Admin
import multiprocessing

global category

class Admin:

    def __init__(self,master):


        global w,h,ws,hs,x,y

        w = 1000
        h = 650
        ws = root.winfo_screenwidth() # width of the screen
        hs = root.winfo_screenheight() # height of the screen
        x = (ws/4) - (w/4)
        y = (hs/4) - (h/4)
        
        self.master = master
        master.title("OGS - Admin")

        def onclick():
            root.quit()
            self.master.withdraw()

        self.master.protocol("WM_DELETE_WINDOW", onclick)

        self.canvas = Canvas(self.master, width=1000, height=650,bg = 'black')
        self.canvas.pack()

        self.heading = Label(self.canvas, text="OGS Admin Login", font=('arial 40 bold'),
            fg = 'white',bg = 'black')
        self.heading.place(x=300, y=100)

        self.cc = Label(self.canvas, text="College Code", font=('arial 20 italic'), fg='white', 
            bg='black')
        self.cc.place(x=250, y=250)

        self.name = Label(self.canvas, text="User ID", font=('arial 20 italic'), fg='white', 
            bg='black')
        self.name.place(x=300, y=300)

        self.password = Label(self.canvas, text="Password", font=('arial 20 italic'), fg='white', 
            bg='black')
        self.password.place(x=300, y=350)

        self.college_code = Entry(root,font = "Times 20")
        self.college_code.place(x=450,y=250)
        
        self.user = Entry(root,font = "Times 20")
        self.user.place(x=450,y=300)

        self.password = Entry(root, show='*',font = "Times 20")
        self.password.place(x=450, y=350)

        self.button1 = Button(self.canvas, text="Login", foreground="white", command=self.login,
                              anchor=CENTER)

        self.button1.configure(width=30, activebackground="#33B5E5", bg='blue', relief=FLAT)
        self.button1_window = self.canvas.create_window(500, 500, anchor=W, window=self.button1)
        font1 = font.Font(family='Times New Roman', size=20, weight='normal')
        self.button1['font'] = font1
        self.button1.config(width=10, height=1)


        #-------------------------------------------------------------------------------------#


        self.FrontPage = Toplevel()

        self.FrontPage.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.canvas2 = Canvas(self.FrontPage, width=1000, height=650, bg = 'black')
        self.canvas2.pack()

        self.AuthButton = Button(self.canvas2, text="Authentication", foreground="white",
            command=self.authButton,anchor=CENTER)

        self.AuthButton.configure(width=30, activebackground="#33B5E5", bg='blue', relief=FLAT)
        self.AuthButton_window = self.canvas2.create_window(100, 300, anchor=W, window=self.AuthButton)
        font1 = font.Font(family='Times New Roman', size=20, weight='normal')
        self.AuthButton['font'] = font1
        self.AuthButton.config(width=20, height=1)

        self.ReadButton = Button(self.canvas2, text="Read Complaints", foreground="white",
            command=self.readButton,anchor=CENTER)
        self.ReadButton.configure(width=30, activebackground="#33B5E5", bg='blue', relief=FLAT)
        self.ReadButton_window = self.canvas2.create_window(500, 300, anchor=W, window=self.ReadButton)
        font1 = font.Font(family='Times New Roman', size=20, weight='normal')
        self.ReadButton['font'] = font1
        self.ReadButton.config(width=25, height=1)

        self.front_back = Button(self.canvas2, text="BACK", foreground="white",
            command=self.frontpage_back,anchor=CENTER)
        self.front_back.configure(activebackground="#33B5E5", bg='red', relief=FLAT)
        self.front_back_window = self.canvas2.create_window(50, 60, anchor=W, window=self.front_back)
        font1 = font.Font(family='Times New Roman', size=15, weight='normal')
        self.front_back['font'] = font1
        self.front_back.config(width=10, height=1)

        self.FrontPage.protocol("WM_DELETE_WINDOW", root.destroy)

        self.FrontPage.withdraw()

        #-------------------------------------------------------------------------------------------#


        #Auth Page

        self.AuthPage = Toplevel()

        self.AuthPage.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.canvas3 = Canvas(self.AuthPage, width=1000, height=650,bg = 'black')
        self.canvas3.pack()

        self.auth_back = Button(self.canvas3, text="BACK", foreground="white",
            command=self.authpage_back,anchor=CENTER)
        self.auth_back.configure(activebackground="#33B5E5", bg='red', relief=FLAT)
        self.auth_back_window = self.canvas3.create_window(50, 50, anchor=W, window=self.auth_back)
        font1 = font.Font(family='Times New Roman', size=15, weight='normal')
        self.auth_back['font'] = font1
        self.auth_back.config(width=10, height=1)

        self.heading = Label(self.AuthPage, text="OGS Authentication", 
            font=('arial 30 bold'),fg = 'white',bg = 'black')
        self.heading.place(x=250, y=20)

        #--------Student Canvas-----------------------------------#

        self.stucanvas = Canvas(self.canvas3, width=450, height=550,
            bg ='#558DEA',highlightbackground = 'white')
        self.stucanvas.place(x=20,y=75)

        self.stu_heading = Label(self.stucanvas, text="Auth-Student", 
            font=('arial 15 bold'),fg = 'black',bg = '#558DEA')
        self.stu_heading.place(x=150, y=20)

        self.stu_dept = Label(self.stucanvas, text="Department", 
            font=('arial 20 bold'),fg = 'black',bg = '#558DEA')
        self.stu_dept.place(x=20, y=100)

        self.dept_choices ={'CSE','IT','ECE','EEE','Civil'}
        self.tkvar = StringVar(root)
        self.tkvar.set('Please Select')
        self.popupMenu = OptionMenu(self.stucanvas,self.tkvar, *self.dept_choices,
            command = self.stu_deptButton)
        self.popupMenu.configure(activebackground = "white",bg='black', relief = FLAT)
        self.popupMenu_window = self.stucanvas.create_window(240, 100, anchor=NW, window=self.popupMenu)
        self.popupMenu.config(width = 12, height = 1,foreground='white',highlightbackground = 'black',
            font = ('arial 15'))

        self.stu_year = Label(self.stucanvas, text="Year", 
            font=('arial 20 bold'),fg = 'black',bg = '#558DEA')
        self.stu_year.place(x=20, y=175)

        self.year_choices ={'I','II','III','IV'}
        self.year_tkvar = StringVar(root)
        self.year_tkvar.set('Please Select')
        self.popupMenu = OptionMenu(self.stucanvas,self.year_tkvar, *self.year_choices)
        self.popupMenu.configure(activebackground = "white",bg='black', relief = FLAT)
        self.popupMenu_window = self.stucanvas.create_window(240, 175, anchor=NW, window=self.popupMenu)
        self.popupMenu.config(width = 12, height = 1,foreground='white',highlightbackground = 'black',
            font = ('arial 15'))

        self.year_of_joining = Label(self.stucanvas, text="Year of Joining", 
            font=('arial 20 bold'),fg = 'black',bg = '#558DEA')
        self.year_of_joining.place(x=20, y=250)

        self.yoj = Entry(self.stucanvas,font = "Times 20")
        self.yoj.place(x=240,y=250,width = 80)

        self.stu_domain = Label(self.stucanvas, text="College\t       @", 
            font=('arial 20 bold'),fg = 'black',bg = '#558DEA')
        self.stu_domain.place(x=20, y=325)

        self.stu_domain = Entry(self.stucanvas,font = "Times 20")
        self.stu_domain.place(x=240,y=325,width = 160)

        self.num_of_stu = Label(self.stucanvas, text="No of Stu", 
            font=('arial 20 bold'),fg = 'black',bg = '#558DEA')
        self.num_of_stu.place(x=20, y=400)

        self.num_of_stu = Entry(self.stucanvas,font = "Times 20")
        self.num_of_stu.place(x=240,y=400,width = 160)


        self.StuAuth = Button(self.stucanvas, text="Authenticate", foreground="white", command=self.stuAuth,
                              anchor=CENTER)
        self.StuAuth.configure(activebackground="#33B5E5", bg='black', relief=FLAT)
        self.StuAuth_window = self.stucanvas.create_window(150, 500, anchor=W, window=self.StuAuth)
        font1 = font.Font(family='Times New Roman', size=20, weight='normal')
        self.StuAuth['font'] = font1
        self.StuAuth.config(width=10, height=1)


        #--------------Teacher Canvas-------------------#

        self.teacanvas = Canvas(self.canvas3, width=450, height=550,
            bg ='white',highlightbackground = '#558DEA')
        self.teacanvas.place(x=510,y=75)

        self.tea_heading = Label(self.teacanvas, text="Auth-Teacher", 
            font=('arial 15 bold'),fg = 'black',bg = 'white')
        self.tea_heading.place(x=150, y=20)


        self.tea_dept = Label(self.teacanvas, text="Department", 
            font=('arial 20 bold'),fg = 'black',bg = 'white')
        self.tea_dept.place(x=20, y=175)


        self.dept_choices ={'CSE','IT','ECE','EEE','Civil'}
        self.staff_tkvar = StringVar(root)
        self.staff_tkvar.set('Please Select')
        self.popupMenu = OptionMenu(self.teacanvas,self.staff_tkvar, *self.dept_choices,
            command = self.tea_deptButton)
        self.popupMenu.configure(activebackground = "white",bg='black', relief = FLAT)
        self.popupMenu_window = self.teacanvas.create_window(200, 175, anchor=NW, window=self.popupMenu)
        self.popupMenu.config(width = 15, height = 1,foreground='white',highlightbackground = 'black',
            font = ('arial 15'))

        self.num_of_staff = Label(self.teacanvas, text="No of Staff", 
            font=('arial 20 bold'),fg = 'black',bg = 'white')
        self.num_of_staff.place(x=20, y=250)

        self.num_of_staff = Entry(self.teacanvas,font = "Times 20")
        self.num_of_staff.place(x=200,y=250,width = 160)

        self.tea_domain = Label(self.teacanvas, text="College\t  @", 
            font=('arial 20 bold'),fg = 'black',bg = 'white')
        self.tea_domain.place(x=20, y=325)

        self.tea_domain = Entry(self.teacanvas,font = "Times 20")
        self.tea_domain.place(x=200,y=325,width = 160)

        self.TeaAuth = Button(self.teacanvas, text="Authenticate", foreground="white",
            command=self.teaAuth, anchor=CENTER)
        self.TeaAuth.configure(width=30, activebackground="#33B5E5", bg='black', relief=FLAT)
        self.TeaAuth_window = self.teacanvas.create_window(150, 500, anchor=W, window=self.TeaAuth)
        font1 = font.Font(family='Times New Roman', size=20, weight='normal')
        self.TeaAuth['font'] = font1
        self.TeaAuth.config(width=10, height=1)

        self.AuthPage.protocol("WM_DELETE_WINDOW", root.destroy)

        self.AuthPage.withdraw()

        #-------------Read Page----------------------------------------#


        self.ReadPage = Toplevel()

        self.ReadPage.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.canvas4 = Canvas(self.ReadPage, width=1000, height=650,bg = 'black')
        self.canvas4.pack()

        self.read_back = Button(self.canvas4, text="BACK", foreground="white",
            command=self.readpage_back,anchor=CENTER)
        self.read_back.configure(activebackground="#33B5E5", bg='red', relief=FLAT)
        self.read_back_window = self.canvas4.create_window(50, 50, anchor=W, window=self.read_back)
        font1 = font.Font(family='Times New Roman', size=15, weight='normal')
        self.read_back['font'] = font1
        self.read_back.config(width=10, height=1)

        #-----------Student Buttons--------------#

        self.leftcanvas = Canvas(self.ReadPage, width = 300, height = 550,
            bg = "white", highlightbackground = "blue", border = 2)
        self.leftcanvas.place(x=20, y=75)

        self.bystu = Label(self.leftcanvas, text="By Student--", 
            font=('arial 15 bold'),fg = 'black',bg = 'white')
        self.bystu.place(x=20, y=20)


        self.stu_onins = Button(self.leftcanvas, text="On Institution", foreground="white",
            command=self.stu_OnInstitution, anchor=CENTER)
        self.stu_onins.configure(width=30, activebackground="#33B5E5", bg='#558DEA', relief=FLAT)
        self.stu_onins_window = self.leftcanvas.create_window(40, 80, anchor=W, window=self.stu_onins)
        font1 = font.Font(family='Times New Roman', size=20, weight='normal')
        self.stu_onins['font'] = font1
        self.stu_onins.config(width=11, height=1)

        self.stu_ontea = Button(self.leftcanvas, text="On Teacher", foreground="white",
            command=self.stu_OnTeacher, anchor=CENTER)
        self.stu_ontea.configure(width=30, activebackground="#33B5E5", bg='#558DEA', relief=FLAT)
        self.stu_ontea_window = self.leftcanvas.create_window(40, 140, anchor=W, window=self.stu_ontea)
        font1 = font.Font(family='Times New Roman', size=20, weight='normal')
        self.stu_ontea['font'] = font1
        self.stu_ontea.config(width=11, height=1)

        self.stu_onother = Button(self.leftcanvas, text="On Other", foreground="white",
            command=self.stu_OnOther, anchor=CENTER)
        self.stu_onother.configure(width=30, activebackground="#33B5E5", bg='#558DEA', relief=FLAT)
        self.stu_onother_window = self.leftcanvas.create_window(40, 200, anchor=W, window=self.stu_onother)
        font1 = font.Font(family='Times New Roman', size=20, weight='normal')
        self.stu_onother['font'] = font1
        self.stu_onother.config(width=11, height=1)

        #--------Teacher Buttons--------------#


        self.bytea = Label(self.leftcanvas, text="By Teacher--", 
            font=('arial 15 bold'),fg = 'black',bg = 'white')
        self.bytea.place(x=20, y=300)


        self.tea_onins = Button(self.leftcanvas, text="On Institution", foreground="white",
            command=self.tea_OnInstitution, anchor=CENTER)
        self.tea_onins.configure(width=30, activebackground="#33B5E5", bg='#558DEA', relief=FLAT)
        self.tea_onins_window = self.leftcanvas.create_window(40, 360, anchor=W, window=self.tea_onins)
        font1 = font.Font(family='Times New Roman', size=20, weight='normal')
        self.tea_onins['font'] = font1
        self.tea_onins.config(width=11, height=1)

        self.tea_onstu = Button(self.leftcanvas, text="On Student", foreground="white",
            command=self.tea_OnStudent, anchor=CENTER)
        self.tea_onstu.configure(width=30, activebackground="#33B5E5", bg='#558DEA', relief=FLAT)
        self.tea_onstu_window = self.leftcanvas.create_window(40, 420, anchor=W, window=self.tea_onstu)
        font1 = font.Font(family='Times New Roman', size=20, weight='normal')
        self.tea_onstu['font'] = font1
        self.tea_onstu.config(width=11, height=1)

        self.tea_onother = Button(self.leftcanvas, text="On Other", foreground="white",
            command=self.tea_OnOther, anchor=CENTER)
        self.tea_onother.configure(width=30, activebackground="#33B5E5", bg='#558DEA', relief=FLAT)
        self.tea_onother_window = self.leftcanvas.create_window(40, 480, anchor=W, window=self.tea_onother)
        font1 = font.Font(family='Times New Roman', size=20, weight='normal')
        self.tea_onother['font'] = font1
        self.tea_onother.config(width=11, height=1)

        self.rightcanvas = Canvas(self.ReadPage, width = 600, height = 550,
            bg = "black", highlightbackground = "blue", border = 2)
        self.rightcanvas.place(x=380, y=75)

        self.scrollb = ttk.Scrollbar(self.rightcanvas)

        self.displaybox = Text(self.rightcanvas, width = 60 , height = 28)
        self.displaybox.pack()
        self.displaybox.focus_set()
        self.scrollb.pack(side = RIGHT, fill = Y)
        self.displaybox.pack(side = LEFT, fill = Y)
        self.scrollb.config(command = self.displaybox.yview)
        self.displaybox.config(yscrollcommand = self.scrollb.set,font=("consolas", 12),
            borderwidth=3, relief="sunken",state = DISABLED)

        self.ReadPage.protocol("WM_DELETE_WINDOW", root.destroy)

        self.ReadPage.withdraw()


    def frontpage_back(self):
        self.FrontPage.withdraw()
        self.user.delete(0,END)
        self.password.delete(0,END)
        self.college_code.delete(0,END)
        self.master.deiconify()
    def authpage_back(self):
        self.AuthPage.withdraw()
        self.yoj.delete(0,END)
        self.stu_domain.delete(0,END)
        self.num_of_stu.delete(0,END)
        self.tea_domain.delete(0,END)
        self.num_of_staff.delete(0,END)
        self.tkvar.set('Please Select')
        self.year_tkvar.set('Please Select')
        self.staff_tkvar.set('Please Select')
        self.FrontPage.deiconify()
    def readpage_back(self):
        self.ReadPage.withdraw()
        self.displaybox.config(state = NORMAL)
        self.displaybox.delete('1.0',END)
        self.displaybox.config(state = DISABLED)
        self.FrontPage.deiconify()

    def login(self):
        print("Done")

        global college_code
        email = self.user.get()
        password = self.password.get()
        college_code = self.college_code.get()

        if len(college_code) == 4:

            try:
                Admin = Validate_Admin.ValidateAdmin(college_code,email)


                if Admin == 0 or Admin == "KeyError":
                    tkinter.messagebox.showinfo("Access Denied!","Please Enter correct OGS id and College Code")
                    
                else:
                    Login.Login(email,password)

                    self.master.withdraw()
                    self.FrontPage.deiconify()
                    
            except requests.exceptions.HTTPError as e:
                response = e.args[0].response
                error = response.json()['error']
                print(response)
                print(error)
                tkinter.messagebox.showinfo("Error!","Please Check OGS ID and Password")
        else:
            tkinter.messagebox.showinfo("Info", "College Code must be of length 4")

    def authButton(self):
        print("Done")

        self.FrontPage.withdraw()
        self.AuthPage.deiconify()

    def readButton(self):
        print("Done")

        self.ReadPage.deiconify()
        self.FrontPage.withdraw()

    def stu_deptButton(self,svalue):
        print (svalue)

        global student_dept

        if svalue == 'CSE':
            student_dept = 'cs'
        if svalue == 'IT':
            student_dept = 'it'
        if svalue == 'ECE':
            student_dept = 'ec'
        if svalue == 'EEE':
            student_dept = 'ee'
        if svalue == 'Civil':
            student_dept = 'cv'


    def tea_deptButton(self,tvalue):

        global teacher_dept

        if tvalue == 'CSE':
            teacher_dept = 'cs'
        if tvalue == 'IT':
            teacher_dept = 'it'
        if tvalue == 'ECE':
            teacher_dept = 'ec'
        if tvalue == 'EEE':
            teacher_dept = 'ee'
        if tvalue == 'Civil':
            teacher_dept = 'cv'

    def stuAuth(self):
        print("Done")

        year_of_joining = self.yoj.get()
        domain = self.stu_domain.get()
        student_domain = '@' + domain
        student_count = self.num_of_stu.get()

        try:

            if len(year_of_joining) == 4 and student_domain.find('.') != -1:
                #print(student_count)

                CreateUser.CreateUser_Student(year_of_joining,student_dept,student_count,student_domain)
                CreateUser.StudentContent(year_of_joining,student_dept,student_count,student_domain,college_code)
                tkinter.messagebox.showinfo("Info","Authenticated Successfully")
            else:
                tkinter.messagebox.showinfo("Info","Check Year or Domain\nDomain must contain .(dot)")
        except NameError:
            tkinter.messagebox.showinfo("Info","Please Fill all fields")
        except Exception:
            tkinter.messagebox.showinfo("Info","Please Fill all fields")

    def teaAuth(self):
        print("Done")

        domain = self.tea_domain.get()
        teacher_domain = '@' + domain
        teacher_count = self.num_of_staff.get()

        try:

            if teacher_domain.find('.') != -1:
                CreateUser.CreateUser_Teacher(teacher_dept,teacher_domain,teacher_count)
                CreateUser.TeacherContent(teacher_dept,teacher_domain,teacher_count,college_code)
                tkinter.messagebox.showinfo("Info","Authenticated Successfully")
            else:
                tkinter.messagebox.showinfo("Info","Check Domain\nDomain must contain .(dot)")
        except NameError:
            tkinter.messagebox.showinfo("Info","Please Fill all fields")
        except Exception:
            tkinter.messagebox.showinfo("Info","Please Fill all fields")

    def stu_OnInstitution(self):

        self.displaybox.config(state=NORMAL)
        self.displaybox.delete('1.0',END)
        category = 'On institution'
        #college_code = self.college_code.get()
        #print(college_code)

        stu_ins_complaint = View_Data.Student(category,college_code)

        for i in range(len(stu_ins_complaint)):
            
            if stu_ins_complaint.index(stu_ins_complaint[i])%2 == 0:
                self.displaybox.insert(END,stu_ins_complaint[i]+'\n')
                continue
            self.displaybox.insert(END,'\t'+stu_ins_complaint[i]+'\n\n')
        self.displaybox.config(state=DISABLED)

    def stu_OnTeacher(self):

        self.displaybox.config(state=NORMAL)
        self.displaybox.delete('1.0',END)
        category = 'On Teachers'
        #college_code = self.college_code.get()
        stu_tea_complaint = View_Data.Student(category,college_code)

        for i in range(len(stu_tea_complaint)):
            
            if stu_tea_complaint.index(stu_tea_complaint[i])%2 == 0:
                self.displaybox.insert(END,stu_tea_complaint[i]+'\n')
                continue
            self.displaybox.insert(END,'\t'+stu_tea_complaint[i]+'\n\n')
        self.displaybox.config(state=DISABLED)


    def stu_OnOther(self):

        self.displaybox.config(state=NORMAL)
        self.displaybox.delete('1.0',END)

        category = 'Others'
       #college_code = self.college_code.get()
        stu_other_complaint = View_Data.Student(category,college_code)

        for i in range(len(stu_other_complaint)):
            
            if stu_other_complaint.index(stu_other_complaint[i])%2 == 0:
                self.displaybox.insert(END,stu_other_complaint[i]+'\n')
                continue
            self.displaybox.insert(END,'\t'+stu_other_complaint[i]+'\n\n')
        self.displaybox.config(state=DISABLED)


    def tea_OnInstitution(self):

        self.displaybox.config(state=NORMAL)
        self.displaybox.delete('1.0',END)
        category = 'On institution'
        #college_code = self.college_code.get()
        tea_ins_complaint = View_Data.Teacher(category,college_code)

        for i in range(len(tea_ins_complaint)):
            
            if tea_ins_complaint.index(tea_ins_complaint[i])%2 == 0:
                self.displaybox.insert(END,tea_ins_complaint[i]+'\n')
                continue
            self.displaybox.insert(END,'\t'+tea_ins_complaint[i]+'\n\n')
        self.displaybox.config(state=DISABLED)


    def tea_OnStudent(self):

        self.displaybox.config(state=NORMAL)
        self.displaybox.delete('1.0',END)

        category = 'On Students'
        #college_code = self.college_code.get()
        tea_stu_complaint = View_Data.Teacher(category,college_code)

        for i in range(len(tea_stu_complaint)):
            
            if tea_stu_complaint.index(tea_stu_complaint[i])%2 == 0:
                self.displaybox.insert(END,tea_stu_complaint[i]+'\n')
                continue
            self.displaybox.insert(END,'\t'+tea_stu_complaint[i]+'\n\n')
        self.displaybox.config(state=DISABLED)

    def tea_OnOther(self):

        self.displaybox.config(state=NORMAL)
        self.displaybox.delete('1.0',END)

        category = 'Others'
        #college_code = self.college_code.get()
        tea_other_complaint = View_Data.Teacher(category,college_code)

        for i in range(len(tea_other_complaint)):
            
            if tea_other_complaint.index(tea_other_complaint[i])%2 == 0:
                self.displaybox.insert(END,tea_other_complaint[i]+'\n')
                continue
            self.displaybox.insert(END,'\t'+tea_other_complaint[i]+'\n\n')
        self.displaybox.config(state=DISABLED)


if __name__ == '__main__':
    print('done')
    root = Tk()
    myApp = Admin(root)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(width=False, height=False)
    multiprocessing.freeze_support()
    root.mainloop()
